#!/usr/bin/env python3
"""
Keyword Ranking Monitor
Tracks keyword positions and alerts on significant changes
"""

import requests
import json
from datetime import datetime, timedelta
import csv

class KeywordRankingMonitor:
    def __init__(self):
        self.keywords = [
            "kuru temizleme istanbul",
            "hali yikama kadikoy", 
            "koltuk yikama atasehir",
            "perde temizleme istanbul",
            "ev tekstili bakimi",
            "profesyonel hali yikama",
            "kuru temizleme fiyatlari",
            "tekstil bakim hizmetleri",
            "sahrayicedit temizleme",
            "umraniye kuru temizleme"
        ]
        self.domain = "dryallekurutemizleme.com"
        self.rankings_history = []
    
    def check_ranking(self, keyword):
        """Check ranking for a specific keyword"""
        # This would integrate with SEO tools API like SEMrush, Ahrefs, or custom scraper
        # For demo purposes, we'll simulate ranking data
        
        import random
        
        # Simulate ranking (in real implementation, use actual API)
        current_position = random.randint(1, 15)
        
        ranking_data = {
            'keyword': keyword,
            'domain': self.domain,
            'position': current_position,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'timestamp': datetime.now().isoformat()
        }
        
        return ranking_data
    
    def compare_with_previous(self, current_ranking):
        """Compare current ranking with previous day"""
        # Load previous rankings
        try:
            with open('/tmp/keyword_rankings_history.json', 'r') as f:
                history = json.load(f)
        except FileNotFoundError:
            return None
        
        # Find previous ranking for same keyword
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        for record in history:
            if record['keyword'] == current_ranking['keyword'] and record['date'] == yesterday:
                position_change = record['position'] - current_ranking['position']
                return {
                    'previous_position': record['position'],
                    'current_position': current_ranking['position'],
                    'change': position_change,
                    'change_direction': 'up' if position_change > 0 else 'down' if position_change < 0 else 'same'
                }
        
        return None
    
    def generate_ranking_report(self):
        """Generate comprehensive ranking report"""
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'total_keywords': len(self.keywords),
            'rankings': [],
            'summary': {
                'improved': 0,
                'declined': 0,
                'unchanged': 0,
                'average_position': 0
            }
        }
        
        total_positions = 0
        
        for keyword in self.keywords:
            current_ranking = self.check_ranking(keyword)
            comparison = self.compare_with_previous(current_ranking)
            
            ranking_info = {
                'keyword': keyword,
                'current_position': current_ranking['position'],
                'change': comparison['change'] if comparison else 0,
                'status': comparison['change_direction'] if comparison else 'new'
            }
            
            report['rankings'].append(ranking_info)
            self.rankings_history.append(current_ranking)
            total_positions += current_ranking['position']
            
            # Update summary
            if comparison:
                if comparison['change'] > 0:
                    report['summary']['improved'] += 1
                elif comparison['change'] < 0:
                    report['summary']['declined'] += 1
                else:
                    report['summary']['unchanged'] += 1
        
        report['summary']['average_position'] = round(total_positions / len(self.keywords), 1)
        
        return report
    
    def save_rankings_history(self):
        """Save rankings to history file"""
        try:
            with open('/tmp/keyword_rankings_history.json', 'r') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []
        
        history.extend(self.rankings_history)
        
        with open('/tmp/keyword_rankings_history.json', 'w') as f:
            json.dump(history, f, indent=2)
    
    def export_to_csv(self, report):
        """Export rankings to CSV for analysis"""
        filename = f'/tmp/keyword_rankings_{report["date"]}.csv'
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['keyword', 'current_position', 'change', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for ranking in report['rankings']:
                writer.writerow(ranking)

def main():
    monitor = KeywordRankingMonitor()
    
    print("🎯 Starting keyword ranking monitoring...")
    
    # Generate report
    report = monitor.generate_ranking_report()
    
    # Save history
    monitor.save_rankings_history()
    
    # Export to CSV
    monitor.export_to_csv(report)
    
    # Print summary
    print(f"📊 Ranking Summary for {report['date']}:")
    print(f"   Average Position: {report['summary']['average_position']}")
    print(f"   Improved: {report['summary']['improved']} keywords")
    print(f"   Declined: {report['summary']['declined']} keywords")
    print(f"   Unchanged: {report['summary']['unchanged']} keywords")
    
    # Alert on significant changes
    significant_changes = [r for r in report['rankings'] if abs(r['change']) >= 3]
    if significant_changes:
        print(f"🚨 {len(significant_changes)} significant ranking changes detected!")
        for change in significant_changes:
            direction = "⬆️" if change['change'] > 0 else "⬇️"
            print(f"   {direction} {change['keyword']}: {change['change']} positions")

if __name__ == "__main__":
    main()
