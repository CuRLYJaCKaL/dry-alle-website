class DryAlleCustomElement extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.render();
        this.setupEventListeners();
    }

    render() {
        this.shadowRoot.innerHTML = `
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                :host {
                    display: block;
                    font-family: 'Roboto', sans-serif;
                    line-height: 1.2;
                    color: #333;
                }

                /* Yellow Top Bar */
                .top-bar {
                    background-color: #f6ec3d;
                    padding: 8px 0;
                    text-align: center;
                    font-size: 14px;
                    color: #333;
                }

                .top-bar-content {
                    max-width: 1600px;
                    margin: 0 auto;
                    padding: 0 60px;
                }

                .top-bar strong {
                    font-weight: 700;
                    text-decoration: underline;
                }

                /* Main Header */
                .header {
                    background-color: #006a44;
                    color: white;
                    transition: transform 0.3s ease, background-color 0.3s ease;
                }

                .header-container {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 40px;
                    max-width: 1600px;
                    margin: 0 auto;
                }

                .logo svg {
                    display: block;
                }

                .contact-button {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    color: white;
                    cursor: pointer;
                    background: rgba(255,255,255,0.1);
                    padding: 8px 16px;
                    border-radius: 20px;
                    transition: background 0.3s ease;
                }

                .contact-button:hover {
                    background: rgba(255,255,255,0.2);
                }

                .phone-icon {
                    font-size: 20px;
                }

                /* Navigation */
                .main-nav {
                    background-color: white;
                    border-bottom: 1px solid #e6e7e8;
                }

                .nav-menu {
                    display: flex;
                    list-style: none;
                    max-width: 1600px;
                    margin: 0 auto;
                    padding: 0 36px;
                    justify-content: flex-start;
                    gap: 80px;
                }

                .nav-menu li {
                    padding: 12px 0;
                }

                .nav-menu a {
                    text-decoration: none;
                    color: #006a44;
                    font-weight: 600;
                    font-size: 14px;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                    transition: color 0.3s ease;
                }

                .nav-menu a:hover {
                    color: #00623b;
                }

                /* Hero Section */
                .hero {
                    position: relative;
                    height: 475px;
                    overflow: hidden;
                    background: linear-gradient(135deg, #f6ec3d 0%, #006a44 100%);
                }

                .hero-background {
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    z-index: 1;
                }

                .hero-background::after {
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: linear-gradient(to left, transparent 0%, transparent 20%, rgba(255,255,255,0.05) 25%, rgba(255,255,255,0.15) 30%, rgba(255,255,255,0.3) 35%, rgba(255,255,255,0.5) 40%, rgba(255,255,255,0.7) 43%, rgba(255,255,255,0.85) 46%, rgba(255,255,255,0.95) 48%, rgba(255,255,255,1) 50%, rgba(255,255,255,1) 100%);
                    z-index: 2;
                }

                .hero-image {
                    width: 50%;
                    height: 100%;
                    object-fit: cover;
                    object-position: right center;
                    position: absolute;
                    right: 0;
                    top: 0;
                }

                .hero-content {
                    position: absolute;
                    top: 50%;
                    left: 60px;
                    transform: translateY(-50%);
                    z-index: 3;
                    color: #00623b;
                    max-width: 600px;
                }

                .hero-title {
                    font-size: 48px;
                    font-weight: 700;
                    line-height: 1.1;
                    margin-bottom: 40px;
                    text-shadow: 2px 2px 4px rgba(255,255,255,0.8);
                    animation: fadeInUp 1s ease;
                }

                .hero-contact h3 {
                    font-size: 24px;
                    font-weight: 600;
                    color: #00623b;
                    margin-bottom: 20px;
                }

                .contact-info {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }

                .contact-item {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    font-size: 18px;
                }

                .contact-icon {
                    font-size: 20px;
                }

                .contact-text {
                    color: #006a44;
                    text-decoration: none;
                    font-weight: 500;
                }

                .contact-text:hover {
                    text-decoration: underline;
                }

                .call-btn {
                    background: #006a44;
                    color: white;
                    border: none;
                    padding: 12px 24px;
                    border-radius: 25px;
                    font-size: 16px;
                    font-weight: 600;
                    cursor: pointer;
                    margin-top: 15px;
                    transition: background 0.3s ease, transform 0.3s ease;
                }

                .call-btn:hover {
                    background: #00623b;
                    transform: translateY(-2px);
                }

                /* Service Icons Section */
                .service-icons {
                    padding: 30px 0;
                    background-color: white;
                }

                .service-icon-container {
                    display: flex;
                    justify-content: center;
                    gap: 400px;
                    max-width: 1600px;
                    margin: 0 auto;
                }

                .service-icon-item {
                    text-align: center;
                }

                .service-icon-item .icon {
                    width: 60px;
                    height: 60px;
                    background-color: #00623B;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 30px;
                    color: white;
                    margin: 0 auto 12px;
                    transition: transform 0.3s ease;
                }

                .service-icon-item .icon:hover {
                    transform: scale(1.1);
                }

                .service-icon-item h4 {
                    font-size: 14px;
                    color: #00623B;
                    font-weight: 500;
                }

                /* Services Section */
                .services {
                    padding: 40px 0;
                    background-color: white;
                }

                .container {
                    max-width: 1800px;
                    margin: 0 auto;
                    padding: 0 75px;
                }

                .services-title {
                    text-align: center;
                    font-size: 28px;
                    color: #00623b;
                    margin-bottom: 24px;
                    font-weight: 700;
                }

                .services-grid {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 28px;
                    margin: 30px 2px;
                }

                .service-card {
                    background: #f0f0f0;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                    display: flex;
                    flex-direction: column;
                    opacity: 0;
                    transform: translateY(30px);
                    animation: fadeInUp 0.6s ease forwards;
                }

                .service-card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 8px 25px rgba(0,106,68,0.15);
                }

                .service-card img {
                    width: 100%;
                    height: 230px;
                    object-fit: cover;
                    transition: transform 0.3s ease;
                    display: block;
                }

                .service-card:hover img {
                    transform: scale(1.02);
                }

                .service-content {
                    padding: 20px;
                    text-align: left;
                    background: #e1e1e1;
                    flex: 1;
                    min-height: 130px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                }

                .service-content h3 {
                    color: #00623B;
                    font-size: 20px;
                    margin-bottom: 10px;
                    font-weight: 600;
                    line-height: 1.2;
                }

                .service-content p {
                    color: #006a44;
                    line-height: 1.4;
                    margin-bottom: 15px;
                    font-size: 14px;
                    font-weight: 400;
                    flex: 1;
                }

                .find-out-more {
                    color: #00623B;
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 14px;
                    transition: color 0.3s ease;
                    margin-top: auto;
                }

                .find-out-more:hover {
                    color: #004d2d;
                    text-decoration: underline;
                }

                /* About Section */
                .about-section {
                    background-color: white;
                    padding: 30px 0 15px 0;
                }

                .contact-info-card {
                    display: flex;
                    max-width: 1650px;
                    margin: 0 auto;
                    padding: 40px 75px;
                    gap: 40px;
                    align-items: center;
                    margin-bottom: 60px;
                    background-color: #e6e7e8;
                    border-radius: 10px;
                }

                .contact-text {
                    flex: 1;
                }

                .contact-text h2 {
                    color: #006a44;
                    font-size: 32px;
                    margin-bottom: 20px;
                    font-weight: 600;
                }

                .contact-text p {
                    color: #666;
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 25px;
                }

                .learn-more-btn {
                    color: #006a44;
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 16px;
                    transition: color 0.3s ease;
                }

                .learn-more-btn:hover {
                    color: #004d2d;
                    text-decoration: underline;
                }

                .contact-image {
                    flex: 1;
                    max-width: 500px;
                }

                .contact-image img {
                    width: 100%;
                    height: 300px;
                    object-fit: cover;
                    border-radius: 8px;
                }

                /* Contact Info Section */
                .contact-info-section {
                    background-color: white;
                    padding: 20px 0 40px 0;
                }

                .address-info {
                    display: flex;
                    justify-content: space-between;
                    max-width: 1800px;
                    margin: 0 auto;
                    padding: 0 75px;
                    gap: 40px;
                }

                .address-item {
                    flex: 1;
                    text-align: center;
                    padding: 30px 20px;
                    background: #f8f9fa;
                    border-radius: 10px;
                    transition: transform 0.3s ease;
                }

                .address-item:hover {
                    transform: translateY(-5px);
                }

                .address-item h3 {
                    color: #006a44;
                    font-size: 20px;
                    margin-bottom: 15px;
                    font-weight: 600;
                }

                .address-item p {
                    color: #666;
                    font-size: 15px;
                    line-height: 1.5;
                }

                .address-item a {
                    color: #006a44;
                    text-decoration: none;
                }

                .address-item a:hover {
                    text-decoration: underline;
                }

                /* Footer */
                .footer {
                    background-color: #006a44;
                    padding: 40px 0;
                    text-align: center;
                }

                .footer-content {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 0 40px;
                }

                .footer-info p {
                    color: white;
                    font-size: 14px;
                    margin: 0;
                }

                /* Animations */
                @keyframes fadeInUp {
                    from {
                        opacity: 0;
                        transform: translateY(30px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .service-card:nth-child(1) { animation-delay: 0.1s; }
                .service-card:nth-child(2) { animation-delay: 0.2s; }
                .service-card:nth-child(3) { animation-delay: 0.3s; }

                /* Responsive Design */
                @media screen and (max-width: 1024px) {
                    .hero-content {
                        left: 40px;
                        max-width: 500px;
                    }
                    
                    .hero-title {
                        font-size: 40px;
                    }
                    
                    .service-icon-container {
                        gap: 100px;
                    }
                    
                    .contact-info-card {
                        margin: 0 20px;
                        padding: 30px;
                    }
                }

                @media screen and (max-width: 768px) {
                    .header-container {
                        padding: 15px 20px;
                    }
                    
                    .nav-menu {
                        flex-direction: column;
                        gap: 0;
                        padding: 0 20px;
                    }
                    
                    .nav-menu li {
                        padding: 10px 0;
                        border-bottom: 1px solid #e6e7e8;
                    }
                    
                    .hero {
                        height: 400px;
                    }
                    
                    .hero-content {
                        left: 20px;
                        right: 20px;
                        max-width: none;
                    }
                    
                    .hero-title {
                        font-size: 32px;
                    }
                    
                    .services-grid {
                        grid-template-columns: 1fr;
                        gap: 20px;
                    }
                    
                    .service-icon-container {
                        flex-direction: column;
                        gap: 40px;
                        align-items: center;
                    }
                    
                    .container {
                        padding: 0 20px;
                    }
                    
                    .contact-info-card {
                        flex-direction: column;
                        padding: 30px 20px;
                        gap: 30px;
                    }
                    
                    .address-info {
                        flex-direction: column;
                        padding: 0 20px;
                        gap: 20px;
                    }
                }

                @media screen and (max-width: 480px) {
                    .top-bar {
                        padding: 5px 0;
                        font-size: 12px;
                    }
                    
                    .hero-title {
                        font-size: 28px;
                    }
                    
                    .services-title {
                        font-size: 24px;
                    }
                    
                    .service-content h3 {
                        font-size: 18px;
                    }
                    
                    .service-content {
                        padding: 15px;
                    }
                }

                /* Smooth scrolling */
                html {
                    scroll-behavior: smooth;
                }
            </style>

            <div class="dry-alle-container">
                <!-- Blue Top Bar -->
                <div class="top-bar">
                    <div class="top-bar-content">
                        <span>Profesyonel kuru temizleme hizmeti için hemen <strong>ARAYINIZ: <a href="tel:+905433527474" style="color: #333; text-decoration: none;">0 (543) 352 74 74</a></strong></span>
                    </div>
                </div>

                <!-- Main Header -->
                <header class="header">
                    <div class="header-container">
                        <div class="logo">
                            <svg width="390" height="105" viewBox="0 0 390 105" xmlns="http://www.w3.org/2000/svg">
                                <text x="195" y="58" font-family="Dancing Script, cursive" font-size="60" font-weight="700" fill="#f6ec3d" text-anchor="middle">Dry Alle</text>
                                <text x="195" y="86" font-family="Roboto, sans-serif" font-size="16" font-weight="600" fill="white" letter-spacing="2px" text-anchor="middle">KURU TEMİZLEME</text>
                            </svg>
                        </div>
                        
                        <div class="contact-button">
                            <div class="phone-icon">📞</div>
                            <span>İletişim</span>
                        </div>
                    </div>
                    
                    <!-- Navigation -->
                    <nav class="main-nav">
                        <ul class="nav-menu">
                            <li><a href="#services">Hizmetlerimiz</a></li>
                            <li><a href="#about">Hakkımızda</a></li>
                            <li><a href="#contact">İletişim</a></li>
                        </ul>
                    </nav>
                </header>

                <main>
                    <!-- Hero Section -->
                    <section class="hero">
                        <div class="hero-background">
                            <img src="https://static.wixstatic.com/media/your-hero-image.jpg" alt="Dry Alle Kuru Temizleme" class="hero-image">
                        </div>
                        <div class="hero-content">
                            <h1 class="hero-title">
                                KALİTELİ TEMİZLİK<br>
                                DENEYİMLİ EKİP<br>
                                MÜKEMMEL SONUÇ
                            </h1>
                            <div class="hero-contact">
                                <h3>Hemen Randevu Alın</h3>
                                <div class="contact-info">
                                    <div class="contact-item">
                                        <span class="contact-icon">📞</span>
                                        <a href="tel:+905433527474" class="contact-text">0 (543) 352 74 74</a>
                                    </div>
                                    <div class="contact-item">
                                        <span class="contact-icon">📍</span>
                                        <span class="contact-text">Sahrayıcedit, Kadıköy, İstanbul</span>
                                    </div>
                                    <button class="call-btn">Hemen Ara</button>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Service Icons Section -->
                    <section class="service-icons">
                        <div class="service-icon-container">
                            <div class="service-icon-item">
                                <div class="icon">
                                    <svg width="32" height="32" viewBox="0 0 32 32" fill="currentColor">
                                        <path d="M28 8H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h24c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2z"/>
                                        <path d="M4 12h24v2H4z"/>
                                        <circle cx="8" cy="18" r="1.5"/>
                                        <circle cx="24" cy="18" r="1.5"/>
                                        <path d="M6 18h20v2H6z"/>
                                        <path d="M12 6v4h8V6l-4-2z"/>
                                    </svg>
                                </div>
                                <h4>Kapıdan Teslimat</h4>
                            </div>
                            <div class="service-icon-item">
                                <div class="icon">
                                    <svg width="32" height="32" viewBox="0 0 32 32" fill="currentColor">
                                        <path d="M16 2l4 8h8l-6.5 5 2.5 8L16 18l-8 5 2.5-8L4 10h8z"/>
                                        <circle cx="16" cy="25" r="2" fill="none" stroke="currentColor" stroke-width="1.5"/>
                                        <path d="M16 27v3" stroke="currentColor" stroke-width="1.5"/>
                                    </svg>
                                </div>
                                <h4>Kaliteli Hizmet</h4>
                            </div>
                        </div>
                    </section>

                    <!-- Main Services Section -->
                    <section class="services" id="services">
                        <div class="container">
                            <h2 class="services-title">En Popüler Hizmetlerimiz</h2>
                            
                            <div class="services-grid">
                                <!-- Row 1 -->
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/dry-cleaning.jpg" alt="Kuru Temizleme">
                                    <div class="service-content">
                                        <h3>Kuru Temizleme</h3>
                                        <p>Kıyafetlerinize özel profesyonel kuru temizleme hizmeti. Modern teknoloji ve çevreci çözümlerle giysileriniz güvenli ellerde.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/carpet-cleaning.jpg" alt="Halı Yıkama">
                                    <div class="service-content">
                                        <h3>Halı Yıkama</h3>
                                        <p>Halılarınızı hijyenik ve temiz tutmak için profesyonel yıkama hizmeti. Leke çıkarma ve derin temizlik garantisi.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/furniture-cleaning.jpg" alt="Koltuk Yıkama">
                                    <div class="service-content">
                                        <h3>Koltuk Yıkama</h3>
                                        <p>Koltuk takımlarınız için özel temizlik hizmeti. Kumaş ve deri koltuklar için uygun yöntemlerle hijyenik temizlik.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/home-textile-cleaning.jpg" alt="Ev Tekstili Temizliği">
                                    <div class="service-content">
                                        <h3>Ev Tekstili Temizliği</h3>
                                        <p>Perdeler, nevresimler ve ev tekstilleriniz için özel temizlik hizmeti. Narin kumaşlara özel hassas yıkama.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/fabric-leather-dyeing.jpg" alt="Kumaş ve Deri Boyama">
                                    <div class="service-content">
                                        <h3>Kumaş ve Deri Boyama</h3>
                                        <p>Solmuş kıyafetlerinize yeni hayat verin. Kumaş ve deri ürünleriniz için profesyonel renk yenileme hizmeti.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/shoe-polish-service.jpg" alt="Lostra Hizmeti">
                                    <div class="service-content">
                                        <h3>Lostra Hizmeti</h3>
                                        <p>Ayakkabı ve çantalarınızın ilk günkü parlaklığına kavuşması için profesyonel lostra hizmeti. Kusursuz görünüm garantisi.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/ironing-service.jpg" alt="Ütü Hizmetleri">
                                    <div class="service-content">
                                        <h3>Ütü Hizmetleri</h3>
                                        <p>Kıyafetleriniz için profesyonel ütü hizmeti. Gömlek, pantolon ve hassas kumaşlar için özel ütüleme teknikleri.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/curtain-blind-cleaning.jpg" alt="Store-Zebra Perde Temizleme">
                                    <div class="service-content">
                                        <h3>Store-Zebra Perde Temizleme</h3>
                                        <p>Store, zebra ve tüm perde türleri için özel temizlik hizmeti. Söküp takma dahil kapsamlı hizmet.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                                
                                <div class="service-card">
                                    <img src="https://static.wixstatic.com/media/luggage-bag-cleaning.jpg" alt="Valiz Bavul Çanta Temizleme">
                                    <div class="service-content">
                                        <h3>Valiz Bavul Çanta Temizleme</h3>
                                        <p>Seyahat çantaları, valizler ve el çantaları için özel temizlik hizmeti. Deri ve kumaş çantalar güvenli ellerde.</p>
                                        <a href="#" class="find-out-more">Detaylı Bilgi ›</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- About Section -->
                    <section class="about-section" id="about">
                        <div class="contact-info-card">
                            <div class="contact-text">
                                <h2>Hakkımızda</h2>
                                <p>Dry Alle Kuru Temizleme olarak 2000 yılından bu yana Kadıköy, Ataşehir ve İstanbul Anadolu Yakası'nın tamamında kaliteli hizmet vermekteyiz. Özel kıyafetlerinize özel bakım, halı ve koltuk yıkama, profesyonel kuru temizleme hizmetleri ile güvenin adresi olduk. Deneyimli ekibimiz, çevreci temizlik teknolojimiz ve ücretsiz kapıdan teslimat hizmetimizle farkı yaşayın.</p>
                                <a href="#contact" class="learn-more-btn">Detaylı Bilgi ›</a>
                            </div>
                            <div class="contact-image">
                                <img src="https://static.wixstatic.com/media/about-us.jpg" alt="Dry Alle Kuru Temizleme Mağaza">
                            </div>
                        </div>
                    </section>

                    <!-- Contact Info Section -->
                    <section class="contact-info-section" id="contact">
                        <div class="address-info">
                            <div class="address-item">
                                <h3>📍 Mağaza Adresimiz</h3>
                                <p>Dry Alle Kuru Temizleme<br>Sahrayıcedit Mahallesi İnönü Caddesi<br>Sinan Sokak No:3/B Kadıköy İstanbul</p>
                            </div>
                            <div class="address-item">
                                <h3>📞 İletişim</h3>
                                <p>Telefon: <a href="tel:+902163527474">0 (216) 352 74 74</a><br>WhatsApp: <a href="tel:+905433527474">0 (543) 352 74 74</a><br>Email: <a href="mailto:dryallekurutemizleme@gmail.com">dryallekurutemizleme@gmail.com</a></p>
                            </div>
                            <div class="address-item">
                                <h3>🕒 Hizmet Saatleri</h3>
                                <p>Pazartesi - Cumartesi: 09:00 - 18:00<br>Pazar: Kapalı<br>Ücretsiz kapıdan teslimat servisi</p>
                            </div>
                        </div>
                    </section>
                </main>

                <footer class="footer">
                    <div class="footer-content">
                        <div class="footer-info">
                            <p>&copy; 2025 Dry Alle Kuru Temizleme. Tüm hakları saklıdır.</p>
                        </div>
                    </div>
                </footer>
            </div>
        `;
    }

    setupEventListeners() {
        const shadow = this.shadowRoot;

        // Smooth scrolling for navigation links
        const navLinks = shadow.querySelectorAll('a[href^="#"]');
        navLinks.forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = shadow.getElementById(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Call button functionality
        const callBtn = shadow.querySelector('.call-btn');
        if (callBtn) {
            callBtn.addEventListener('click', function() {
                window.open('tel:+905433527474', '_self');
            });
        }

        // Contact button functionality
        const contactButton = shadow.querySelector('.contact-button');
        if (contactButton) {
            contactButton.addEventListener('click', function() {
                const contactSection = shadow.getElementById('contact');
                if (contactSection) {
                    contactSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        }

        // Service card hover effects with intersection observer
        const serviceCards = shadow.querySelectorAll('.service-card');
        
        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe service cards for scroll animations
        serviceCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.1}s`;
            observer.observe(card);
        });

        // Header scroll effect
        let lastScrollTop = 0;
        const header = shadow.querySelector('.header');

        window.addEventListener('scroll', function() {
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > lastScrollTop && scrollTop > 100) {
                // Scrolling down
                header.style.transform = 'translateY(-100%)';
            } else {
                // Scrolling up
                header.style.transform = 'translateY(0)';
            }
            
            // Add background to header when scrolled
            if (scrollTop > 50) {
                header.style.backgroundColor = 'rgba(0, 106, 68, 0.98)';
                header.style.backdropFilter = 'blur(10px)';
            } else {
                header.style.backgroundColor = '#006a44';
                header.style.backdropFilter = 'none';
            }
            
            lastScrollTop = scrollTop;
        });

        // Dispatch custom events for Wix integration
        this.dispatchEvent(new CustomEvent('dry-alle-loaded', {
            detail: { message: 'Dry Alle Custom Element loaded successfully' },
            bubbles: true
        }));
    }

    // Methods that can be called from Wix Velo
    scrollToSection(sectionId) {
        const section = this.shadowRoot.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    }

    updateContactInfo(phone, whatsapp, email) {
        const phoneLinks = this.shadowRoot.querySelectorAll('a[href^="tel:"]');
        const emailLinks = this.shadowRoot.querySelectorAll('a[href^="mailto:"]');
        
        phoneLinks.forEach(link => {
            if (link.textContent.includes('543')) {
                link.href = `tel:${whatsapp}`;
                link.textContent = whatsapp;
            } else {
                link.href = `tel:${phone}`;
                link.textContent = phone;
            }
        });

        emailLinks.forEach(link => {
            link.href = `mailto:${email}`;
            link.textContent = email;
        });
    }

    highlightService(serviceIndex) {
        const serviceCards = this.shadowRoot.querySelectorAll('.service-card');
        serviceCards.forEach((card, index) => {
            if (index === serviceIndex) {
                card.style.transform = 'translateY(-10px)';
                card.style.boxShadow = '0 15px 35px rgba(0,106,68,0.25)';
            } else {
                card.style.transform = 'translateY(0)';
                card.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
            }
        });
    }
}

// Register the custom element
customElements.define('dry-alle-website', DryAlleCustomElement);

// Export for use in Wix Velo
export { DryAlleCustomElement };