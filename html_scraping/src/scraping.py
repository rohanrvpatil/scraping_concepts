from selectolax.parser import HTMLParser
from urllib.parse import urljoin

from rich import print

from src import (
    Product, Response
)


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
    
    html=page.body_html
    a_tags=html.css("div#search-results > ul li > a")
    product_links={a_tag.attrs["href"] for a_tag in a_tags} #set is denoted by {}. Used here to remove duplicates
    
    for link in product_links:
        details_page=get_page(client, urljoin(base_url, link), headers)
        parse_details(urljoin(base_url, link),details_page.body_html)
        
    
def parse_details(product_link, html):
    from src import (
        export_csv, export_xlsx, export_json
    )
    
    new_product=Product (
        link=product_link,
        name=extract_text(html, "h1#product-page-title",0),
        product_id=extract_text(html, "ol.cdr-breadcrumb__list_15-1-0 li:last-child a",0),
        price=extract_text(html, "span#buy-box-product-price.price-value",0),
        rating=extract_text(html, "span.cdr-rating__number_15-1-0",0),
    )
    #print(new_product)
    export_json(new_product)
    

    