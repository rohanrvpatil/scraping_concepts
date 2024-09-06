from dataclasses import dataclass
from selectolax.parser import HTMLParser


@dataclass
class Product:
    name: str
    type: str
    price: str
    rating: str

@dataclass
class Response:
    body_html: HTMLParser
    next_page: dict

URL="https://www.rei.com/c/downhill-ski-boots"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.rei.com/c/downhill-ski-boots',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'X-Newrelic-Id': 'XAQFV1JRGwoEXFdWBgEG',
}