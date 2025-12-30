/**
 * Smart DCA Investment Tool - Main JavaScript
 * ============================================
 * Core client-side functionality
 */

// Global app namespace
const DCAApp = {
    // Configuration
    config: {
        refreshInterval: 300000, // 5 minutes
        currencyFormat: new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }),
        percentFormat: new Intl.NumberFormat('en-US', {
            style: 'percent',
            minimumFractionDigits: 1,
            maximumFractionDigits: 2
        })
    },

    // Format currency
    formatCurrency(amount) {
        return this.config.currencyFormat.format(amount);
    },

    // Format percentage
    formatPercent(value) {
        return this.config.percentFormat.format(value / 100);
    },

    // Show loading state on button
    showLoading(element) {
        element.dataset.originalText = element.innerHTML;
        element.classList.add('btn-loading');
        element.disabled = true;
    },

    // Hide loading state on button
    hideLoading(element) {
        element.classList.remove('btn-loading');
        element.innerHTML = element.dataset.originalText || element.innerHTML;
        element.disabled = false;
    },

    // Show toast notification
    showToast(message, type = 'info') {
        // Remove any existing toasts
        document.querySelectorAll('.toast').forEach(t => t.remove());
        
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            if (toast.parentNode) {
                toast.remove();
            }
        }, 3000);
    },

    // Copy text to clipboard
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            this.showToast('Copied to clipboard!', 'success');
        } catch (err) {
            this.showToast('Failed to copy', 'error');
        }
    },

    // Initialize mobile menu
    initMobileMenu() {
        const menuButton = document.querySelector('.mobile-menu-button');
        const mobileMenu = document.querySelector('.mobile-menu');
        
        if (menuButton && mobileMenu) {
            menuButton.addEventListener('click', () => {
                mobileMenu.classList.toggle('active');
                mobileMenu.classList.toggle('hidden');
                
                // Toggle hamburger to X
                const icon = menuButton.querySelector('svg');
                if (mobileMenu.classList.contains('active')) {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>';
                } else {
                    icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>';
                }
            });
            
            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!menuButton.contains(e.target) && !mobileMenu.contains(e.target)) {
                    mobileMenu.classList.remove('active');
                    mobileMenu.classList.add('hidden');
                }
            });
        }
    },

    // Highlight active nav link
    highlightActiveNav() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('nav a');
        
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPath || (currentPath === '/' && href === '/')) {
                link.classList.add('text-blue-600', 'font-semibold');
            }
        });
    },

    // API helper with error handling
    async fetchAPI(url, options = {}) {
        try {
            const response = await fetch(url, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'An error occurred');
            }
            
            return { success: true, data };
        } catch (error) {
            console.error('API Error:', error);
            return { success: false, error: error.message };
        }
    },

    // Debounce function for input handling
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Initialize app
    init() {
        console.log('Smart DCA Investment Tool initialized');
        this.initMobileMenu();
        this.highlightActiveNav();
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    DCAApp.init();
});
