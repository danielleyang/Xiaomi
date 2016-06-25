import scrapy
import re
from scrapy.selector import Selector
from xiaomiapp.items import XiaomiappItem
#from scrapy.spiders import Rule,CrawlSpider
#from scrapy.linkextractors import LinkExtractor
from urlparse import urljoin


class XiaomiSpider(scrapy.Spider):
    name = "xiaomi"
    allowed_domains = ["http://app.mi.com/"]

    # this is the url under one categories we need to crawl
    start_urls = {
        'http://app.mi.com/'
    }

    #rules = [Rule(LinkExtractor(allow=(r'http://app.mi.com/category/5/.*page=[0-9]')),callback='parse_next_page',follow = True)]

    def parse(self, response):
        page = Selector(response)
        hrefs = page.xpath('.//div[@class="sidebar-mod"]/ul[@class="category-list"]/li/a/@href')

        for href in hrefs:
            url = href.extract()
            fullurl = urljoin(response.url, url)
            yield scrapy.Request(fullurl, callback=self.parse_categories, dont_filter=True)

    def parse_categories(self, response):
        page = Selector(response)
        divs = page.xpath(
            '//ul[@id = "all-applist"][@class = "applist"]/li')  # this is the main block in html for all the contents we want to crawl

        for div in divs:
            item = XiaomiappItem() # this is defined in item.py file
            item['title'] = div.xpath('.//h5/a/text()').extract_first().encode('utf-8')
            url = div.xpath('.//h5/a/@href').extract_first() # this is the relative url
            item['url'] = urljoin(response.url, url) # we need to get the absolute urls
            appid = re.match(r'/detail/(.*)', url).group(1)
            item['appid'] = appid
            item['categories'] = div.xpath('.//p[@class="app-desc"]/a/text()').extract_first().encode('utf-8')
            yield item
