import json
import requests
from urllib.parse import urlencode

with open('../metadata/config.json', 'r') as f:
    config = json.loads(f.read())
subscriptionKey = config['translate_key']

url = "https://api.cognitive.microsofttranslator.com/translate"

querystring = {"api-version":"3.0",
    'from' : 'en',
	'to' : 'ko'
}
text = "Hello, Worlds!"

content = [{"Text": text}]

headers= {
    'Ocp-Apim-Subscription-Key' : subscriptionKey,
    'Content-Type': "application/json",
    }
response_body = json.dumps(content)
response = requests.request("POST", url, data=response_body, headers=headers, params=querystring)
res = json.loads(response.text)
print(res[0]['translations'][0]['text'])
