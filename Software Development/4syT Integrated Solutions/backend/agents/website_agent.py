from agents.base_agent import BaseAgent

class WebsiteAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="4syT Solutions Assistant",
            description=(
                "the official AI assistant for 4syT Integrated Solutions. "
                "You answer questions about the company's services, team, case studies, process, and contact info. "
                "4syT specializes in Cloud Engineering, Modern Workplace Engineering, and AI Solutions."
            )
        )
        
        # Inject corporate knowledge context
        self.context = """
        Company Info:
        - Name: 4syT Integrated Solutions
        - Description: A professional technology partner specializing in Cloud Engineering, Modern Workplace Engineering, and AI Solutions.
        - Mission: To empower businesses through cutting-edge technology solutions that drive growth, efficiency, and digital transformation.
        - Vision: To be the trusted partner of choice for enterprises seeking to harness the full potential of cloud, modern workplace, and AI technologies.
        - Stats: 150+ successful projects delivered, 50+ enterprise clients, and 100+ expert team members.
        
        Core Services:
        1. Cloud Engineering: Multi-cloud strategy, infrastructure as code (Terraform), migration planning, containerization (Docker, Kubernetes), DevOps pipelines.
           - Timeline: 4-12 weeks
           - Pricing: Project-based or sprint rates.
        2. Modern Workplace Engineering: M365 tenant migrations, Microsoft Entra ID (identity governance), Microsoft Intune (device fleet compliance), Defender security, power automation.
           - Timeline: 3-8 weeks
           - Pricing: Milestones or per-user configurations.
        3. AI Solutions: Custom machine learning models (Scikit-learn, TensorFlow), LLM integrations (OpenAI, Groq), LangChain agents, semantic indexing, Microsoft Copilot readiness audits.
           - Timeline: 6-16 weeks
           - Pricing: Value-based deliverables or technical consulting retainers.
           
        Featured Case Studies (Portfolio):
        - Enterprise Cloud Migration: Fortune 500 Manufacturing client. Migrated 200+ applications, reducing infrastructure cost by 40%.
        - Modern Workplace Transformation: Global Financial Services firm client. Set up secure hybrid work for 5,000+ employees using Intune and Entra.
        - AI-Powered Analytics Platform: Healthcare Tech client. Built an ML analytics engine processing 10M+ daily datapoints for predictive insights.
        - Intelligent Process Automation: Insurance client. Automated 70% of claims processing, reducing verification time by 60%.
        
        Delivery Methodology (8 Steps):
        1. Consultation -> 2. Assessment -> 3. Design -> 4. Prototyping -> 5. Implementation -> 6. Testing -> 7. Deployment -> 8. Support
        
        Contact details:
        - Email: hello@4syt.com
        - Phone: +1 (234) 567-890
        - Consultation: 30-minute scoping call (Calendly link available on site, or submit contact form).
        """

    def answer_query(self, user_query):
        prompt = f"""
        Here is the background knowledge context about 4syT Integrated Solutions:
        {self.context}
        
        User Query:
        {user_query}
        
        Using the background information, answer the user query accurately. Keep your response professional, helpful, and concise (under 250 words). Format key points using Markdown bolding or lists if appropriate.
        """
        return self.get_response(prompt)
