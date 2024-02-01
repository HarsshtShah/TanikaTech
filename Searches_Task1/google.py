import requests
import json

url = "https://www.searchapi.io/api/v1/search"
params = {
  "engine": "google_trends",
  "q": "Jewelry",
  "data_type": "RELATED_TOPICS",
  "api_key": "PWYvEQT55QEZaGmkhp9zyEVv"
}

response = requests.get(url, params = params)

resp_text = response.text

d =dict(json.loads(resp_text))

topic = dict(d['related_topics'])

for i in range(len(topic['top'])):
    print(i , ": ",topic['top'][i]['title'])