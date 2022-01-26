from pprint import pprint

from matplotlib import pyplot as plt


def print_data(minutes, GatechSpider):
    print("Time: " + str(round(minutes, 2)) + " minutes")
    print("Crawled: " + str(len(GatechSpider.url_keywords)) + " pages")
    print("Keywords / Page (avg): " + str(get_avg_keyword(GatechSpider.url_keywords, GatechSpider.max_iter)) + " keywords")
    print("Pages / Minute: " + str(round(len(GatechSpider.url_keywords) / minutes, 0)) + " per minute")
    # pprint(GatechSpider.url_keywords)


def get_avg_keyword(url_keywords, max_iter):
    keyword_sum = 0
    for key, value in url_keywords.items():
        keyword_sum += len(value)
    return round(keyword_sum/max_iter, 1)


def plot_time_data(GatechSpider):
    x = [*range(len(GatechSpider.time_history))]
    y = GatechSpider.time_history

    plt.plot(x, y)
    plt.xlabel('# URL Crawled')
    plt.ylabel('Time (minutes)')
    plt.title('# of Pages Crawled per Minute')

    plt.show()
