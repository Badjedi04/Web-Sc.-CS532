unique_uris = set()
with open('unique-urls.txt', 'r', encoding='utf-8') as f:
    for uri in f:
        unique_uris.add(uri.strip())

print("Number of unique URIs:", len(unique_uris))
