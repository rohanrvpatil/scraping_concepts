<mark>This GitHub repository includes web scraping projects built with Scrapy, Selenium, BeautifulSoup, httpx.</mark>

## basic_scrapy_rugshop:

* **Website:** https://www.therugshopuk.co.uk/rugs-by-room/bedroom-rugs.html
* **Purpose:** Extracts product data of rugs
* **Fields extracted:** name, price, link
* **Scraping tool:** Scrapy
* **Libraries/Methods used:** selectors
* **Exported data:** [output.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/basic_scrapy_rugshop/output.csv)



## beautiful_soup_proxies:

* **Website:** https://free-proxy-list.net/
* **Purpose:** Extracting free proxies and verifying them
* **Fields extracted:** proxy(with port)
* **Scraping tool:** BeautifulSoup
* **Libraries/Methods used:** requests
* **Exported data:** [verified_proxies.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/scraping_proxies/verified_proxies.csv)



## dynamic_hidden_api_json:

* **Website:** https://www.petsathome.com/
* **Purpose:** Extracts product data of pet toys, accessories, food essentials
* **Fields extracted:** 28 columns of product details
* **Scraping tool:** Fetch/XHR tool in Network tab of Console (Extracted json from API)
* **Libraries/Methods used:** requests
* **Exported data:** [products_data.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/extracting_json/files/products_data.xlsx), [response_data.json](https://github.com/rohanrvpatil/scraping_concepts/blob/main/extracting_json/files/response_data.json)



## httpx_scraping:

* **Website:** https://www.rei.com/c/downhill-ski-boots
* **Purpose:** Extracts product data of downhill ski-boots
* **Fields extracted:**  link, name, product_id, price, rating
* **Scraping tool:** python-httpx
* **Libraries/Methods used:** selectors, urljoin, HTMLParser, dataclasses, export functions for csv/xlsx/json
* **Exported data:** [data.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.csv), [data.json](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.json), [data.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.xlsx)


## dynamic_scrapy_splash_beerwulf (test project):

* **Website:** https://www.beerwulf.com/en-gb/c/mixedbeercases
* **Purpose:** Extracts beer product data
* **Fields extracted:**  name, price
* **Scraping tool:** scrapy-splash
* **Libraries/Methods used:** None
* **Exported data:** None



## selenium_amazon_products:

* **Website:** [Amazon searching for "dell i7 laptop"](https://www.amazon.com/s?k=dell+i7+laptop&crid=3OIV4GP9RPUT3&sprefix=dell+i7%2Caps%2C687&ref=nb_sb_ss_ts-doa-p_1_7)
* **Purpose:** Extracting product details of laptops related to "dell i7 laptop"
* **Fields extracted:** link, title, price, brand, model name, screen size, about this item, technical details: summary, rating (out of 5)
* **Scraping tool:** Selenium
* **Libraries/Methods used:** user agent rotation, chrome_options
* **Exported data:** [laptop_details.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/selenium_amazon_products/search_laptop_details/data/laptop_details.xlsx)





| Project Name                          | Website                                                                                           | Purpose                                       | Fields Extracted                                                                 | Scraping Tool           | Libraries/Methods Used                       | Exported Data                                                                                                                                   |
|---------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------|-------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **basic_scrapy_rugshop**              | [therugshopuk.co.uk](https://www.therugshopuk.co.uk/rugs-by-room/bedroom-rugs.html)                | Extracts product data of rugs                 | name, price, link                                                                | Scrapy                  | selectors                                    | [output.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/basic_scrapy_rugshop/output.csv)                                      |
| **beautiful_soup_proxies**            | [free-proxy-list.net](https://free-proxy-list.net/)                                                | Extracting free proxies and verifying them    | proxy (with port)                                                                | BeautifulSoup            | requests                                     | [verified_proxies.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/scraping_proxies/verified_proxies.csv)                      |
| **dynamic_hidden_api_json**           | [petsathome.com](https://www.petsathome.com/)                                                      | Extracts product data of pet toys             | 28 columns of product details                                                   | Fetch/XHR tool           | requests                                     | [products_data.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/extracting_json/files/products_data.xlsx), [response_data.json](https://github.com/rohanrvpatil/scraping_concepts/blob/main/extracting_json/files/response_data.json) |
| **httpx_scraping**                    | [rei.com](https://www.rei.com/c/downhill-ski-boots)                                                | Extracts product data of downhill ski-boots   | link, name, product_id, price, rating                                            | python-httpx             | selectors, urljoin, HTMLParser, dataclasses  | [data.csv](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.csv), [data.json](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.json), [data.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/html_scraping/data_exports/data.xlsx) |
| **dynamic_scrapy_splash_beerwulf**     | [beerwulf.com](https://www.beerwulf.com/en-gb/c/mixedbeercases)                                    | Extracts beer product data                    | name, price                                                                      | scrapy-splash            | None                                        | None                                                                                                                                           |
| **selenium_amazon_products**          | [Amazon](https://www.amazon.com/s?k=dell+i7+laptop&crid=3OIV4GP9RPUT3&sprefix=dell+i7%2Caps%2C687) | Extracting product details of laptops         | link, title, price, brand, model name, screen size, about this item, technical details, rating (out of 5) | Selenium                 | user agent rotation, chrome_options           | [laptop_details.xlsx](https://github.com/rohanrvpatil/scraping_concepts/blob/main/selenium_amazon_products/search_laptop_details/data/laptop_details.xlsx) |
