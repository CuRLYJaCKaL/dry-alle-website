#!/usr/bin/env python3
"""
Real-time SEO Monitoring Dashboard Server
Provides live data for the SEO dashboard
"""

from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import json
import os
import sqlite3
import random

app = Flask(__name__)

class SEODataProvider:
    def __init__(self):
        self.db_path = "/tmp/seo_monitoring.db"
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for storing SEO metrics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables for different metrics
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS traffic_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                organic_sessions INTEGER,
                pageviews INTEGER,
                bounce_rate REAL,
                conversion_rate REAL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS keyword_rankings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                keyword TEXT NOT NULL,
                position INTEGER,
                previous_position INTEGER,
                url TEXT,
                date TEXT NOT NULL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS technical_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                metric_name TEXT NOT NULL,
                metric_value REAL,
                threshold_value REAL,
                status TEXT,
                date TEXT NOT NULL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_current_metrics(self):
        """Get current SEO metrics"""
        # In production, this would fetch real data from Google Analytics, Search Console, etc.
        # For demo purposes, we'll generate realistic sample data
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        metrics = {
            'organic_traffic': {
                'value': 12847,
                'change': 23.5,
                'trend': 'up'
            },
            'avg_ranking': {
                'value': 4.2,
                'change': 1.3,
                'trend': 'up'
            },
            'conversion_rate': {
                'value': 8.9,
                'change': 0.7,
                'trend': 'up'
            },
            'site_speed_mobile': {
                'value': 94,
                'change': 2,
                'trend': 'up'
            },
            'gmb_views': {
                'value': 3456,
                'change': 18.2,
                'trend': 'up'
            },
            'whatsapp_clicks': {
                'value': 1238,
                'change': 31.4,
                'trend': 'up'
            }
        }
        
        return metrics
    
    def get_keyword_rankings(self):
        """Get current keyword rankings"""
        keywords = [
            {'keyword': 'kuru temizleme istanbul', 'position': 2, 'change': 1, 'trend': 'up'},
            {'keyword': 'hali yikama kadikoy', 'position': 1, 'change': 0, 'trend': 'same'},
            {'keyword': 'koltuk yikama atasehir', 'position': 3, 'change': 2, 'trend': 'up'},
            {'keyword': 'perde temizleme istanbul', 'position': 4, 'change': 3, 'trend': 'up'},
            {'keyword': 'ev tekstili bakimi', 'position': 5, 'change': 1, 'trend': 'up'},
            {'keyword': 'profesyonel hali yikama', 'position': 6, 'change': -1, 'trend': 'down'},
            {'keyword': 'kuru temizleme fiyatlari', 'position': 7, 'change': 2, 'trend': 'up'},
            {'keyword': 'tekstil bakim hizmetleri', 'position': 8, 'change': 0, 'trend': 'same'},
            {'keyword': 'sahrayicedit temizleme', 'position': 2, 'change': 1, 'trend': 'up'},
            {'keyword': 'umraniye kuru temizleme', 'position': 1, 'change': 2, 'trend': 'up'}
        ]
        
        return keywords
    
    def get_traffic_trend(self, days=30):
        """Get traffic trend for the last N days"""
        trend_data = []
        base_traffic = 8000
        
        for i in range(days):
            date = (datetime.now() - timedelta(days=days-i-1)).strftime('%Y-%m-%d')
            # Simulate realistic traffic with growth trend and weekly patterns
            weekly_factor = 1.2 if (i % 7) in [0, 6] else 1.0  # Weekend boost
            growth_factor = 1 + (i * 0.01)  # Gradual growth
            daily_traffic = int(base_traffic * weekly_factor * growth_factor + random.randint(-500, 500))
            
            trend_data.append({
                'date': date,
                'traffic': daily_traffic,
                'conversions': int(daily_traffic * 0.08)  # 8% conversion rate
            })
        
        return trend_data
    
    def get_alerts(self):
        """Get current system alerts"""
        alerts = [
            {
                'type': 'success',
                'icon': '✅',
                'title': 'Site Hızı Optimizasyonu Başarılı',
                'message': 'Tüm sayfalar 95+ Lighthouse skoruna ulaştı',
                'timestamp': '2 saat önce'
            },
            {
                'type': 'warning',
                'icon': '⚠️',
                'title': 'Blog İçerik Güncellemesi Gerekli',
                'message': '5 blog yazısı 3+ aydır güncellenmemiş',
                'timestamp': '1 gün önce'
            },
            {
                'type': 'success',
                'icon': '🎯',
                'title': 'Yeni Anahtar Kelime Fırsatı',
                'message': '"istanbul elit temizleme" için content gap tespit edildi',
                'timestamp': '3 saat önce'
            },
            {
                'type': 'error',
                'icon': '🔧',
                'title': 'Teknik SEO Uyarısı',
                'message': '2 sayfada broken link tespit edildi - acil düzeltme gerekli',
                'timestamp': '30 dakika önce'
            }
        ]
        
        return alerts
    
    def get_weekly_performance(self):
        """Get weekly performance comparison"""
        return {
            'current_week': {
                'organic_traffic': 12847,
                'phone_calls': 387,
                'whatsapp_messages': 1238,
                'form_submissions': 156,
                'avg_ranking': 4.2
            },
            'previous_week': {
                'organic_traffic': 10412,
                'phone_calls': 342,
                'whatsapp_messages': 943,
                'form_submissions': 134,
                'avg_ranking': 5.5
            },
            'targets': {
                'organic_traffic': 12000,
                'phone_calls': 350,
                'whatsapp_messages': 1000,
                'form_submissions': 150,
                'avg_ranking': 5.0
            }
        }

# Initialize data provider
data_provider = SEODataProvider()

@app.route('/')
def dashboard():
    """Serve the main dashboard"""
    return render_template('dashboard.html')

@app.route('/api/metrics')
def get_metrics():
    """API endpoint for current metrics"""
    metrics = data_provider.get_current_metrics()
    return jsonify(metrics)

@app.route('/api/keywords')
def get_keywords():
    """API endpoint for keyword rankings"""
    keywords = data_provider.get_keyword_rankings()
    return jsonify(keywords)

@app.route('/api/traffic-trend')
def get_traffic_trend():
    """API endpoint for traffic trend data"""
    days = int(request.args.get('days', 30))
    trend_data = data_provider.get_traffic_trend(days)
    return jsonify(trend_data)

@app.route('/api/alerts')
def get_alerts():
    """API endpoint for system alerts"""
    alerts = data_provider.get_alerts()
    return jsonify(alerts)

@app.route('/api/weekly-performance')
def get_weekly_performance():
    """API endpoint for weekly performance data"""
    performance = data_provider.get_weekly_performance()
    return jsonify(performance)

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Create a simple dashboard template
    dashboard_template = '''<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dry Alle SEO Dashboard - Live</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; }
        .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 20px; }
        .metric-card { background: white; padding: 20px; border-radius: 10px; text-align: center; }
        .metric-value { font-size: 36px; font-weight: bold; color: #2c3e50; }
        .metric-change { color: #27ae60; font-size: 14px; }
        .chart-container { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .refresh-indicator { position: fixed; top: 20px; right: 20px; background: #27ae60; color: white; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="refresh-indicator" id="refreshIndicator">🔄 Güncelleniyor...</div>
    
    <div class="container">
        <div class="header">
            <h1>🏆 Dry Alle SEO Dashboard - Canlı İzleme</h1>
            <p>Son güncelleme: <span id="lastUpdate"></span></p>
        </div>
        
        <div class="metrics-grid" id="metricsGrid">
            <!-- Metrics will be populated by JavaScript -->
        </div>
        
        <div class="chart-container">
            <h3>📈 30 Günlük Trafik Trendi</h3>
            <canvas id="trafficChart"></canvas>
        </div>
    </div>
    
    <script>
        let trafficChart;
        
        function updateMetrics() {
            fetch('/api/metrics')
                .then(response => response.json())
                .then(data => {
                    const grid = document.getElementById('metricsGrid');
                    grid.innerHTML = '';
                    
                    Object.entries(data).forEach(([key, metric]) => {
                        const card = document.createElement('div');
                        card.className = 'metric-card';
                        card.innerHTML = `
                            <h3>${key.replace('_', ' ').toUpperCase()}</h3>
                            <div class="metric-value">${metric.value.toLocaleString()}</div>
                            <div class="metric-change">↗️ +${metric.change}%</div>
                        `;
                        grid.appendChild(card);
                    });
                });
        }
        
        function updateTrafficChart() {
            fetch('/api/traffic-trend')
                .then(response => response.json())
                .then(data => {
                    const ctx = document.getElementById('trafficChart').getContext('2d');
                    
                    if (trafficChart) {
                        trafficChart.destroy();
                    }
                    
                    trafficChart = new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: data.map(d => d.date),
                            datasets: [{
                                label: 'Organik Trafik',
                                data: data.map(d => d.traffic),
                                borderColor: '#3498db',
                                backgroundColor: 'rgba(52, 152, 219, 0.1)',
                                tension: 0.4
                            }]
                        },
                        options: {
                            responsive: true,
                            scales: {
                                y: {
                                    beginAtZero: false
                                }
                            }
                        }
                    });
                });
        }
        
        function updateDashboard() {
            document.getElementById('refreshIndicator').style.display = 'block';
            
            updateMetrics();
            updateTrafficChart();
            
            document.getElementById('lastUpdate').textContent = new Date().toLocaleString('tr-TR');
            
            setTimeout(() => {
                document.getElementById('refreshIndicator').style.display = 'none';
            }, 1000);
        }
        
        // Initial load
        updateDashboard();
        
        // Auto-refresh every 5 minutes
        setInterval(updateDashboard, 300000);
    </script>
</body>
</html>'''
    
    with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
        f.write(dashboard_template)
    
    print("🚀 Starting SEO Monitoring Dashboard Server...")
    print("📊 Dashboard available at: http://localhost:5000")
    print("🔌 API endpoints available at: http://localhost:5000/api/")
    
    app.run(debug=True, host='0.0.0.0', port=5000)