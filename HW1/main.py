import requests
from bs4 import BeautifulSoup

def get_pdf_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    pdf_links = []
    for link in links:
        try:
            if link.endswith(".pdf"):
                response = requests.head(link, allow_redirects=True)
                content_type = response.headers.get("Content-Type", "").lower()
                if "pdf" in content_type:
                    pdf_links.append((link, response.url, response.headers.get("Content-Length", 0)))
        except:
            pass
    return pdf_links

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python findPDFs.py URL")
        sys.exit(1)
    url = sys.argv[1]
    pdf_links = get_pdf_links(url)
    for link, final_url, size in pdf_links:
        print("URI:", link)
        print("Final URI:", final_url)
        print("Content Length:", size, "bytes")
        print()
