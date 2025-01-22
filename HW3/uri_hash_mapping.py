import hashlib

with open('clean.txt', 'r') as f:
    uri_list = f.readlines()

def generate_hash(uri):
    md5_hash = hashlib.md5(uri.encode())
    return md5_hash.hexdigest()

uri_hash_map = {}

for i, uri in enumerate(uri_list):
    uri_hash_map[uri.strip()] = (i+1, generate_hash(uri))

with open('uri_hash_map.csv', 'w') as f:
    f.write("serial_number,uri,hash_value\n")
    for uri, values in uri_hash_map.items():
        f.write(f"{values[0]},{uri},{values[1]}\n")
