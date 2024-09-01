import requests
import json
import pandas as pd

def generate_json():
    cookies = {
        'ai_user': 'qpjfvROlgqhVPm2AqYBURH|2024-09-01T09:53:26.926Z',
        'notifications-hidden-state': '{%22state%22:{%22isNotificationsHidden%22:false}%2C%22version%22:0}',
        'principal-correlation-id': 'f5190552-4de9-4eba-8caf-4114fe5bd37b',
        'pet-care-platform-customer': 'true',
        '__Secure-pcp-auth.csrf-token': '5f7bfbfe783cc7b701ab4d1dea7691fc02012e4e845c01fa149463730398b097%7C6cf79f83c223d8c6ecede30970cfacbc3b464c8446593fd2e95a531335cb056f',
        '__Secure-pcp-auth.callback-url': 'https%3A%2F%2Fwww.petsathome.com',
        'ASLBSA': '0003d5f45bab3384e8551346ac6319e3546498bd3a3b9874351f28108b3c3d2e6939',
        'ASLBSACORS': '0003d5f45bab3384e8551346ac6319e3546498bd3a3b9874351f28108b3c3d2e6939',
        'ai_session': 'kw506PZ9Zzjrwdn3BC5rwn|1725184407014|1725184903731',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Sep+01+2024+15%3A32%3A12+GMT%2B0530+(India+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=8873c084-5eb4-4325-b39d-1410f8192998&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0',
        'OptanonAlertBoxClosed': '2024-09-01T10:02:12.420Z',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'ai_user=qpjfvROlgqhVPm2AqYBURH|2024-09-01T09:53:26.926Z; notifications-hidden-state={%22state%22:{%22isNotificationsHidden%22:false}%2C%22version%22:0}; principal-correlation-id=f5190552-4de9-4eba-8caf-4114fe5bd37b; pet-care-platform-customer=true; __Secure-pcp-auth.csrf-token=5f7bfbfe783cc7b701ab4d1dea7691fc02012e4e845c01fa149463730398b097%7C6cf79f83c223d8c6ecede30970cfacbc3b464c8446593fd2e95a531335cb056f; __Secure-pcp-auth.callback-url=https%3A%2F%2Fwww.petsathome.com; ASLBSA=0003d5f45bab3384e8551346ac6319e3546498bd3a3b9874351f28108b3c3d2e6939; ASLBSACORS=0003d5f45bab3384e8551346ac6319e3546498bd3a3b9874351f28108b3c3d2e6939; ai_session=kw506PZ9Zzjrwdn3BC5rwn|1725184407014|1725184903731; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Sep+01+2024+15%3A32%3A12+GMT%2B0530+(India+Standard+Time)&version=6.26.0&isIABGlobal=false&hosts=&consentId=8873c084-5eb4-4325-b39d-1410f8192998&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0; OptanonAlertBoxClosed=2024-09-01T10:02:12.420Z',
        'priority': 'u=1, i',
        'referer': 'https://www.petsathome.com/',
        'request-id': '|6854251d2c064856bb047144e369dc7a.d227dee086e045fb',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-6854251d2c064856bb047144e369dc7a-d227dee086e045fb-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-nextjs-data': '1',
    }

    params = {
        'searchTerm': 'dog',
    }

    response = requests.get(
        'https://www.petsathome.com/_next/data/LEU7CVLi8TpJnmi4pslRA/en/search.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    json_data = response.json()

    with open('./files/response_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


def export_json():

    with open('./files/response_data.json', 'r') as json_file:
        json_data = json.load(json_file)

    df = pd.json_normalize(json_data['pageProps']['data']['products'])

    df.to_excel('./files/products_data.xlsx', index=False)
