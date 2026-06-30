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
    this.hasGreeted = false;
    
    // Local Knowledge Base for Client-Side Fallback (inspired by ai-agent-app)
    this.companyKB = {
      welcome: {
        greeting: "Hello! Welcome to **4syT Integrated Solutions**. I am your interactive AI assistant. \n\nHow can I help you today? You can ask me about our **Core Services** (Cloud, Workplace, AI), view our **Projects Portfolio**, learn about our **Work Process**, or get details on **Consultation & Booking**.",
        options: [
          { text: "💼 Our Services", query: "What services do you offer?" },
          { text: "🚀 Featured Projects", query: "Show me your portfolio projects" },
          { text: "🔄 Our Process", query: "What is your work process?" },
          { text: "📅 Book a Call", query: "How do I book a consultation?" }
        ]
      },
      company: {
        name: "4syT Integrated Solutions",
        about: "Founded on the principles of innovation and excellence, **4syT Integrated Solutions** is a forward-thinking technology partner. We help organizations navigate and thrive in the digital age by aligning robust engineering standards with strategic business growth.",
        mission: "To empower businesses through cutting-edge technology solutions that drive growth, efficiency, and digital transformation.",
        vision: "To be the trusted partner of choice for enterprises seeking to harness the full potential of cloud, modern workplace, and AI technologies.",
        stats: "We have delivered **150+ successful projects** for **50+ enterprise clients** with an expert team of **100+ members** globally."
      },
      services: {
        overview: "We deliver enterprise-grade technology solutions across three core pillars:\n\n1. **Cloud Engineering**: Scalable, secure multi-cloud architectures, migrations, and infrastructure automation.\n2. **Modern Workplace Engineering**: Agile employee environments, secure collaboration, identity governance, and device compliance.\n3. **AI Solutions**: Custom machine learning models, intelligent automation (RPA), semantic indexing, and Copilot readiness pipelines.",
        cloud: {
          name: "Cloud Engineering",
          desc: "Architect, deploy, and optimize scalable cloud infrastructure. We specialize in multi-cloud strategies, migration planning, and infrastructure automation to accelerate your digital transformation.",
          technologies: ["AWS", "Microsoft Azure", "Google Cloud Platform", "Terraform", "Docker", "Kubernetes", "GitHub Actions"],
          timeline: "4 to 12 weeks depending on complexity.",
          pricing: "Project-based pricing or dedicated sprint team retainers."
        },
        workplace: {
          name: "Modern Workplace Engineering",
          desc: "Create productive, secure, and agile work environments. We design modern workplace solutions that empower employees, enhance collaboration, and drive organizational efficiency.",
          technologies: ["Microsoft 365", "Microsoft Entra ID", "Microsoft Intune", "Microsoft Defender", "Power Automate", "Power BI"],
          timeline: "3 to 8 weeks depending on tenant size.",
          pricing: "Per-user configuration setup or customized transition milestones."
        },
        ai: {
          name: "AI Solutions",
          desc: "Unlock the power of artificial intelligence. From machine learning models to intelligent automation, we build AI solutions that drive innovation and create competitive advantages.",
          technologies: ["OpenAI API", "LangChain / LangGraph", "Python", "FastAPI", "ZenML", "MLflow", "Scikit-Learn"],
          timeline: "6 to 16 weeks depending on data ready state.",
          pricing: "Value-based project pricing or technical consulting retainers."
        }
      },
      projects: {
        list: "Here are some of our featured case studies (ask about a specific one for more details):\n\n* **Enterprise Cloud Migration** (Fortune 500 Manufacturer)\n* **Modern Workplace Transformation** (Global Financial Services Firm)\n* **AI-Powered Analytics Platform** (Healthcare Tech Provider)\n* **Intelligent Process Automation** (Insurance Industry Leader)",
        migration: {
          name: "Enterprise Cloud Migration",
          client: "Fortune 500 Manufacturing Company",
          desc: "Successfully migrated 200+ applications to a secure multi-cloud environment, reducing infrastructure costs by 40% and improving deployment speeds via Terraform.",
          tags: ["Cloud Engineering", "Multi-Cloud Strategy", "Terraform", "AWS", "Azure"]
        },
        workplace: {
          name: "Modern Workplace Transformation",
          client: "Global Financial Services Firm",
          desc: "Implemented a comprehensive modern workplace solution enabling hybrid work for 5,000+ employees with enhanced security, Microsoft Intune compliance, and Entra ID governance.",
          tags: ["Workplace", "Hybrid Work", "M365", "Intune", "Entra ID"]
        },
        analytics: {
          name: "AI-Powered Analytics Platform",
          client: "Healthcare Technology Provider",
          desc: "Built an intelligent analytics platform using machine learning to process 10M+ data points daily, enabling predictive insights and improving decision-making pipelines.",
          tags: ["AI/ML", "Analytics", "Python", "Scikit-Learn", "FastAPI"]
        },
        automation: {
          name: "Intelligent Process Automation",
          client: "Insurance Industry Leader",
          desc: "Deployed Robotic Process Automation (RPA) and AI integrations automating 70% of manual claims processing, reducing verification time by 60% with 99.9% accuracy.",
          tags: ["Automation", "RPA", "AI Solutions", "Python", "Power Automate"]
        }
      },
      process: "We follow a disciplined, 8-step delivery methodology to ensure project success:\n\n1. **Consultation**: Initial discovery to align on goals and requirements.\n2. **Assessment**: Auditing your current tenant configurations, data schemas, or cloud environments.\n3. **Design**: Creating a tailored architecture baseline and blueprint.\n4. **Prototyping**: Developing lightweight POCs to validate feasibility.\n5. **Implementation**: High-fidelity execution, coding, and integration sprints.\n6. **Testing**: Comprehensive performance, security, and accessibility checks.\n7. **Deployment**: Production rollout using zero-downtime processes.\n8. **Support**: Post-launch optimizations, telemetry analytics, and proactive monitoring.",
      contact: {
        info: "You can reach out to the **4syT Team** through any of these channels:\n\n* ✉️ **Email**: [hello@4syt.com](mailto:hello@4syt.com)\n* 📞 **Phone**: [+1 (234) 567-890](tel:+1234567890)\n* 📅 **Consultation**: Use the Calendly button in the contact sidebar or submit the contact form.",
        booking: "To schedule a direct **30-minute technical consultation** with our principal engineers, click the 'Open Calendly' button on this page, or fill out the 'Let's Work Together' contact form below."
      }
    };

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
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
        </button>
      </div>
      
      <div class="rag-widget-panel" style="display: none;">
        <div class="rag-widget-header">
          <div class="rag-header-info">
            <div class="rag-avatar-dot"></div>
            <h4>4syT Smart Assistant</h4>
          </div>
          <button class="rag-close-btn" aria-label="Close AI Assistant">×</button>
        </div>
        <div class="rag-widget-messages"></div>
        <div class="rag-widget-chips"></div>
        <div class="rag-widget-input">
          <input type="text" placeholder="Ask me about services, projects, or booking..." class="rag-input"/>
          <button class="rag-send-btn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
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
    
    if (!this.hasGreeted) {
      this.triggerGreeting();
    } else {
      this.widget.querySelector('.rag-input').focus();
    }
  }
  
  closeWidget() {
    const panel = this.widget.querySelector('.rag-widget-panel');
    panel.style.display = 'none';
    this.isOpen = false;
  }
  
  triggerGreeting() {
    this.hasGreeted = true;
    this.showTypingIndicator();
    setTimeout(() => {
      this.hideTypingIndicator();
      this.displayMessage(this.companyKB.welcome.greeting, 'assistant');
      this.displaySuggestionChips(this.companyKB.welcome.options);
    }, 800);
  }
  
  sendMessage(customText = null) {
    const input = this.widget.querySelector('.rag-input');
    const message = customText ? customText.trim() : input.value.trim();
    
    if (!message) return;
    
    // Display user message
    this.displayMessage(message, 'user');
    if (!customText) input.value = '';
    
    // Clear existing chips
    this.clearSuggestionChips();
    
    // Display typing indicator before processing response
    this.showTypingIndicator();
    
    // Trigger response call
    this.getRAGResponse(message);
  }
  
  displayMessage(message, sender) {
    const messagesContainer = this.widget.querySelector('.rag-widget-messages');
    const messageEl = document.createElement('div');
    messageEl.className = `rag-message rag-message-${sender}`;
    
    if (sender === 'assistant') {
      messageEl.innerHTML = this.formatMarkdown(message);
    } else {
      messageEl.textContent = message;
    }
    
    // Styles applied directly
    messageEl.style.cssText = `
      margin-bottom: 12px;
      padding: 10px 14px;
      border-radius: 8px;
      max-width: 85%;
      word-wrap: break-word;
      line-height: 1.5;
      font-size: 0.92rem;
      animation: fadeIn 0.3s ease;
      background: ${sender === 'user' ? '#0066cc' : '#f0f0f0'};
      color: ${sender === 'user' ? 'white' : '#1a1a1a'};
      align-self: ${sender === 'user' ? 'flex-end' : 'flex-start'};
      border-bottom-right-radius: ${sender === 'user' ? '2px' : '8px'};
      border-bottom-left-radius: ${sender === 'assistant' ? '2px' : '8px'};
    `;
    messagesContainer.appendChild(messageEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  
  showTypingIndicator() {
    this.hideTypingIndicator(); // Ensure no duplicates
    const messagesContainer = this.widget.querySelector('.rag-widget-messages');
    const indicatorEl = document.createElement('div');
    indicatorEl.className = 'rag-typing-indicator';
    indicatorEl.innerHTML = `
      <span></span>
      <span></span>
      <span></span>
    `;
    indicatorEl.style.cssText = `
      display: flex;
      gap: 4px;
      padding: 12px 16px;
      background: #f0f0f0;
      border-radius: 8px;
      align-self: flex-start;
      margin-bottom: 12px;
      width: fit-content;
      animation: fadeIn 0.2s ease;
    `;
    
    // Style keyframes for dots are added inside addStyles()
    messagesContainer.appendChild(indicatorEl);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }
  
  hideTypingIndicator() {
    const indicator = this.widget.querySelector('.rag-typing-indicator');
    if (indicator) indicator.remove();
  }
  
  displaySuggestionChips(options) {
    const chipsContainer = this.widget.querySelector('.rag-widget-chips');
    chipsContainer.innerHTML = '';
    
    options.forEach(option => {
      const chip = document.createElement('button');
      chip.className = 'rag-chip';
      chip.textContent = option.text;
      chip.style.cssText = `
        background: transparent;
        border: 1px solid #0066cc;
        color: #0066cc;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        cursor: pointer;
        font-weight: 500;
        transition: all 0.2s ease;
        white-space: nowrap;
      `;
      
      chip.addEventListener('mouseenter', () => {
        chip.style.background = 'rgba(0, 102, 204, 0.08)';
      });
      chip.addEventListener('mouseleave', () => {
        chip.style.background = 'transparent';
      });
      
      chip.addEventListener('click', () => {
        this.sendMessage(option.query);
      });
      
      chipsContainer.appendChild(chip);
    });
    
    chipsContainer.style.cssText = `
      display: flex;
      gap: 8px;
      padding: 8px 16px;
      overflow-x: auto;
      border-top: 1px solid #f0f0f0;
      scrollbar-width: none;
    `;
  }
  
  clearSuggestionChips() {
    const chipsContainer = this.widget.querySelector('.rag-widget-chips');
    chipsContainer.innerHTML = '';
    chipsContainer.style.padding = '0';
  }
  
  async getRAGResponse(query) {
    try {
      const response = await fetch('/api/rag', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });
      
      if (response.ok) {
        const data = await response.json();
        this.hideTypingIndicator();
        this.displayMessage(data.answer || 'I couldn\'t find an answer to that question.', 'assistant');
      } else {
        throw new Error('API server returned error code');
      }
    } catch (error) {
      // Local Retrieval Engine Fallback (Zero-dependency RAG)
      setTimeout(() => {
        this.hideTypingIndicator();
        const localAnswer = this.localRetrieve(query);
        this.displayMessage(localAnswer.text, 'assistant');
        if (localAnswer.chips) {
          this.displaySuggestionChips(localAnswer.chips);
        }
      }, 700);
    }
  }
  
  localRetrieve(query) {
    const q = query.toLowerCase();
    
    // Greeting
    if (q.includes('hello') || q.includes('hi') || q.includes('hey') || q.includes('welcome') || q.includes('greeter')) {
      return {
        text: "Hi there! I hope you're having a great day. How can **4syT Integrated Solutions** assist you with your project needs today?",
        chips: [
          { text: "💼 View Services", query: "What services do you offer?" },
          { text: "📅 Contact Info", query: "How can I contact your team?" }
        ]
      };
    }
    
    // Specific Cloud Service
    if (q.includes('cloud') || q.includes('aws') || q.includes('azure') || q.includes('gcp') || q.includes('terraform') || q.includes('kubernetes')) {
      const s = this.companyKB.services.cloud;
      return {
        text: `### **${s.name}**\n\n${s.desc}\n\n* **Timeline**: ${s.timeline}\n* **Pricing Model**: ${s.pricing}\n* **Key Stack**: ${s.technologies.join(', ')}\n\nWould you like to check out a cloud project case study?`,
        chips: [
          { text: "📂 Cloud Case Study", query: "Tell me about the Enterprise Cloud Migration project" },
          { text: "⚙️ Other Services", query: "What core services do you offer?" }
        ]
      };
    }
    
    // Specific Workplace Service
    if (q.includes('workplace') || q.includes('m365') || q.includes('intune') || q.includes('entra') || q.includes('office 365') || q.includes('microsoft')) {
      const s = this.companyKB.services.workplace;
      return {
        text: `### **${s.name}**\n\n${s.desc}\n\n* **Timeline**: ${s.timeline}\n* **Pricing Model**: ${s.pricing}\n* **Key Stack**: ${s.technologies.join(', ')}\n\nWould you like to learn about a workplace transformation case study?`,
        chips: [
          { text: "📂 Workplace Case Study", query: "Tell me about the Modern Workplace Transformation project" },
          { text: "⚙️ Other Services", query: "What core services do you offer?" }
        ]
      };
    }
    
    // Specific AI Service
    if (q.includes('ai') || q.includes('artificial') || q.includes('intelligence') || q.includes('machine learning') || q.includes('ml') || q.includes('openai') || q.includes('llm') || q.includes('copilot')) {
      const s = this.companyKB.services.ai;
      return {
        text: `### **${s.name}**\n\n${s.desc}\n\n* **Timeline**: ${s.timeline}\n* **Pricing Model**: ${s.pricing}\n* **Key Stack**: ${s.technologies.join(', ')}\n\nWe build intelligent agents, RAG pipelines, and assess organization readiness for Copilot. Inquire about our case studies below:`,
        chips: [
          { text: "📂 AI Analytics Case Study", query: "Tell me about the AI-Powered Analytics Platform" },
          { text: "📂 Process Automation Case Study", query: "Tell me about the Process Automation case study" }
        ]
      };
    }
    
    // Services general
    if (q.includes('service') || q.includes('offer') || q.includes('capabilities') || q.includes('solutions')) {
      return {
        text: `### **Our Core Solutions**\n\n${this.companyKB.services.overview}\n\nAsk about any specific service to get details on pricing, timelines, and tools.`,
        chips: [
          { text: "☁️ Cloud Engineering", query: "Tell me about Cloud Engineering services" },
          { text: "🏢 Modern Workplace", query: "Tell me about Modern Workplace services" },
          { text: "🤖 AI Solutions", query: "Tell me about AI Solutions" }
        ]
      };
    }
    
    // Case Studies / Projects
    if (q.includes('project') || q.includes('portfolio') || q.includes('work') || q.includes('case study') || q.includes('client') || q.includes('success')) {
      // Specific project checks
      if (q.includes('migration') || q.includes('manufacturing')) {
        const p = this.companyKB.projects.migration;
        return {
          text: `### **Case Study: ${p.name}**\n\n* **Client**: ${p.client}\n* **Overview**: ${p.desc}\n* **Core Stack**: ${p.tags.join(', ')}`,
          chips: [{ text: "📅 Inquire About Migration", query: "How do I book a consultation?" }, { text: "📂 View Other Projects", query: "Show me all projects" }]
        };
      }
      if (q.includes('transformation') || q.includes('hybrid') || q.includes('financial')) {
        const p = this.companyKB.projects.workplace;
        return {
          text: `### **Case Study: ${p.name}**\n\n* **Client**: ${p.client}\n* **Overview**: ${p.desc}\n* **Core Stack**: ${p.tags.join(', ')}`,
          chips: [{ text: "📅 Inquire About Workplace Setup", query: "How do I book a consultation?" }, { text: "📂 View Other Projects", query: "Show me all projects" }]
        };
      }
      if (q.includes('analytics') || q.includes('healthcare') || q.includes('predictive')) {
        const p = this.companyKB.projects.analytics;
        return {
          text: `### **Case Study: ${p.name}**\n\n* **Client**: ${p.client}\n* **Overview**: ${p.desc}\n* **Core Stack**: ${p.tags.join(', ')}`,
          chips: [{ text: "📅 Inquire About Analytics", query: "How do I book a consultation?" }, { text: "📂 View Other Projects", query: "Show me all projects" }]
        };
      }
      if (q.includes('automation') || q.includes('rpa') || q.includes('insurance')) {
        const p = this.companyKB.projects.automation;
        return {
          text: `### **Case Study: ${p.name}**\n\n* **Client**: ${p.client}\n* **Overview**: ${p.desc}\n* **Core Stack**: ${p.tags.join(', ')}`,
          chips: [{ text: "📅 Inquire About Automation", query: "How do I book a consultation?" }, { text: "📂 View Other Projects", query: "Show me all projects" }]
        };
      }
      
      // General list
      return {
        text: `### **Featured Work & Case Studies**\n\n${this.companyKB.projects.list}\n\nAsk about any specific case study to learn details on implementation outcomes.`,
        chips: [
          { text: "☁️ Cloud Migration", query: "Tell me about the Enterprise Cloud Migration project" },
          { text: "🏢 Workplace Setup", query: "Tell me about the Modern Workplace Transformation project" },
          { text: "🤖 Healthcare Analytics", query: "Tell me about the AI-Powered Analytics Platform" }
        ]
      };
    }
    
    // Process
    if (q.includes('process') || q.includes('how do you work') || q.includes('steps') || q.includes('methodology') || q.includes('workflow')) {
      return {
        text: `### **Our Delivery Methodology**\n\n${this.companyKB.process}\n\nWe run initial consultations and prototypes to validate ideas before scaling production deployments.`,
        chips: [
          { text: "📅 Book Consultation", query: "How do I book a consultation?" },
          { text: "💼 View Services", query: "What services do you offer?" }
        ]
      };
    }
    
    // Contact
    if (q.includes('contact') || q.includes('book') || q.includes('call') || q.includes('email') || q.includes('phone') || q.includes('consultation') || q.includes('calendly') || q.includes('hire')) {
      return {
        text: `### **Contact Us & Booking**\n\n${this.companyKB.contact.info}\n\n${this.companyKB.contact.booking}`,
        chips: [
          { text: "✉️ Send Email", query: "How can I contact your team?" },
          { text: "💼 Our Services", query: "What services do you offer?" }
        ]
      };
    }
    
    // Pricing
    if (q.includes('pricing') || q.includes('cost') || q.includes('price') || q.includes('how much') || q.includes('rate') || q.includes('fee')) {
      return {
        text: `### **Pricing & Engagement Models**\n\n* **Cloud Engineering**: Project-based blueprints or sprint team retainers.\n* **Modern Workplace Engineering**: Setup milestones or per-user configurations.\n* **AI Solutions**: Value-based deliverables or technical consulting retainers.\n\nWe provide tailored quotes depending on requirements. Get in touch to schedule a free 30-minute scoping call.`,
        chips: [
          { text: "📅 Schedule Scoping Call", query: "How do I book a consultation?" },
          { text: "🔄 Our Process", query: "What is your work process?" }
        ]
      };
    }
    
    // About / Mission / Vision
    if (q.includes('about') || q.includes('mission') || q.includes('vision') || q.includes('who are you') || q.includes('team') || q.includes('stats')) {
      return {
        text: `### **About 4syT Integrated Solutions**\n\n${this.companyKB.company.about}\n\n* **Our Mission**: ${this.companyKB.company.mission}\n* **Our Vision**: ${this.companyKB.company.vision}\n* **Stats**: ${this.companyKB.company.stats}`,
        chips: [
          { text: "💼 View Our Services", query: "What services do you offer?" },
          { text: "🚀 Explore Case Studies", query: "Show me all projects" }
        ]
      };
    }
    
    // Fallback
    return {
      text: "I want to make sure you get the right info! I can explain our **Services** (Cloud, Workplace, AI), show **Projects** (Migration, Intune Setup, AI Analytics), explain our **Delivery Process**, or give you details on **Booking a Scoping Call**. \n\nWhat can I clarify for you?",
      chips: [
        { text: "💼 Core Services", query: "What services do you offer?" },
        { text: "🚀 Portfolio Case Studies", query: "Show me all projects" },
        { text: "📅 Contact Info", query: "How can I contact your team?" }
      ]
    };
  }
  
  formatMarkdown(text) {
    if (!text) return '';
    // Escape HTML to prevent basic XSS (leaving markdown formatting intact)
    let html = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    
    // Headers (### Header)
    html = html.replace(/^### (.*$)/gim, '<h5 style="margin-top:12px;margin-bottom:6px;font-weight:700;font-size:0.95rem;">$1</h5>');
    html = html.replace(/^## (.*$)/gim, '<h4 style="margin-top:14px;margin-bottom:8px;font-weight:700;font-size:1.05rem;color:#0066cc;">$1</h4>');
    html = html.replace(/^# (.*$)/gim, '<h3 style="margin-top:16px;margin-bottom:10px;font-weight:700;font-size:1.15rem;color:#0066cc;">$1</h3>');
    
    // Bold (**text**)
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong style="font-weight:700;">$1</strong>');
    
    // Markdown Links [label](url)
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" style="color:#0066cc;text-decoration:underline;font-weight:500;">$1</a>');
    
    // Bullet lists (* list item or - list item)
    html = html.replace(/^\s*[-*]\s+(.*$)/gim, '<li style="margin-left:14px;margin-bottom:4px;">$1</li>');
    
    // Newlines to breaks
    html = html.replace(/\n/g, '<br>');
    
    return html;
  }
  
  addStyles() {
    const style = document.createElement('style');
    style.textContent = `
      .rag-widget {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 999;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }
      
      .rag-toggle-btn {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: #1a1a1a;
        color: #d4d4d4;
        border: 1px solid rgba(212, 212, 212, 0.3);
        cursor: pointer;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-size: 24px;
      }
      
      .rag-toggle-btn:hover {
        transform: translateY(-3px) scale(1.05);
        border-color: #0066cc;
        color: white;
        box-shadow: 0 6px 20px rgba(0, 102, 204, 0.3);
      }
      
      .rag-widget-panel {
        position: absolute;
        bottom: 75px;
        right: 0;
        width: 380px;
        height: 540px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.08);
        border-radius: 16px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.18);
        display: flex;
        flex-direction: column;
        overflow: hidden;
        animation: panelSlideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      }
      
      .rag-widget-header {
        background: #1a1a1a;
        color: white;
        padding: 16px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      }
      
      .rag-header-info {
        display: flex;
        align-items: center;
        gap: 10px;
      }
      
      .rag-avatar-dot {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10b981;
      }
      
      .rag-widget-header h4 {
        margin: 0;
        font-size: 15px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: #f5f5f5;
      }
      
      .rag-close-btn {
        background: none;
        border: none;
        color: #808080;
        cursor: pointer;
        font-size: 24px;
        line-height: 1;
        transition: color 0.2s;
      }
      
      .rag-close-btn:hover {
        color: white;
      }
      
      .rag-widget-messages {
        flex: 1;
        overflow-y: auto;
        padding: 20px;
        display: flex;
        flex-direction: column;
      }
      
      /* Typing Indicator Animation */
      .rag-typing-indicator span {
        width: 6px;
        height: 6px;
        background: #808080;
        border-radius: 50%;
        display: inline-block;
        animation: bounce 1.3s infinite ease-in-out;
      }
      .rag-typing-indicator span:nth-child(2) {
        animation-delay: 0.15s;
      }
      .rag-typing-indicator span:nth-child(3) {
        animation-delay: 0.3s;
      }
      
      .rag-widget-input {
        border-top: 1px solid rgba(0, 0, 0, 0.06);
        padding: 14px 16px;
        display: flex;
        gap: 10px;
        background: white;
      }
      
      .rag-input {
        flex: 1;
        border: 1px solid #d4d4d4;
        border-radius: 24px;
        padding: 10px 18px;
        font-size: 13px;
        outline: none;
        transition: all 0.2s;
      }
      
      .rag-input:focus {
        border-color: #0066cc;
        box-shadow: 0 0 0 2px rgba(0, 102, 204, 0.15);
      }
      
      .rag-send-btn {
        background: #0066cc;
        color: white;
        border: none;
        border-radius: 50%;
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: background 0.2s;
      }
      
      .rag-send-btn:hover {
        background: #0052a3;
      }
      
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(6px); }
        to { opacity: 1; transform: translateY(0); }
      }
      
      @keyframes panelSlideIn {
        from { opacity: 0; transform: translateY(20px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
      }
      
      @keyframes bounce {
        0%, 80%, 100% { transform: scale(0); }
        40% { transform: scale(1.0); }
      }
      
      @media (max-width: 480px) {
        .rag-widget {
          bottom: 20px;
          right: 20px;
        }
        
        .rag-widget-panel {
          width: calc(100vw - 40px);
          height: 480px;
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
