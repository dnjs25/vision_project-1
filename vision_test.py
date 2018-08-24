import requests
import time
import sys
import json
from server import use_translate_api
with open('../metadata/config.json', 'r') as f:
    config = json.loads(f.read())
api_url = "https://eastasia.api.cognitive.microsoft.com/vision/v1.0/describe"
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': config['vision_key'],
}
params = {'maxCandidates': '1'}
with open('static/temp/upload_180613_054312.jpg', 'rb') as f:
    data = f.read()

try:
    start_time = time.time()
    resp = requests.post(api_url, params=params, headers=headers, data=data)
    e = time.time() - start_time
    print(e)
    # print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60), file=sys.stderr)
    resp.raise_for_status()
    res = json.loads(resp.text)
    print(use_translate_api(res['description']['captions'][0]['text']))
except Exception as e:
    print(str(e))
    sys.exit(0)
