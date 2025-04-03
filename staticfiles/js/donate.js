document.addEventListener('DOMContentLoaded', function() {
    // Animation for donation methods
    const methods = document.querySelectorAll('.donation-method');
    
    methods.forEach(method => {
        method.addEventListener('mouseenter', function() {
            const icon = this.querySelector('.method-icon i');
            icon.style.transform = 'scale(1.1)';
        });
        
        method.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.method-icon i');
            icon.style.transform = 'scale(1)';
        });
    });

    // PayPal button enhancement
    const paypalBtn = document.querySelector('.paypal-btn');
    if (paypalBtn) {
        paypalBtn.addEventListener('click', function() {
            console.log('Initiating PayPal donation');
            // Add any tracking or confirmation here
        });
    }
});