import json
import requests
import pandas as pd


#to yield products one by one
def generate_json(offset):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'ocp-apim-subscription-key': '291a9190a1c6453fb7ae13c799ae5665',
        'origin': 'https://www.petsathome.com',
        'pet-care-platform-search-uid': '',
        'priority': 'u=1, i',
        'referer': 'https://www.petsathome.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-pcp-correlation-id': 'ead7742b-b3c5-4a21-88c6-5b7cd2510be9',
        'x-pcp-correlation-session-id': 'fc2bc962-c25b-4ad7-84f0-7969aa7ef9e1',
        'x-pcp-origin': 'web/pcp',
        'x-pcp-principal-correlation-id': 'f5190552-4de9-4eba-8caf-4114fe5bd37b',
        'x-pcp-referrer': '/search',
    }

    params = {
        'searchTerm': 'dog',
        'offset': offset,
        'limit': '40',
        'sortBy': 'best-match',
        'searchType': 'Product',
    }

    response = requests.get('https://api2.petsathome.com/cs/ecomm/api/v1/search', params=params, headers=headers)

    
    for product in response.json()['products']:
        yield product



results=[]

#storing all products in results
#5000 is used since there are 4870 search results for the term 'dog'
# 100 can be tested with different values
for offset in range(0,5000,40):
    for product in generate_json(offset):
        results.append(product)
        
# generating json file        
with open("./response_data.json", "w") as f:
    json.dump(results, f)

#converting json to xlsx
with open('./response_data.json', 'r') as json_file:
    json_data = json.load(json_file)

    df = pd.json_normalize(json_data)
    df.to_excel('./response_data.xlsx', index=False)

