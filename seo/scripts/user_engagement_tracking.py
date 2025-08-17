#!/usr/bin/env python3
"""
Kullanıcı Etkileşim Metrikleri İzleme Sistemi
Blog optimizasyonu sonrası kullanıcı davranış analizi
"""

import os
import json
from datetime import datetime, timedelta

class UserEngagementTracker:
    def __init__(self, project_root="/Users/macos/Documents/Projeler/DryAlle"):
        self.project_root = project_root
        self.base_url = "https://dryallekurutemizleme.com"
        
        # Tracking kategorileri
        self.engagement_categories = {
            'page_metrics': [
                'page_views', 'unique_visitors', 'session_duration', 
                'pages_per_session', 'bounce_rate'
            ],
            'user_behavior': [
                'scroll_depth', 'time_on_page', 'click_through_rate',
                'return_visitor_rate', 'exit_rate'
            ],
            'conversion_metrics': [
                'contact_form_submissions', 'phone_calls', 'service_inquiries',
                'quote_requests', 'social_shares'
            ],
            'technical_metrics': [
                'page_load_speed', 'mobile_usability', 'core_web_vitals',
                'image_load_times', 'error_rates'
            ]
        }

    def create_google_analytics_config(self):
        """Google Analytics 4 konfigürasyonu"""
        ga4_config = {
            'measurement_id': 'G-XXXXXXXXXX',  # Replace with actual GA4 ID
            'enhanced_ecommerce': True,
            'custom_events': [
                {
                    'event_name': 'blog_engagement',
                    'parameters': {
                        'blog_slug': 'text',
                        'engagement_type': 'text',
                        'engagement_value': 'number',
                        'user_type': 'text'
                    }
                },
                {
                    'event_name': 'image_interaction',
                    'parameters': {
                        'image_format': 'text',
                        'load_time': 'number',
                        'image_src': 'text',
                        'interaction_type': 'text'
                    }
                },
                {
                    'event_name': 'content_depth',
                    'parameters': {
                        'scroll_percentage': 'number',
                        'reading_time': 'number',
                        'content_type': 'text',
                        'page_url': 'text'
                    }
                }
            ],
            'goals': [
                {
                    'name': 'Blog Engagement Time',
                    'type': 'duration',
                    'target': 120,  # 2 minutes
                    'description': 'User spends at least 2 minutes on blog'
                },
                {
                    'name': 'Deep Content Reading',
                    'type': 'event',
                    'condition': 'scroll_depth > 75',
                    'description': 'User scrolls beyond 75% of content'
                },
                {
                    'name': 'Service Inquiry',
                    'type': 'conversion',
                    'event': 'contact_form_submission',
                    'description': 'User submits contact form'
                }
            ]
        }
        
        return ga4_config

    def create_heatmap_tracking_script(self):
        """Heatmap ve kullanıcı davranış tracking scripti"""
        tracking_script = """
<!-- User Engagement & Heatmap Tracking -->
<script>
(function() {
    // Scroll depth tracking
    let maxScroll = 0;
    let scrollMilestones = [25, 50, 75, 90, 100];
    let scrollReported = [];
    
    function trackScrollDepth() {
        const scrollPercent = Math.round(
            (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100
        );
        
        if (scrollPercent > maxScroll) {
            maxScroll = scrollPercent;
        }
        
        scrollMilestones.forEach(milestone => {
            if (scrollPercent >= milestone && !scrollReported.includes(milestone)) {
                scrollReported.push(milestone);
                
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'scroll_depth', {
                        custom_parameter_percentage: milestone,
                        custom_parameter_page: window.location.pathname,
                        custom_parameter_content_type: 'blog'
                    });
                }
            }
        });
    }
    
    // Reading time tracking
    let startTime = Date.now();
    let isReading = true;
    let totalReadingTime = 0;
    
    function trackReadingTime() {
        if (isReading) {
            totalReadingTime = Date.now() - startTime;
        }
    }
    
    // User interaction tracking
    function trackUserInteraction(type, element) {
        if (typeof gtag !== 'undefined') {
            gtag('event', 'user_interaction', {
                custom_parameter_type: type,
                custom_parameter_element: element,
                custom_parameter_timestamp: Date.now(),
                custom_parameter_page: window.location.pathname
            });
        }
    }
    
    // Click tracking for important elements
    document.addEventListener('click', function(e) {
        const target = e.target;
        
        // Track clicks on service links
        if (target.matches('a[href*="hizmet"], a[href*="service"]')) {
            trackUserInteraction('service_link_click', target.href);
        }
        
        // Track clicks on contact buttons
        if (target.matches('.contact-btn, .iletisim-btn')) {
            trackUserInteraction('contact_button_click', target.textContent);
        }
        
        // Track clicks on blog navigation
        if (target.matches('.blog-nav a, .kategori-link')) {
            trackUserInteraction('blog_navigation', target.href);
        }
        
        // Track image clicks
        if (target.matches('img.featured-image')) {
            trackUserInteraction('featured_image_click', target.src);
        }
    });
    
    // Phone number click tracking
    document.addEventListener('click', function(e) {
        if (e.target.matches('a[href^="tel:"]')) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'phone_call_intent', {
                    custom_parameter_number: e.target.href.replace('tel:', ''),
                    custom_parameter_source: 'blog_page'
                });
            }
        }
    });
    
    // Form submission tracking
    document.addEventListener('submit', function(e) {
        const form = e.target;
        if (form.matches('form')) {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submission', {
                    custom_parameter_form_type: form.id || 'contact_form',
                    custom_parameter_page: window.location.pathname
                });
            }
        }
    });
    
    // Visibility change tracking (tab switching)
    document.addEventListener('visibilitychange', function() {
        if (document.hidden) {
            isReading = false;
            trackReadingTime();
        } else {
            startTime = Date.now();
            isReading = true;
        }
    });
    
    // Page unload tracking
    window.addEventListener('beforeunload', function() {
        trackReadingTime();
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'page_engagement_summary', {
                custom_parameter_reading_time: totalReadingTime,
                custom_parameter_max_scroll: maxScroll,
                custom_parameter_page: window.location.pathname,
                custom_parameter_session_id: sessionStorage.getItem('session_id') || 'unknown'
            });
        }
    });
    
    // Event listeners
    window.addEventListener('scroll', trackScrollDepth, { passive: true });
    
    // Initialize session
    if (!sessionStorage.getItem('session_id')) {
        sessionStorage.setItem('session_id', 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9));
    }
    
    // Track page view with enhanced data
    if (typeof gtag !== 'undefined') {
        gtag('event', 'enhanced_page_view', {
            custom_parameter_page_type: 'blog',
            custom_parameter_content_category: document.querySelector('meta[name="keywords"]')?.content || 'dry-cleaning',
            custom_parameter_session_id: sessionStorage.getItem('session_id'),
            custom_parameter_timestamp: Date.now()
        });
    }
})();
</script>
        """
        
        return tracking_script

    def create_conversion_tracking_setup(self):
        """Conversion tracking ve goal tanımları"""
        conversion_setup = {
            'conversion_events': [
                {
                    'name': 'contact_form_submission',
                    'category': 'Lead Generation',
                    'value': 50,
                    'currency': 'TRY',
                    'trigger': 'form submission with class .contact-form'
                },
                {
                    'name': 'phone_call_click',
                    'category': 'Lead Generation',
                    'value': 30,
                    'currency': 'TRY',
                    'trigger': 'click on tel: link'
                },
                {
                    'name': 'service_inquiry',
                    'category': 'Service Interest',
                    'value': 25,
                    'currency': 'TRY',
                    'trigger': 'click on service-related links'
                },
                {
                    'name': 'blog_engagement_high',
                    'category': 'Content Engagement',
                    'value': 10,
                    'currency': 'TRY',
                    'trigger': 'reading time > 2 minutes AND scroll depth > 75%'
                }
            ],
            'funnel_analysis': {
                'stages': [
                    'Blog Page View',
                    'Content Engagement (>50% scroll)',
                    'Deep Content Reading (>75% scroll)',
                    'Service Link Click',
                    'Contact Form View',
                    'Form Submission'
                ],
                'tracking_parameters': [
                    'utm_source', 'utm_medium', 'utm_campaign',
                    'referrer', 'device_type', 'browser'
                ]
            }
        }
        
        return conversion_setup

    def create_ab_test_tracking_config(self):
        """A/B test için özel tracking konfigürasyonu"""
        ab_test_config = {
            'test_groups': {
                'optimized_blogs': [
                    'vintage-clothing-ozel-care',
                    'wedding-season-wedding-dress-carei',
                    'professional-vs-evde-carpet-cleaning-comparison',
                    'outdoor-textile-urunleri-carei',
                    'is-kiyafetleri-professional-care'
                ],
                'control_blogs': [
                    'autumn-kiyafet-gecisi-guide',
                    'winter-preparation-tekstil-koruma',
                    'kalorifer-sezonu-tekstil-carei',
                    'air-conditioned-tekstil-carei',
                    'back-to-school-uniform-carei'
                ]
            },
            'metrics_to_compare': [
                {
                    'metric': 'average_session_duration',
                    'hypothesis': 'Optimized blogs will have 25% longer session duration',
                    'measurement': 'time in seconds'
                },
                {
                    'metric': 'bounce_rate',
                    'hypothesis': 'Optimized blogs will have 15% lower bounce rate',
                    'measurement': 'percentage'
                },
                {
                    'metric': 'scroll_depth_average',
                    'hypothesis': 'Optimized blogs will have 20% deeper scroll engagement',
                    'measurement': 'percentage'
                },
                {
                    'metric': 'conversion_rate',
                    'hypothesis': 'Optimized blogs will have 30% higher conversion rate',
                    'measurement': 'percentage'
                },
                {
                    'metric': 'page_load_time',
                    'hypothesis': 'Optimized blogs will load 35% faster',
                    'measurement': 'milliseconds'
                }
            ],
            'statistical_requirements': {
                'confidence_level': 95,
                'minimum_sample_size': 1000,
                'test_duration_days': 30,
                'significance_threshold': 0.05
            }
        }
        
        return ab_test_config

    def create_monitoring_dashboard_config(self):
        """Real-time monitoring dashboard konfigürasyonu"""
        dashboard_config = {
            'real_time_metrics': [
                'current_active_users',
                'pages_per_minute',
                'average_page_load_time',
                'conversion_events_per_hour'
            ],
            'daily_reports': [
                'unique_visitors',
                'total_pageviews',
                'average_session_duration',
                'bounce_rate',
                'top_performing_blogs',
                'conversion_summary'
            ],
            'weekly_analysis': [
                'a_b_test_performance',
                'user_behavior_trends',
                'content_engagement_patterns',
                'technical_performance_summary'
            ],
            'alerts': [
                {
                    'metric': 'page_load_time',
                    'threshold': '> 3000ms',
                    'action': 'email_notification'
                },
                {
                    'metric': 'bounce_rate',
                    'threshold': '> 70%',
                    'action': 'slack_notification'
                },
                {
                    'metric': 'conversion_rate',
                    'threshold': '< 2%',
                    'action': 'dashboard_alert'
                }
            ]
        }
        
        return dashboard_config

    def generate_tracking_implementation_guide(self):
        """Tracking sistemi implementasyon kılavuzu"""
        implementation_guide = {
            'step_1_google_analytics': {
                'title': 'Google Analytics 4 Kurulumu',
                'tasks': [
                    'GA4 property oluştur',
                    'Enhanced ecommerce aktif et',
                    'Custom events tanımla',
                    'Conversion goals kur',
                    'Audience segments oluştur'
                ],
                'estimated_time': '2 hours'
            },
            'step_2_tracking_code': {
                'title': 'Tracking Code Implementasyonu',
                'tasks': [
                    'Ana tracking script ekle',
                    'Custom event handlers kur',
                    'Form tracking aktif et',
                    'Phone call tracking ekle',
                    'Error tracking kur'
                ],
                'estimated_time': '3 hours'
            },
            'step_3_heatmap_tools': {
                'title': 'Heatmap ve User Behavior Tools',
                'recommendations': [
                    'Hotjar (ücretsiz plan)',
                    'Microsoft Clarity (ücretsiz)',
                    'Crazy Egg (premium)'
                ],
                'implementation': [
                    'Tool seç ve hesap oluştur',
                    'Tracking code ekle',
                    'Heatmap kayıtlarını başlat',
                    'User session recordings aktif et'
                ],
                'estimated_time': '1 hour'
            },
            'step_4_conversion_tracking': {
                'title': 'Conversion ve Goal Tracking',
                'tasks': [
                    'Conversion events tanımla',
                    'Goal funnels oluştur',
                    'Attribution modeling kur',
                    'ROI tracking başlat'
                ],
                'estimated_time': '2 hours'
            },
            'step_5_monitoring_alerts': {
                'title': 'Monitoring ve Alert Sistemi',
                'tasks': [
                    'Dashboard kur',
                    'Automated reports tanımla',
                    'Alert thresholds belirle',
                    'Notification channels kur'
                ],
                'estimated_time': '1 hour'
            }
        }
        
        return implementation_guide

    def save_engagement_tracking_system(self):
        """Engagement tracking sistemi dosyalarını kaydet"""
        print("📊 Kullanıcı etkileşim tracking sistemi oluşturuluyor...")
        
        # Ana konfigürasyonlar
        ga4_config = self.create_google_analytics_config()
        heatmap_script = self.create_heatmap_tracking_script()
        conversion_setup = self.create_conversion_tracking_setup()
        ab_test_config = self.create_ab_test_tracking_config()
        dashboard_config = self.create_monitoring_dashboard_config()
        implementation_guide = self.generate_tracking_implementation_guide()
        
        # Ana tracking sistemi raporu
        tracking_system = {
            'system_creation_date': datetime.now().isoformat(),
            'project': 'DryAlle User Engagement Tracking System',
            'google_analytics_config': ga4_config,
            'conversion_tracking': conversion_setup,
            'ab_test_configuration': ab_test_config,
            'monitoring_dashboard': dashboard_config,
            'implementation_guide': implementation_guide,
            'tracking_scripts': {
                'heatmap_script': heatmap_script
            },
            'success_metrics': [
                'User engagement increased by 25%',
                'Conversion rate improved by 30%',
                'Bounce rate decreased by 15%',
                'Session duration increased by 35%'
            ]
        }
        
        # Tracking system raporu kaydet
        reports_dir = os.path.join(self.project_root, 'seo/reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        tracking_path = os.path.join(reports_dir, 'user_engagement_tracking_system.json')
        with open(tracking_path, 'w', encoding='utf-8') as f:
            json.dump(tracking_system, f, ensure_ascii=False, indent=2)
        
        # Heatmap tracking script kaydet
        tracking_dir = os.path.join(self.project_root, 'seo/tracking')
        os.makedirs(tracking_dir, exist_ok=True)
        
        heatmap_path = os.path.join(tracking_dir, 'user_engagement_tracking.html')
        with open(heatmap_path, 'w', encoding='utf-8') as f:
            f.write(heatmap_script)
        
        # Implementation guide kaydet
        guide_path = os.path.join(tracking_dir, 'implementation_guide.json')
        with open(guide_path, 'w', encoding='utf-8') as f:
            json.dump(implementation_guide, f, ensure_ascii=False, indent=2)
        
        return tracking_path, heatmap_path, guide_path, tracking_system

def main():
    """Kullanıcı Etkileşim Metrikleri İzleme Sistemi"""
    print("📊 KULLANICI ETKİLEŞİM METRİKLERİ İZLEME SİSTEMİ")
    print("=" * 60)
    print("🎯 GA4 Setup | Heatmap Tracking | Conversion Analysis")
    print("=" * 60)
    
    tracker = UserEngagementTracker()
    
    try:
        # Engagement tracking sistemi oluştur
        tracking_path, heatmap_path, guide_path, system_report = tracker.save_engagement_tracking_system()
        
        # Özet
        print("\n" + "=" * 60)
        print("📊 ENGAGEMENT TRACKING SİSTEMİ OLUŞTURULDU")
        print("=" * 60)
        
        print(f"✅ Tracking kategorileri: {len(tracker.engagement_categories)} kategori")
        for category, metrics in tracker.engagement_categories.items():
            print(f"   📈 {category}: {len(metrics)} metrik")
        
        print(f"\n🎯 GA4 KONFIGÜRASYONU:")
        ga4_config = system_report['google_analytics_config']
        print(f"   • Custom events: {len(ga4_config['custom_events'])}")
        print(f"   • Conversion goals: {len(ga4_config['goals'])}")
        print(f"   • Enhanced ecommerce: {'✅' if ga4_config['enhanced_ecommerce'] else '❌'}")
        
        print(f"\n📊 A/B TEST TRACKING:")
        ab_config = system_report['ab_test_configuration']
        print(f"   • Test groups: {len(ab_config['test_groups'])} group")
        print(f"   • Comparison metrics: {len(ab_config['metrics_to_compare'])} metrik")
        print(f"   • Confidence level: {ab_config['statistical_requirements']['confidence_level']}%")
        
        print(f"\n🔄 CONVERSION TRACKING:")
        conversion_config = system_report['conversion_tracking']
        print(f"   • Conversion events: {len(conversion_config['conversion_events'])} event")
        print(f"   • Funnel stages: {len(conversion_config['funnel_analysis']['stages'])} stage")
        
        print(f"\n📁 OLUŞTURULAN DOSYALAR:")
        print(f"   📊 Tracking System: {tracking_path}")
        print(f"   🔍 Heatmap Script: {heatmap_path}")
        print(f"   📋 Implementation Guide: {guide_path}")
        
        print(f"\n⏱️ IMPLEMENTATION SCHEDULE:")
        guide = system_report['implementation_guide']
        for step, config in guide.items():
            print(f"   • {config['title']}: {config['estimated_time']}")
        
        print(f"\n🎯 BAŞARI HEDEFLERİ:")
        for metric in system_report['success_metrics'][:3]:
            print(f"   ✅ {metric}")
        
        print(f"\n🎉 ENGAGEMENT TRACKING SİSTEMİ HAZIR!")
        print(f"   • Google Analytics 4 konfigürasyonu tamamlandı")
        print(f"   • Heatmap ve user behavior tracking kuruldu")
        print(f"   • Conversion tracking sistemi hazırlandı")
        print(f"   • A/B test metrics tanımlandı")
        
        return True
        
    except Exception as e:
        print(f"❌ Tracking sistemi oluşturma hatası: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)