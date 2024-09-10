import scrapy
from scrapy_splash import SplashRequest



class BeerProductsSpider(scrapy.Spider):
    name = "beer_products"
    #allowed_domains = ["https://www.beerwulf.com/"]
    #start_urls = ["https://www.beerwulf.com/en-gb/c/mixedbeercases"]
    
    def start_requests(self):
        url="https://www.beerwulf.com/en-gb/c/mixedbeercases"
        
        yield SplashRequest(url=url, callback=self.parse)
        
        
    def parse(self, response):
        products=response.css("div#product-items-container a")
        
        for product in products:
            yield {
                'name': product.css("div.product-name::text").get(),
                'price': product.css('span.price::text').get()
            }
