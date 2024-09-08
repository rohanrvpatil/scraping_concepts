import scrapy

class AllrugsSpider(scrapy.Spider):
    name = "allrugs"
    allowed_domains = ["therugshopuk.co.uk"]
    start_urls = ["https://www.therugshopuk.co.uk/rugs-by-room/bedroom-rugs.html"]

    def parse(self, response):
        for item in response.css("div.product-item-info"):
            
            price=item.css("span.special-price span.price::text").get()        
            
            yield {
                'title': item.css("img.product-image-photo.image::attr(alt)").get(),
                'price': price,
                'link': item.css("a.product-item-link::attr(href)").get() 
            }
        
        next_page = response.css("a[title=Next]::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

