// Component Loader
function loadComponent(componentName, targetSelector) {
    return fetch(`/components/${componentName}.html`)
        .then(response => response.text())
        .then(html => {
            const targetElement = document.querySelector(targetSelector);
            if (targetElement) {
                targetElement.innerHTML = html;
            }
        })
        .catch(error => {
            console.error(`Component ${componentName} yüklenemedi:`, error);
        });
}

// Hızlı İletişim component'ini yükle
function loadQuickContact() {
    loadComponent('quick-contact', '.quick-contact-container');
}

// Sayfa yüklendiğinde çalışacak
document.addEventListener('DOMContentLoaded', function() {
    // Eğer quick-contact-container varsa component'i yükle
    if (document.querySelector('.quick-contact-container')) {
        loadQuickContact();
    }
});