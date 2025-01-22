import requests

# read the URLs from the file
with open('output.txt', 'r', encoding='utf-8') as f:
    urls = [line.strip() for line in f.readlines()]

# resolve each URL and save the final target URI in a new file
with open('resolved-urls.txt', 'w') as f:
    for url in urls:
        try:
            response = requests.get(url, allow_redirects=True, timeout=5)
            final_url = response.url
            f.write(final_url + '\n')
        except:
            print('Error resolving URL:', url)
