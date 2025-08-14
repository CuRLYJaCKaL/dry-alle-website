// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');

    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Store Locator Functionality
    const findStoresBtn = document.querySelector('.btn-primary');
    const locateMeBtn = document.querySelector('.btn-secondary');

    findStoresBtn.addEventListener('click', function() {
        alert('Store locator feature would be implemented here. This would typically open a map or list of nearby stores.');
    });

    locateMeBtn.addEventListener('click', function() {
        if (navigator.geolocation) {
            locateMeBtn.textContent = 'Locating...';
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    locateMeBtn.textContent = 'Locate me';
                    alert(`Your location: ${position.coords.latitude}, ${position.coords.longitude}\nThis would typically show nearby Johnson Cleaners stores.`);
                },
                function(error) {
                    locateMeBtn.textContent = 'Locate me';
                    alert('Location access denied. Please enable location services or use the store finder.');
                }
            );
        } else {
            alert('Geolocation is not supported by this browser.');
        }
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Service card hover effects
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

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
    serviceCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Header scroll effect
    let lastScrollTop = 0;
    const header = document.querySelector('.header');

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
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.backgroundColor = 'white';
            header.style.backdropFilter = 'none';
        }
        
        lastScrollTop = scrollTop;
    });

    // Form validation (if forms are added later)
    function validateForm(form) {
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        let isValid = true;

        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.borderColor = '#e74c3c';
            } else {
                input.style.borderColor = '#ddd';
            }
        });

        return isValid;
    }

    // Newsletter signup (placeholder)
    function setupNewsletterSignup() {
        const newsletterForm = document.querySelector('#newsletter-form');
        if (newsletterForm) {
            newsletterForm.addEventListener('submit', function(e) {
                e.preventDefault();
                if (validateForm(this)) {
                    alert('Thank you for subscribing to our newsletter!');
                    this.reset();
                }
            });
        }
    }

    setupNewsletterSignup();

    // Loading screen (optional)
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });

    // Error handling for images
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            console.log('Image failed to load:', this.src);
        });
    });

    // Accessibility improvements
    document.querySelectorAll('button, .btn-primary, .btn-secondary, .btn-outline').forEach(button => {
        button.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });

    // Contact form handling (if contact form exists)
    const contactForms = document.querySelectorAll('form[data-type="contact"]');
    contactForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            if (validateForm(this)) {
                // Here you would typically send the form data to a server
                alert('Thank you for your message. We will get back to you soon!');
                this.reset();
            } else {
                alert('Please fill in all required fields.');
            }
        });
    });

    console.log('Johnson Cleaners website loaded successfully!');
});