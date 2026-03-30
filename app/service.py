"""class URLService:
    def __init__(self):
        self.malware_urls = self._load_malware_urls()

    def _load_malware_urls(self):
        try:
            with open('data/malware_urls.txt', 'r') as f:
                return set(line.strip() for line in f if line.strip())
       except FileNotFoundError:
            return set()

    def is_malicious(self, url: str) -> bool:
        return url in self.malware_urls
"""
from urllib.parse import urlparse

class URLService:
    def __init__(self):
        self.malware_urls = self._load_malware_urls()

    def _load_malware_urls(self):
        try:
            with open('data/malware_urls.txt', 'r') as f:
                return set(self._normalize(line.strip()) for line in f if line.strip())
        except FileNotFoundError:
            return set()

    def _normalize(self, url: str) -> str:
        parsed = urlparse(f"http://{url}")  # asegura parseo correcto
        return f"{parsed.hostname}{parsed.path}".rstrip("/")

    def is_malicious(self, url: str) -> bool:
        normalized = self._normalize(url)
        return normalized in self.malware_urls
