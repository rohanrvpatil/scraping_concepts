CSS selectors:

next_page = response.css("a[title=Next]::attr(href)").get()

all_products= response.css("div.product-item-info")

name=response.css("img.product-image-photo.image::attr(alt)").get()
price=response.css("span.special-price span.price::text").get()
link=response.css("a.product-item-link::attr(href)").get()


Commands:

To just get output of scraping in console
scrapy crawl allrugs

To export csv output
scrapy crawl allrugs -o output.csv -t csv

Starting project
scrapy startproject project_name

Creating genspider
cd project_name
scrapy genspider allrugs rugs.co.uk

To find out css selectors
scrapy shell 'link'


