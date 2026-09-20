"""Bounded public-page text extraction. Error states are not source content."""
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url, max_chars=4000):
    if not isinstance(url, str) or urlsplit(url).scheme not in {"http", "https"} or not urlsplit(url).hostname:
        return "ERROR_FETCHING_URL: valid HTTP(S) URL required"
    if not isinstance(max_chars, int) or not 1 <= max_chars <= 8000: raise ValueError("max_chars must be 1–8000")
    try:
        with requests.get(url, headers={"User-Agent":"Thinkbox-Learning-Demo/1.1"}, timeout=10, stream=True) as response:
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "").lower()
            if not any(t in content_type for t in ["text/html", "text/plain", "application/xhtml"]):
                return "ERROR_FETCHING_URL: unsupported content type"
            body = bytearray()
            for chunk in response.iter_content(8192):
                body.extend(chunk)
                if len(body) > 2_000_000: return "ERROR_FETCHING_URL: page too large"
            soup = BeautifulSoup(bytes(body), "html.parser")
            for item in soup(["script", "style", "nav", "footer"]): item.decompose()
            text = soup.get_text(" ", strip=True)
            return text[:max_chars] if text else "ERROR_FETCHING_URL: empty page"
    except requests.RequestException as exc:
        return "ERROR_FETCHING_URL: " + type(exc).__name__
