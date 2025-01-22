import json
import re

# Regular expression to match URLs
url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# Open the JSONL file containing tweets
with open('tweets-1545.jsonl', 'r', encoding='utf-8') as f:
    # Loop over each line in the file
    for line in f:
        # Load the JSON data from the line
        tweet_data = json.loads(line)
        # Extract links from the tweet's text
        links = re.findall(url_pattern, tweet_data['text'])
        # If links were found, write them to the output file
        if links:
            with open('output.txt', 'a', encoding='utf-8') as out_file:
                out_file.write('Tweet: {}\n'.format(tweet_data['text']))
                out_file.write('Links:\n')
                for link in links:
                    out_file.write('{}\n'.format(link))
                out_file.write('\n')