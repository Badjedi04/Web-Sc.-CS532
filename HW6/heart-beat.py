import pandas as pd
from pandas import DataFrame
import requests

def check_website_status(domain):
    website_status = 'Live'
    try:
        response = requests.get('http://' + domain, timeout = 10)
        if response.status_code != 200:
            website_status = 'Not Live'
    except:
        website_status = 'Not Live'
    return website_status

# Implementation for D1
D1 = pd.read_csv('D1.csv')
D1 = D1.sort_values('# Citations in our Alternative Narrative Tweets', ascending=False)
D1 = D1.iloc[0:10, [0,1,4]]
D1_list = []

for index, row in D1.iterrows():
    website_status = check_website_status(row['Domain'])
    website_object = { 
        'domain': row['Domain'], 
        'type': row['Media Type (Determined through Content Analysis)'],
        'tweets': row['# Citations in our Alternative Narrative Tweets'],
        'status': website_status
        }

    D1_list.append(website_object)

D1_updated_dataframe = DataFrame(D1_list)
D1_updated_dataframe.to_csv('D1_updated_dataset.csv')

# Implementation for D2
D2 = pd.read_csv('D2.csv')
D2 = D2.sort_values('Tweet count', ascending=False)
D2 = D2.iloc[0:10, [0,2]]
D2_list = []

for index, row in D2.iterrows():
    website_status = check_website_status(row['Domain'])
    website_object = { 
        'domain': row['Domain'], 
        'type': '',
        'tweets': row['Tweet count'],
        'status': website_status
        }

    D2_list.append(website_object)

D2_updated_dataframe = DataFrame(D2_list)
D2_updated_dataframe.to_csv('D2_updated_dataset.csv')
