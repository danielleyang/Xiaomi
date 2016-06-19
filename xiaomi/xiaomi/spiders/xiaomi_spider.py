from scrapy import Spider
from scrapy.selector import Selector
from xiaomi.items import XiaomiItem


class xiaomi_spider(Spider):
    name = "xiaomi"
    allowed_domains = ["http://app.mi.com"]
    start_urls = [
        "http://app.mi.com"
    ]

    def parse(self, response):
        sel = Selector(response)
        contents = sel.xpath('//div[@class="applist-wrap"]/ul[@class="applist"]/li')
        #items = []


        for content in contents:
        	item = XiaomiItem()
        	item['title'] = content.xpath('h5/a/text()').extract()[0]
        	#item['title'] = len(item['title'])
        	item['url'] = content.xpath('h5/a/@href').extract()[0]
        	yield item

