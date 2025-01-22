import os
from shutil import copy
import numpy as np

inverted_index = []

for file_name in os.listdir('main_text/'):
    with open(os.path.join('main_text', file_name), 'r', encoding='utf-8') as f:
        content = f.read().lower()
        tokens = content.split()

        clean_tokens = [token.strip('''!()-[]{};:'"\, <>./?@#$%^&*_~–''') for token in tokens]

        unique_tokens = set(filter(None, clean_tokens))

        inverted_index.extend(list(unique_tokens))

unique_tokens = list(set(inverted_index))

with open('inverted_file.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(unique_tokens) + '\n')
