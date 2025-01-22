import sys
import requests

with open("cleaned_urls.txt", "r", encoding='utf-8') as file:
    count = 1
    with open("TimeMap2.json", "a+") as output_file:
        for link in file:
            try:
                response = requests.get("http://localhost:1208/timemap/json/" + link.strip())
                if response.ok:
                    mems = response.content.decode("utf-8")
                    new_timeMaps = mems[2:]
                    output_file.write(new_timeMaps)
                    output_file.flush()
                    count += 1
                print(count)

            except requests.exceptions.RequestException as e:
                print("Exception: {} for link: {}".format(str(e), link.strip()))