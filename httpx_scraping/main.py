import httpx
from urllib.parse import urljoin

from src import (
    headers, URL, get_page, detail_page_loop
)


def main():
    client = httpx.Client()
    
    current_url=URL
    
    while True:
        page = get_page(client, current_url, headers)
        detail_page_loop(client, page, headers)
        if page.next_page["href"] is False:
            client.close()
            break
        else:
            current_url=urljoin(current_url, page.next_page["href"])
            print(current_url)
            
            
            
if __name__ == '__main__':
    main()