import requests
import json
BASE = "http://dc7f8894ba02.ngrok.io/"
response = requests.put(BASE + "hello", {"id": 1})
print(response.json())
