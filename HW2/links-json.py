import json
import re

# Regular expression to match URLs
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Open the JSON file containing tweets
with open('tweets-1140.json', 'r', encoding='utf-8') as f:
    # Load the JSON data
    tweet_data = json.load(f)

    # Loop over each tweet in the data
    for tweet in tweet_data:
        # Extract links from the tweet's text
        links = re.findall(url_pattern, tweet['text'])
        # If links were found, write them to the output file
        if links:
            with open('output.txt', 'a', encoding='utf-8') as out_file:
                out_file.write('Tweet: {}\n'.format(tweet['text']))
                out_file.write('Links:\n')
                for link in links:
                    out_file.write('{}\n'.format(link))
                out_file.write('\n')
