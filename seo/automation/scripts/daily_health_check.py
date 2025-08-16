#!/usr/bin/env python3
"""
Daily SEO Health Check Automation
Runs comprehensive site health checks and sends alerts
"""

import requests
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SEOHealthChecker:
    def __init__(self):
        self.base_url = "https://dryallekurutemizleme.com"
        self.critical_pages = [
            "/",
            "/hizmetler/kuru-temizleme.html",
            "/hizmetler/hali-yikama.html",
            "/hizmetler/koltuk-yikama.html",
            "/bolgeler/kadikoy-kuru-temizleme.html",
            "/bolgeler/atasehir-hali-yikama.html"
        ]
        self.alerts = []
    
    def check_page_speed(self, url):
        """Check page speed using PageSpeed Insights API"""
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        params = {
            'url': url,
            'strategy': 'mobile',
            'category': ['performance', 'seo', 'accessibility']
        }
        
        try:
            response = requests.get(api_url, params=params)
            data = response.json()
            
            performance_score = data['lighthouseResult']['categories']['performance']['score'] * 100
            seo_score = data['lighthouseResult']['categories']['seo']['score'] * 100
            
            if performance_score < 90:
                self.alerts.append(f"⚠️ Performance issue: {url} scored {performance_score}")
            
            if seo_score < 95:
                self.alerts.append(f"🔍 SEO issue: {url} scored {seo_score}")
                
            return {
                'url': url,
                'performance': performance_score,
                'seo': seo_score,
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            self.alerts.append(f"❌ Error checking {url}: {str(e)}")
            return None
    
    def check_broken_links(self):
        """Check for broken internal links"""
        broken_links = []
        
        for page in self.critical_pages:
            try:
                response = requests.get(self.base_url + page, timeout=10)
                if response.status_code != 200:
                    broken_links.append(f"{page} - Status: {response.status_code}")
                    self.alerts.append(f"🔗 Broken link: {page} ({response.status_code})")
            except Exception as e:
                broken_links.append(f"{page} - Error: {str(e)}")
                self.alerts.append(f"🔗 Link error: {page} - {str(e)}")
        
        return broken_links
    
    def check_ssl_certificate(self):
        """Check SSL certificate validity"""
        try:
            response = requests.get(self.base_url, timeout=10)
            if not response.url.startswith('https://'):
                self.alerts.append("🔒 SSL issue: Site not serving HTTPS")
                return False
        except Exception as e:
            self.alerts.append(f"🔒 SSL check failed: {str(e)}")
            return False
        
        return True
    
    def generate_report(self):
        """Generate daily health report"""
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'status': 'healthy' if len(self.alerts) == 0 else 'issues_detected',
            'alerts_count': len(self.alerts),
            'alerts': self.alerts,
            'checks_performed': [
                'page_speed_analysis',
                'broken_link_detection', 
                'ssl_certificate_validation'
            ]
        }
        
        return report
    
    def send_alert_email(self, report):
        """Send email alert if issues detected"""
        if len(self.alerts) == 0:
            return  # No alerts to send
        
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        email_user = "alerts@dryalle.com"
        email_password = "your_app_password"
        
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = "seo@dryalle.com"
        msg['Subject'] = f"🚨 SEO Health Alert - {report['alerts_count']} Issues Detected"
        
        body = f"""
        SEO Health Check Report - {report['date']}
        
        Status: {report['status'].upper()}
        Issues Detected: {report['alerts_count']}
        
        Alerts:
        {chr(10).join(self.alerts)}
        
        Please review and take necessary actions.
        
        Automated by Dry Alle SEO Monitoring System
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_user, email_password)
            server.send_message(msg)
            server.quit()
            print("Alert email sent successfully")
        except Exception as e:
            print(f"Failed to send alert email: {str(e)}")

def main():
    checker = SEOHealthChecker()
    
    # Run health checks
    print("🔍 Running daily SEO health check...")
    
    # Check page speeds
    for page in checker.critical_pages:
        url = checker.base_url + page
        result = checker.check_page_speed(url)
        if result:
            print(f"✅ Checked {page}")
    
    # Check for broken links
    broken_links = checker.check_broken_links()
    print(f"🔗 Checked {len(checker.critical_pages)} critical pages")
    
    # Check SSL
    ssl_status = checker.check_ssl_certificate()
    print(f"🔒 SSL Status: {'✅ Valid' if ssl_status else '❌ Issues'}")
    
    # Generate report
    report = checker.generate_report()
    
    # Save report
    with open(f'/tmp/seo_health_report_{report["date"]}.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    # Send alerts if needed
    if len(checker.alerts) > 0:
        checker.send_alert_email(report)
        print(f"🚨 {len(checker.alerts)} alerts generated and sent")
    else:
        print("✅ All checks passed - no issues detected")

if __name__ == "__main__":
    main()
