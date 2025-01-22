import os
import numpy as np

from pandas import DataFrame

idf = np.round(np.log2(60000000000 / 3730000000), 3)

rows = []
count = 0
for item in os.listdir('stopword_coronavirus/'):
    if count == 10:
        break
    with open('stopword_coronavirus/' + item, 'r', encoding='utf-8') as filehandle:
        file_content = filehandle.read().lower()

    word_count = len(file_content.split())
    term_count = file_content.count('coronavirus')

    term_freq = np.round(term_count / word_count, 3)
    tf_idf = np.round(term_freq * idf, 3)

    rows.append([item, term_freq, idf, tf_idf])
    count += 1

result = DataFrame(rows, columns=['File', 'TF', 'IDF', 'TF-IDF'])
result.to_csv('rank-tf-idf.csv')
print(result)
