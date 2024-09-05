import httpx

from src import (
    headers, URL, get_page, parse_links, pagination_loop
)










def main():
    client = httpx.Client()
    pagination_loop(client, headers)

    

if __name__ == '__main__':
    main()