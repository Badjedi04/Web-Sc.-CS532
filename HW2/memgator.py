import sys
import requests
import os


if not os.path.exists("timemaps"):
    os.mkdir("timemaps")


memento_analysis = open("memento_analysis.txt", "w")

with open("cleaned-urls.txt", "r", encoding='utf-8') as fobj:
    count = 0
    for url in fobj:
        # fname = url.split("/")[2]
        #if not os.path.exists(os.path.join("timemaps")):
            #with open(os.path.join("timemaps", fname), "w") as output_file:
        try:
            response = requests.head("http://localhost:1208/timemap/json/" + url.strip())
            print(f'Writing URL:  {url} : {response.status_code}')
            if response.status_code == 200:
                print(response.headers)
                if "x-memento-count" in response.headers:
                    print(response.headers["x-memento-count"])
                    memento_analysis.write(f'url.strip() : {response.headers["x-memento-count"]}\n')
                #mems = response.content.decode("utf-8")
                #new_timeMaps = mems[2:]
                #output_file.write(mems)
                #output_file.flush()
                count += 1
            print("URLs complete: " + str(count))
        except requests.exceptions.RequestException as e:
            print("Exception: {} for link: {}".format(str(e), url.strip()))
