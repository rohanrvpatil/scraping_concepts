import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from urllib.parse import urljoin

from rich import print

@dataclass
class Product:
    name: str
    sku: str
    price: str
    rating: str

@dataclass
class Response:
    body_html: HTMLParser
    next_page: dict
    
def pagination_loop(client, headers):
    url="https://www.rei.com/c/downhill-ski-boots"
    while True:
        page = get_page(client, url, headers)
        detail_page_loop(client, page, headers)
        if page.next_page["href"] is False:
            client.close()
            break
        else:
            url=urljoin(url, page.next_page["href"])
            print(url)
        #print(page)
        #print(parse_links(page.body_html))


def get_page(client, URL, headers):
    response=client.get(URL, headers=headers)
    html=HTMLParser(response.text)
    if html.css_first("a[data-id=pagination-test-link-next]"):
        next_page=html.css_first("a[data-id=pagination-test-link-next]").attributes
    else:
        next_page={"href":False}
    return Response(body_html=html, next_page=next_page)

def extract_text(html, selector, index):
    try:
        return html.css(selector)[index].text(strip=True)
    except IndexError:
        return "none"
    
def detail_page_loop(client, page, headers):
    base_url="https://www.rei.com/"
    product_links=parse_links(page.body_html)
    for link in product_links:
        details_page=get_page(client, urljoin(base_url, link), headers)
        parse_details(details_page.body_html)
        
    
def parse_details(html):
    new_product=Product(
        name=extract_text(html, "h1#product-page-title",0),
        sku=extract_text(html, "a.cdr-breadcrumb__link_15-1-0",0),
        price=extract_text(html, "span#buy-box-product-price.price-value.price-value--sale",0),
        rating=extract_text(html, "span.cdr-rating__number_15-1-0",0),
    )
    print(new_product)

def parse_links(html):
    a_tags=html.css("div#search-results > ul li > a")
    return {a_tag.attrs["href"] for a_tag in a_tags}  #set is denoted by {}. Used here to remove duplicates
    
    