import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Define your company's strategic context here
COMPANY_CONTEXT = """
Company Vision: To be the most trusted and efficient digital enterprise globally.
Company Mission: Empower teams through modern workplace tools and intelligent automation.
Strategic Goals:
1. Reduce operational expenses by 15% through cloud efficiency.
2. Improve customer satisfaction (CSAT) to 92% or higher.
3. Automate 40% of manual internal workflows by end of year.
"""

def analyze_initiative(initiative_name: str, doc_text: str) -> dict:
    """
    Uses OpenAI (gpt-4o-mini) to extract strategic benefits and generate an actionable OKR.
    
    Args:
        initiative_name (str): Title or name of the project initiative.
        doc_text (str): Extracted text content from documentation URL.
        
    Returns:
        dict: Containing 'benefits', 'okr', and 'status'.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "benefits": "Error: OPENAI_API_KEY environment variable is not set.",
            "okr": "Error: OPENAI_API_KEY environment variable is not set.",
            "status": "Error: Missing API Key"
        }

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    prompt = f"""
    You are a Principal Business Opportunity Scouting & Strategy Officer.
    
    {COMPANY_CONTEXT}
    
    Initiative Name: {initiative_name}
    Document Content Summary: {doc_text}
    
    Task:
    1. Identify 2 concrete benefits of this initiative as it relates directly to our Vision, Mission, and Strategic Goals.
    2. Create 1 actionable, ambitious Objective and 2 measurable Key Results (OKRs) for this initiative.
    
    Format your response EXACTLY as follows (do not add extra markdown):
    BENEFITS:
    [Your bulleted benefits here]
    
    OKR:
    Objective: [Your objective here]
    KR1: [First key result]
    KR2: [Second key result]
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        # Split output into Benefits and OKR sections
        try:
            parts = raw_text.split("OKR:")
            benefits_part = parts[0].replace("BENEFITS:", "").strip()
            okr_part = f"Objective: {parts[1].strip()}"
            return {"benefits": benefits_part, "okr": okr_part, "status": "Completed"}
        except Exception:
            return {"benefits": raw_text, "okr": "Manual Review Needed", "status": "Completed (Unstructured)"}
    except Exception as e:
        return {
            "benefits": f"Error during AI analysis: {str(e)}",
            "okr": "Failed to generate OKR due to API error",
            "status": f"Error: {type(e).__name__}"
        }
