import scrapy
import time


class GatechSpider(scrapy.Spider):
    name = "gatech"
    start_urls = ['https://www.cc.gatech.edu']

    visited = {'/'}

    time_history = [0]

    max_iter = 2500

    url_keywords = {}

    start = time.time()

    def parse(self, response):
        title = response.css('title::text')[0].getall()
        keywords = response.css('div::text').getall() + response.css('p::text').getall()
        phrases = title + keywords
        words = []

        i = 0
        while i < len(phrases):
            if '\n' in phrases[i] or len(phrases[i]) < 4:
                phrases.pop(i)
            else:
                words += phrases[i].strip(",.!?").lower().split()
                i += 1

        self.url_keywords[response.url] = words

        temp_links = response.css('a::attr(href)').getall()
        links = [link for link in temp_links if link[0] == '/' and link not in self.visited]

        self.time_history.append((time.time() - self.start) / 60)

        if len(self.visited) < self.max_iter:
            if len(self.visited) + len(links) > self.max_iter:
                links = links[0:self.max_iter - len(self.visited)]

            self.visited.update(links)
            yield from response.follow_all(links, callback=self.parse)
