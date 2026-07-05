import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


# get an URL with command line input of "python itunes.py weezer", where weezer is band name
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# JSON: Java script Object Notation
# json.dumps: formats jason responses
print(json.dumps(response.json(), indent=2))

# how to get track name?
o = response.json()
for result in o["results"]:
    print(result["trackName"])