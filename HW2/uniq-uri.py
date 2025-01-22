unique_uris = set()

with open('resolved-urls.txt', 'r', encoding='utf-8') as f:
    for line in f:
        uri = line.strip()
        if uri not in unique_uris:
            unique_uris.add(uri)

with open('unique-urls.txt', 'w') as f:
    for uri in unique_uris:
        f.write(uri + '\n')
