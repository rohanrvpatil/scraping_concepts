import scrapy
from basic_scrapy_rugshop.items import BasicScrapyRugshopItem
from scrapy.loader import ItemLoader

class AllrugsSpider(scrapy.Spider):
    name = "allrugs"
    allowed_domains = ["therugshopuk.co.uk"]
    start_urls = ["https://www.therugshopuk.co.uk/rugs-by-room/bedroom-rugs.html"]

    def parse(self, response):
        
        for product in response.css("div.product-item-info"):
            
            l=ItemLoader(item=BasicScrapyRugshopItem(), selector=product)
            
            l.add_css('title', 'img.product-image-photo.image::attr(alt)')
            l.add_css('price', "span.special-price span.price")
            l.add_css('link', 'a.product-item-link::attr(href)')
                    
            yield l.load_item()
        
        next_page = response.css("a[title=Next]::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

