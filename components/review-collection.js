// Automated Review Collection System
class ReviewCollectionSystem {
    constructor() {
        this.googleReviewUrl = "https://g.page/r/YOUR_GOOGLE_MY_BUSINESS_ID/review"; // GMB ID'si eklenecek
        this.reviews = [];
        this.init();
    }

    init() {
        this.createReviewPrompt();
        this.setupTriggers();
        this.displayReviews();
        this.addReviewSchema();
    }

    createReviewPrompt() {
        const reviewModal = document.createElement('div');
        reviewModal.id = 'review-modal';
        reviewModal.className = 'review-modal hidden';
        reviewModal.innerHTML = `
            <div class="review-modal-content">
                <div class="review-header">
                    <h3>Hizmetimizden Memnun Kaldınız mı?</h3>
                    <button class="close-review" onclick="ReviewCollection.closeModal()">&times;</button>
                </div>
                <div class="review-body">
                    <p>Deneyiminizi paylaşarak diğer müşterilere yardımcı olun!</p>
                    <div class="star-rating" id="star-rating">
                        ${this.createStarRating()}
                    </div>
                    <div class="review-actions">
                        <button class="review-btn google-review" onclick="ReviewCollection.goToGoogle()">
                            <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIyLjU2IDEyLjI1QzIyLjU2IDExLjQ3IDIyLjQ5IDEwLjcyIDIyLjM2IDEwSDE0VjE0LjI1SDIyLjU2VjEyLjI1WiIgZmlsbD0iIzQyODVGNCIvPgo8L3N2Zz4K" alt="Google">
                            Google'da Değerlendir
                        </button>
                        <button class="review-btn whatsapp-review" onclick="ReviewCollection.sendWhatsApp()">
                            <svg width="20" height="20" fill="#25D366" viewBox="0 0 24 24">
                                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0020.885 3.488"/>
                            </svg>
                            WhatsApp ile Geri Bildirim
                        </button>
                    </div>
                </div>
            </div>
        `;
        document.body.appendChild(reviewModal);
    }

    createStarRating() {
        let stars = '';
        for (let i = 1; i <= 5; i++) {
            stars += `<span class="star" data-rating="${i}">⭐</span>`;
        }
        return stars;
    }

    setupTriggers() {
        // Time-based trigger (30 seconds after page load)
        setTimeout(() => {
            this.showReviewPrompt();
        }, 30000);

        // Scroll-based trigger (80% of page)
        let hasTriggered = false;
        window.addEventListener('scroll', () => {
            if (hasTriggered) return;
            
            const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            if (scrollPercent > 80) {
                hasTriggered = true;
                setTimeout(() => this.showReviewPrompt(), 2000);
            }
        });

        // Exit intent trigger
        document.addEventListener('mouseleave', () => {
            if (!hasTriggered) {
                hasTriggered = true;
                this.showReviewPrompt();
            }
        });

        // Star rating interaction
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('star')) {
                const rating = parseInt(e.target.dataset.rating);
                this.handleStarRating(rating);
            }
        });
    }

    showReviewPrompt() {
        // Check if user has already left a review (localStorage)
        const hasReviewed = localStorage.getItem('dryalle_reviewed');
        const lastPrompt = localStorage.getItem('dryalle_review_prompt');
        const now = new Date().getTime();
        
        // Don't show if reviewed or prompted within last 7 days
        if (hasReviewed || (lastPrompt && now - parseInt(lastPrompt) < 7 * 24 * 60 * 60 * 1000)) {
            return;
        }

        const modal = document.getElementById('review-modal');
        if (modal) {
            modal.classList.remove('hidden');
            localStorage.setItem('dryalle_review_prompt', now.toString());
            
            // Analytics tracking
            if (typeof gtag !== 'undefined') {
                gtag('event', 'review_prompt_shown', {
                    'event_category': 'Reviews',
                    'event_label': window.location.pathname
                });
            }
        }
    }

    handleStarRating(rating) {
        const stars = document.querySelectorAll('.star');
        stars.forEach((star, index) => {
            star.style.opacity = index < rating ? '1' : '0.3';
        });

        if (rating >= 4) {
            // Good rating - direct to Google
            setTimeout(() => {
                document.querySelector('.google-review').style.display = 'block';
                document.querySelector('.whatsapp-review').style.display = 'none';
            }, 500);
        } else {
            // Lower rating - direct to private feedback
            setTimeout(() => {
                document.querySelector('.google-review').style.display = 'none';
                document.querySelector('.whatsapp-review').style.display = 'block';
            }, 500);
        }

        // Track rating
        if (typeof gtag !== 'undefined') {
            gtag('event', 'star_rating_given', {
                'event_category': 'Reviews',
                'event_label': `${rating}_stars`,
                'value': rating
            });
        }
    }

    goToGoogle() {
        localStorage.setItem('dryalle_reviewed', 'true');
        window.open(this.googleReviewUrl, '_blank');
        this.closeModal();
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'google_review_clicked', {
                'event_category': 'Reviews',
                'event_label': 'positive_redirect'
            });
        }
    }

    sendWhatsApp() {
        const message = "Merhaba, hizmetiniz hakkında geri bildirimde bulunmak istiyorum.";
        const phoneNumber = "905433527474";
        const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
        
        localStorage.setItem('dryalle_reviewed', 'true');
        window.open(whatsappUrl, '_blank');
        this.closeModal();
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'whatsapp_feedback_clicked', {
                'event_category': 'Reviews',
                'event_label': 'private_feedback'
            });
        }
    }

    closeModal() {
        const modal = document.getElementById('review-modal');
        if (modal) {
            modal.classList.add('hidden');
        }
    }

    displayReviews() {
        // Sample reviews for display (you can fetch real reviews from Google My Business API)
        this.reviews = [
            {
                name: "Ayşe Y.",
                rating: 5,
                text: "İçerenköy'de aldığım halı yıkama hizmeti mükemmeldi. Persian halımı çok özenle temizlediler.",
                date: "2024-12-15"
            },
            {
                name: "Mehmet K.",
                rating: 5,
                text: "Suadiye'deki evimde koltuk yıkama yaptırdım. Sonuç harika, kesinlikle tavsiye ederim.",
                date: "2024-12-10"
            },
            {
                name: "Zeynep M.",
                rating: 5,
                text: "Erenköy'de antika koltuk temizliği yaptırdım. Çok profesyonel ve güvenilir hizmet.",
                date: "2024-12-08"
            }
        ];

        this.createReviewDisplay();
    }

    createReviewDisplay() {
        const reviewsContainer = document.querySelector('.customer-testimonials-container');
        if (!reviewsContainer) return;

        const reviewsHTML = this.reviews.map(review => `
            <div class="review-card">
                <div class="review-header">
                    <h4>${review.name}</h4>
                    <div class="review-stars">
                        ${'⭐'.repeat(review.rating)}
                    </div>
                </div>
                <p class="review-text">${review.text}</p>
                <span class="review-date">${new Date(review.date).toLocaleDateString('tr-TR')}</span>
            </div>
        `).join('');

        reviewsContainer.innerHTML = `
            <section class="reviews-section">
                <h2>Müşteri Yorumları</h2>
                <div class="reviews-grid">
                    ${reviewsHTML}
                </div>
            </section>
        `;
    }

    addReviewSchema() {
        const reviewSchema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": "Dry Alle Kuru Temizleme",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "reviewCount": "127"
            },
            "review": this.reviews.map(review => ({
                "@type": "Review",
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": review.rating
                },
                "author": {
                    "@type": "Person",
                    "name": review.name
                },
                "reviewBody": review.text,
                "datePublished": review.date
            }))
        };

        const script = document.createElement('script');
        script.type = 'application/ld+json';
        script.textContent = JSON.stringify(reviewSchema);
        document.head.appendChild(script);
    }
}

// Global instance
const ReviewCollection = new ReviewCollectionSystem();

// Export for module systems
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ReviewCollectionSystem;
}