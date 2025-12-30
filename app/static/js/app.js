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

    // Show loading state
    showLoading(element) {
        element.innerHTML = '<span class="spinner"></span> Loading...';
        element.disabled = true;
    },

    // Hide loading state
    hideLoading(element, originalText) {
        element.innerHTML = originalText;
        element.disabled = false;
    },

    // Show toast notification
    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
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

    // Initialize app
    init() {
        console.log('Smart DCA Investment Tool initialized');
        // Add initialization logic here
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    DCAApp.init();
});
