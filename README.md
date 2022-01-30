# Scrapy Web Crawler

### Installation
1. Install Python 3.x
2. Install scrapy [here](https://docs.scrapy.org/en/latest/intro/install.html)
3. Install any other libraries required
4. Run ```__init__.py```

### Pros
* Relatively quick (x pages per minute)
* Stores most keywords from every page
* Normalizes keywords by making them all lower case, getting rid of characters that aren't alphanumeric
* Never scrapes the same url twice.
* Doesn't stop running if we reach a malfunctioning page


### Cons
* Misses some keywords that have weird formatting
* Lack of stemming
* Indexing keywords would be inefficient for searching (no order and a lot)
* Doesn't prioritize titles and headers as keywords
* Only uses one spider which will limit speed

### Crawl Statistics and Plots
![plot](web_crawler/images/4675_plot.png)
![stats](web_crawler/images/4675_stats.PNG)

### Experience
I started my project using a Python library called Scrapy. This library allows me to put in a URL and it gives me information about the website. I specifically took links and text from every website visited. I used the links to crawl more websites and the text to store useful keywords. Every page I went to crawled all the URL’s within that page unless that URL was already visited (no repeats allowed). It kept on doing this until no new URL’s were found or the program reached a maximum. It was challenging to figure out exactly how the Scrapy library worked as the documentation was vague and confusing at points. I tried to combine using a library that extracts data from websites and Scrapy but I resorted to using scrapy for both as it made the runtime much faster.

### Lessons Learned
I learned that the library you use to extract data from websites dramatically affects the runtime. Using some inefficient libraries resulted in runtimes that were 10 times slower than others. Doing research on this was useful and something I wish I did from the start. I also learnt that extracting different types of text from different types of websites is challenging. Scraping a website to extract keywords means extracting text from headers, paragraphs, etc. and the layout of websites isn’t always the same. Lastly, dealing with websites that lead to bad gateways was challenging as the library I was using couldn’t handle it. I had to change my function from following one page at a time to following a group of links. Therefore, if I hit a bad link, I still had other URL’s that kept my program running. Scraping only parts of websites lead to increased efficiency but also decreased information, which is a tradeoff I would have to investigate more if I took this project further.

### Prediction
The relationship between URL’s crawled and time is linear according to the graph, so If it takes 1.95 minutes time to crawl 2206 pages, then crawling 10 million pages should take about 8,839 minutes. 1 billion pages should take about 883,952 minutes.

### Resources
[scrapy](https://scrapy.org/) \n
[pyplot](https://matplotlib.org/stable/index.html)

