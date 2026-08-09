import requests
from bs4 import BeautifulSoup

def fetch_page_content(url: str, max_chars: int = 4000) -> str:
    """
    Fetches the webpage URL and returns clean text up to max_chars.
    
    Args:
        url (str): The target webpage URL to extract content from.
        max_chars (int): Maximum character limit for returned text.
        
    Returns:
        str: Extracted textual content or error message starting with ERROR_FETCHING_URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Business-Opportunity-Scouting-Agent/1.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove scripts, styles, and navigation elements
        for element in soup(["script", "style", "nav", "footer"]):
            element.decompose()
            
        text = soup.get_text(separator=" ", strip=True)
        return text[:max_chars]
    except Exception as error:
        return f"ERROR_FETCHING_URL: {str(error)}"
