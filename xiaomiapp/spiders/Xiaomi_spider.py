import scrapy
import re
import urllib
from scrapy.selector import Selector
from xiaomiapp.items import XiaomiappItem
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

    def find_next_page(self,url):
        try:
            page_num_str = url.split('/')[-1]
            page_num = int(page_num_str)+1
            #Limit the number of pages crawl for testing
            if page_num > 2:
                return None

            url = url[:-len(page_num_str)] + str(page_num)
            return url;
        except ValueError:
            print "### next page url cannot be handled"
            print url
            return None

    def parse_categories(self, response):
        page = Selector(response)
        params = urllib.urlencode({'page': '0'})
        url = response.url
        url1 = url + '#' + params
        while url:
            yield scrapy.Request(url1, self.parse_apps, meta={
                'splash':{
                    'endpoint':"render,html",
                    'args':{'wait':0.1}
                }
            },dont_filter=True)
        url1 = self.find_next_page(url1)

    def parse_apps(self,response):
        page = Selector(response)
        divs = page.xpath(
            '//ul[@id = "all-applist"][@class = "applist"]/li'
        )  # this is the main block in html for all the contents we want to crawl

        for div in divs:
            item = XiaomiappItem() # this is defined in item.py file
            item['title'] = div.xpath('.//h5/a/text()').extract_first().encode('utf-8')
            url = div.xpath('.//h5/a/@href').extract_first() # this is the relative url
            item['url'] = urljoin(response.url, url) # we need to get the absolute urls
            appid = re.match(r'/detail/(.*)', url).group(1)
            item['appid'] = appid
            item['categories'] = div.xpath('.//p[@class="app-desc"]/a/text()').extract_first().encode('utf-8')
            yield item
