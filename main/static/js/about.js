document.addEventListener('DOMContentLoaded', function() {
    console.log('About page loaded');
    
    // Animate sections on scroll
    const sections = document.querySelectorAll('.about-section');
    
    function checkVisibility() {
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (sectionTop < windowHeight * 0.75) {
                section.style.opacity = '1';
                section.style.transform = 'translateY(0)';
            }
        });
    }
    
    // Initialize
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    });
    
    // Check on load and scroll
    checkVisibility();
    window.addEventListener('scroll', checkVisibility);
    
    // Highlight current section in navigation
    const navLinks = document.querySelectorAll('.nav-item');
    navLinks.forEach(link => {
        if (link.classList.contains('active')) {
            link.style.fontWeight = '600';
            link.style.color = '#2c7be5';
        }
    });
});