import requests
import os
from bs4 import BeautifulSoup
import hashlib

def download_html(uri):
    response = requests.get(uri)
    if response.status_code == 200:
        return response.content
    else:
        return None

def generate_hash(uri):
    md5_hash = hashlib.md5(uri.encode())
    return md5_hash.hexdigest()

with open('clean.txt', 'r') as f:
    uri_list = f.readlines()

output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

batch_size = 10000

for batch_index in range(0, len(uri_list), batch_size):
    batch_uri_list = uri_list[batch_index:batch_index+batch_size]
    print("Processing URIs {}-{} out of {}: ".format(batch_index+1, batch_index+len(batch_uri_list), len(uri_list)))

    for index, uri in enumerate(batch_uri_list):
        uri = uri.strip()
        uri_hash = generate_hash(uri)
        print("Processing URI {}/{}: {}".format(index+1, len(batch_uri_list), uri))

        main_text_file = os.path.join(output_folder, 'main_text_{}.txt'.format(uri_hash))
        html_tags_file = os.path.join(output_folder, 'html_tags_{}.txt'.format(uri_hash))
        if os.path.exists(main_text_file) and os.path.exists(html_tags_file):
            print("Files already exist for URI: {}".format(uri))
            continue

        html_content = download_html(uri)
        if html_content is not None:
            soup = BeautifulSoup(html_content, 'html.parser')

            main_text = soup.get_text()

            with open(main_text_file, 'w', encoding='utf-8') as f:
                f.write(main_text)

            with open(html_tags_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))

        else:
            print("Failed to download URI: {}".format(uri))