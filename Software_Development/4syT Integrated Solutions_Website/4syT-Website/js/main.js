// ============================================
// 4syT INTEGRATED SOLUTIONS - MAIN JAVASCRIPT
// ============================================

// ============================================
// NAVIGATION & MOBILE MENU
// ============================================

class MobileMenu {
  constructor() {
    this.toggle = document.querySelector('.nav-toggle');
    this.navLinks = document.querySelector('.nav-links');
    this.init();
  }
  
  init() {
    if (this.toggle) {
      this.toggle.addEventListener('click', () => this.handleToggle());
      document.addEventListener('click', (e) => this.handleClickOutside(e));
    }
  }
  
  handleToggle() {
    this.toggle.classList.toggle('active');
    this.navLinks.classList.toggle('active');
  }
  
  handleClickOutside(e) {
    if (this.navLinks?.classList.contains('active') &&
        !e.target.closest('.nav-links') &&
        !e.target.closest('.nav-toggle')) {
      this.toggle.classList.remove('active');
      this.navLinks.classList.remove('active');
    }
  }
  
  close() {
    if (this.toggle) {
      this.toggle.classList.remove('active');
      this.navLinks.classList.remove('active');
    }
  }
}

// ============================================
// SCROLL REVEAL ANIMATIONS
// ============================================

class ScrollReveal {
  constructor() {
    this.reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .card');
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          this.observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });
    
    this.init();
  }
  
  init() {
    this.reveals.forEach(element => {
      this.observer.observe(element);
    });
  }
}

// ============================================
// HERO LOGO ANIMATION
// ============================================

class HeroAnimation {
  constructor() {
    this.init();
  }
  
  init() {
    const smallCircle = document.querySelector('.logo-circle-small');
    const lightEmanation = document.querySelector('.light-emanation');
    
    if (smallCircle) {
      // Start animations on page load
      setTimeout(() => smallCircle.classList.add('roll'), 100);
    }
  }
}

// ============================================
// SMOOTH SCROLL NAVIGATION
// ============================================

class SmoothScroll {
  constructor() {
    this.links = document.querySelectorAll('a[href^="#"]');
    this.init();
  }
  
  init() {
    this.links.forEach(link => {
      link.addEventListener('click', (e) => this.handleClick(e));
    });
  }
  
  handleClick(e) {
    const href = e.currentTarget.getAttribute('href');
    if (href === '#') return;
    
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      
      // Close mobile menu if open
      const mobileMenu = window.mobileMenu;
      if (mobileMenu) mobileMenu.close();
      
      // Scroll to target
      const navHeight = document.querySelector('nav')?.offsetHeight || 0;
      const targetPosition = target.offsetTop - navHeight;
      
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  }
}

// ============================================
// FORM HANDLING
// ============================================

class FormHandler {
  constructor() {
    this.forms = document.querySelectorAll('form');
    this.init();
  }
  
  init() {
    this.forms.forEach(form => {
      form.addEventListener('submit', (e) => this.handleSubmit(e));
    });
  }
  
  handleSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    
    // Validate form
    if (!this.validateForm(data)) {
      this.showMessage(form, 'Please fill in all required fields', 'error');
      return;
    }
    
    // Simulate form submission (replace with actual API call)
    this.submitForm(form, data);
  }
  
  validateForm(data) {
    // Add your validation logic here
    return Object.values(data).every(value => value.trim() !== '');
  }
  
  async submitForm(form, data) {
    const button = form.querySelector('button[type="submit"]');
    const originalText = button.textContent;
    
    try {
      button.disabled = true;
      button.textContent = 'Sending...';
      
      // Replace with your actual API endpoint
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
      
      if (response.ok) {
        this.showMessage(form, 'Message sent successfully!', 'success');
        form.reset();
      } else {
        this.showMessage(form, 'Failed to send message. Please try again.', 'error');
      }
    } catch (error) {
      console.error('Form submission error:', error);
      this.showMessage(form, 'An error occurred. Please try again later.', 'error');
    } finally {
      button.disabled = false;
      button.textContent = originalText;
    }
  }
  
  showMessage(form, message, type) {
    // Remove existing message
    const existingMessage = form.querySelector('.form-message');
    if (existingMessage) existingMessage.remove();
    
    // Create and show message
    const messageElement = document.createElement('div');
    messageElement.className = `form-message form-message-${type}`;
    messageElement.textContent = message;
    messageElement.style.cssText = `
      padding: 12px 16px;
      margin-bottom: 16px;
      border-radius: 6px;
      background: ${type === 'success' ? '#10b981' : '#ef4444'};
      color: white;
      font-weight: 500;
    `;
    
    form.insertBefore(messageElement, form.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => messageElement.remove(), 5000);
  }
}

// ============================================
// RAG ASSISTANT WIDGET
// ============================================

class RAGAssistant {
  constructor() {
    this.isOpen = false;
    this.widget = null;
    this.init();
  }
  
  init() {
    this.createWidget();
    this.attachEvents();
  }
  
  createWidget() {
    const widget = document.createElement('div');
    widget.className = 'rag-widget';
    widget.innerHTML = `
      <div class="rag-widget-toggle">
        <button class="rag-toggle-btn" aria-label="Open AI Assistant">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/>
            <path d="M12 7v5m0 3h.01"/>
          </svg>
        </button>
      </div>
      
      <div class="rag-widget-panel" style="display: none;">
        <div class="rag-widget-header">
          <h4>4syT AI Assistant</h4>
          <button class="rag-close-btn" aria-label="Close AI Assistant">×</button>
        </div>
        <div class="rag-widget-messages"></div>
        <div class="rag-widget-input">
          <input type="text" placeholder="Ask me anything..." class="rag-input"/>
          <button class="rag-send-btn">Send</button>
        </div>
      </div>
    `;
    
    this.widget = widget;
    document.body.appendChild(widget);
    this.addStyles();
  }
  
  attachEvents() {
    const toggleBtn = this.widget.querySelector('.rag-toggle-btn');
    const closeBtn = this.widget.querySelector('.rag-close-btn');
    const sendBtn = this.widget.querySelector('.rag-send-btn');
    const input = this.widget.querySelector('.rag-input');
    
    toggleBtn?.addEventListener('click', () => this.toggleWidget());
    closeBtn?.addEventListener('click', () => this.closeWidget());
    sendBtn?.addEventListener('click', () => this.sendMessage());
    input?.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.sendMessage();
    });
  }
  
  toggleWidget() {
    this.isOpen ? this.closeWidget() : this.openWidget();
  }
  
  openWidget() {
    const panel = this.widget.querySelector('.rag-widget-panel');
    panel.style.display = 'flex';
    this.isOpen = true;
    this.widget.querySelector('.rag-input').focus();
  }
  
  closeWidget() {
    const panel = this.widget.querySelector('.rag-widget-panel');
    panel.style.display = 'none';
    this.isOpen = false;
  }
  
  sendMessage() {
    const input = this.widget.querySelector('.rag-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Display user message
    this.displayMessage(message, 'user');
    input.value = '';
    
    // Simulate API call to RAG backend
    // Replace with your actual RAG API endpoint
    this.getRAGResponse(message);
  }
  
  displayMessage(message, sender) {
    const messagesContainer = this.widget.querySelector('.rag-widget-messages');
    const messageEl = document.createElement('div');
    messageEl.className = `rag-message rag-message-${sender}`;
    messageEl.textContent = message;
    messageEl.style.cssText = `
      margin-bottom: 12px;
      padding: 8px 12px;
      border-radius: 6px;
      max-width: 80%;
      word-wrap: break-word;
      background: ${sender === 'user' ? '#0066cc' : '#e5e5e5'};
      color: ${sender === 'user' ? 'white' : '#1a1a1a'};
      text-align: ${sender === 'user' ? 'right' : 'left'};
      margin-left: ${sender === 'user' ? 'auto' : '0'};
    `;
    messagesContainer.appendChild(messageEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  
  async getRAGResponse(query) {
    try {
      // Replace with your actual RAG API endpoint
      const response = await fetch('/api/rag', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });
      
      if (response.ok) {
        const data = await response.json();
        this.displayMessage(data.answer || 'I couldn\'t find an answer to that question.', 'assistant');
      }
    } catch (error) {
      console.error('RAG API error:', error);
      this.displayMessage('Sorry, I encountered an error. Please try again later.', 'assistant');
    }
  }
  
  addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .rag-widget {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 999;
        font-family: var(--font-family-primary, sans-serif);
      }
      
      .rag-toggle-btn {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: var(--color-accent-blue, #0066cc);
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        font-size: 24px;
      }
      
      .rag-toggle-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 16px rgba(0, 102, 204, 0.4);
      }
      
      .rag-widget-panel {
        position: absolute;
        bottom: 80px;
        right: 0;
        width: 360px;
        height: 500px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        display: flex;
        flex-direction: column;
        overflow: hidden;
      }
      
      .rag-widget-header {
        background: var(--color-primary-dark, #1a1a1a);
        color: white;
        padding: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      
      .rag-widget-header h4 {
        margin: 0;
        font-size: 16px;
      }
      
      .rag-close-btn {
        background: none;
        border: none;
        color: white;
        cursor: pointer;
        font-size: 24px;
      }
      
      .rag-widget-messages {
        flex: 1;
        overflow-y: auto;
        padding: 16px;
        display: flex;
        flex-direction: column;
      }
      
      .rag-widget-input {
        border-top: 1px solid #e0e0e0;
        padding: 12px;
        display: flex;
        gap: 8px;
      }
      
      .rag-input {
        flex: 1;
        border: 1px solid #e0e0e0;
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 14px;
      }
      
      .rag-send-btn {
        background: var(--color-accent-blue, #0066cc);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        cursor: pointer;
        font-weight: 600;
      }
      
      @media (max-width: 480px) {
        .rag-widget {
          bottom: 20px;
          right: 20px;
        }
        
        .rag-widget-panel {
          width: 100vw;
          height: 400px;
          bottom: auto;
          top: auto;
          left: 0;
          right: 0;
          border-radius: 12px 12px 0 0;
        }
      }
    `;
    document.head.appendChild(style);
  }
}

// ============================================
// INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', () => {
  // Initialize components
  window.mobileMenu = new MobileMenu();
  new ScrollReveal();
  new HeroAnimation();
  new SmoothScroll();
  new FormHandler();
  new RAGAssistant();
  
  console.log('4syT Website initialized successfully');
});
