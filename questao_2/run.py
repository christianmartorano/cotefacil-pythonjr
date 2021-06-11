from scrapy import crawler
from questao_2.spiders.servimed import ServimedSpider


runner = crawler.CrawlerProcess()

runner.crawl(ServimedSpider)
runner.start()
