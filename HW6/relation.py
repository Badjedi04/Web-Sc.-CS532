import pandas as pd
from pandas import DataFrame

def lowercase_domain_names(dataset):
    dataset["Domain"] = dataset["Domain"].str.lower()
    return dataset

def get_mutual_links(dataset1, dataset2):
    links_set1 = set(dataset1.iloc[:,0])
    links_set2 = set(dataset2.iloc[:,0])
    mutual_links = set.intersection(links_set1, links_set2)
    return mutual_links

def save_mutual_dataset(mutual_links, file_name):
    mutual_dataset = DataFrame(mutual_links, columns=['Domain'])
    mutual_dataset.to_csv(file_name, index=False)

def count_domains(file_name):
    mutual_dataset = pd.read_csv(file_name)
    count = len(mutual_dataset.index)
    return count

def get_unique_domains(*args):
    list_domains = []
    for file_name in args:
        mutual_dataset = pd.read_csv(file_name)
        for index, row in mutual_dataset.iterrows():
            list_domains.append(str(row['Domain']))
    domain_set = set(list_domains)
    unique_domains = list(domain_set)
    return unique_domains

# Lowercase domain names in all datasets
D1_dataset = pd.read_csv('D1.csv')
D1_dataset = lowercase_domain_names(D1_dataset)
D2_dataset = pd.read_csv('D2.csv')
D2_dataset = lowercase_domain_names(D2_dataset)
D3_dataset = pd.read_csv('D3.csv')
D3_dataset = lowercase_domain_names(D3_dataset)

# Find mutual links between datasets
D1_D2_mutual_links = get_mutual_links(D1_dataset, D2_dataset)
D2_D3_mutual_links = get_mutual_links(D2_dataset, D3_dataset)
D1_D3_mutual_links = get_mutual_links(D1_dataset, D3_dataset)
D1_D2_D3_mutual_links = set.intersection(D1_D2_mutual_links, D3_dataset.iloc[:,0])

# Save mutual datasets to CSV files
save_mutual_dataset(D1_D2_mutual_links, 'D1_D2_mutual_links.csv')
save_mutual_dataset(D2_D3_mutual_links, 'D2_D3_mutual_links.csv')
save_mutual_dataset(D1_D3_mutual_links, 'D1_D3_mutual_links.csv')
save_mutual_dataset(D1_D2_D3_mutual_links, 'D1_D2_D3_mutual_links.csv')

# Count number of domains in each mutual dataset
D1_D2_mutual_count = count_domains('D1_D2_mutual_links.csv')
D2_D3_mutual_count = count_domains('D2_D3_mutual_links.csv')
D1_D3_mutual_count = count_domains('D1_D3_mutual_links.csv')
D1_D2_D3_mutual_count = count_domains('D1_D2_D3_mutual_links.csv')

# Print unique domains
unique_domains = get_unique_domains('D1_D2_mutual_links.csv', 'D2_D3_mutual_links.csv', 'D1_D3_mutual_links.csv', 'D1_D2_D3_mutual_links.csv')
for domain in unique_domains:
    print(domain)
