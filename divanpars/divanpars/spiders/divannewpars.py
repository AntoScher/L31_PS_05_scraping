import scrapy
from scrapy.crawler import CrawlerProcess

class DivanSpider(scrapy.Spider):
    name = "divan"
    start_urls = [
        'https://www.divan.ru/category/svet',
    ]

    def parse(self, response):
        print(f"Visited {response.url}")
        for product in response.css('div.Pk6w8'):
            name = product.css('img::attr(alt)').get()
            if name:
                print(f"Found product: {name}")
            yield {
                'name': name,
            }

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(DivanSpider)
    process.start()
    print("Crawling finished")



      #response.css('div.Pk6w8 img::attr(alt)').get()
    # scrapy crawl divan



        
