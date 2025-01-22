from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def remove_utm_params(url):
    parsed_url = urlparse(url)
    query_params = dict()
    for key, value in parse_qs(parsed_url.query).items():
        if not key.startswith('utm_'):
            query_params[key] = value
    new_query_string = urlencode(query_params, doseq=True)
    new_parsed_url = parsed_url._replace(query=new_query_string)
    new_url = urlunparse(new_parsed_url)
    return new_url

input_file = open('unique-urls.txt', 'r')
output_file = open('cleaned-urls.txt', 'w')

for line in input_file:
    url = line.strip()
    new_url = remove_utm_params(url)
    output_file.write(new_url + '\n')

input_file.close()
output_file.close()
