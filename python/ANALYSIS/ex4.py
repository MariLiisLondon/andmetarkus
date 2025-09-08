#üaigalda pip install tools.api_request

import requests
import json

url =  "https://demo-datahub.rik.ee/api/v1/meta/classifications" 
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))
   