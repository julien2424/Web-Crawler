import logging
import sys
import time

from scrapy.crawler import CrawlerProcess

from web_crawler.output_data import print_data, plot_time_data
from web_crawler.spiders.gatech_spider import GatechSpider

logging.disable(sys.maxsize)

start = time.time()

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(GatechSpider)
process.start()

minutes = (time.time() - start) / 60
print_data(minutes, GatechSpider)
plot_time_data(GatechSpider)
