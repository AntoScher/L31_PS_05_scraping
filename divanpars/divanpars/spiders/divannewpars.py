import scrapy
from scrapy.crawler import CrawlerProcess

class DivanSpider(scrapy.Spider):
    name = "divan"
    start_urls = [
        'https://www.divan.ru/category/svet',
    ]

    def parse(self, response):       
        for product in response.css('div.Pk6w8'):
            name = product.css('img::attr(alt)').get()
            price = response.css('meta[itemprop="price"]::attr(content)').get()  # Извлечение цены
            link = response.urljoin(response.css('div.lsooF a::attr(href)').get())  # Извлечение ссылки
            
            yield {
                'name': name,
                'price': price,
                'link': link,
            }

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(DivanSpider)
    process.start()
    print("Crawling finished")
