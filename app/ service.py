class URLService:
    def __init__(self, filepath="data/malware_urls.txt"):
        self.malware_urls = set()
        with open(filepath, "r") as f:
            for line in f:
                self.malware_urls.add(line.strip())

    def is_malicious(self, url: str) -> bool:
        return url in self.malware_urls