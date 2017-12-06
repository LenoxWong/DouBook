#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LenoxWong'


from scrapy import Spider, Request
from selenium import webdriver
from ..items import DoubookItem
from ..configs import DEFAULT

class DbSpider(Spider):
    name = 'DB'
    allowed_domains = ['book.douban.com']

    __pt_driver__ = webdriver.PhantomJS()

    basic_url =  'https://book.douban.com/subject_search?search_text={}&cat=1001&start={}'
    page = 0

    def start_requests(self):
        if getattr(self, 'search', None) is None:
            self.search = DEFAULT['search']
        if getattr(self, 'rate', None) is None:
            self.rate = DEFAULT['rate']

        start_url = self.basic_url.format(self.search, self.page)
        yield Request(url=start_url, callback=self.parse)

    def parse(self, response):
        l = len(response.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div').extract())
        print(l)
        if l > 0:
            for detail in response.xpath('//div[@id="wrapper"]/div[@id="root"]//div[@class="detail"]'):
                rate =  detail.xpath('.//span[@class="rating_nums"]/text()').extract_first() or '0.0'
                if float(rate) < float(self.rate):
                    continue

                book = DoubookItem()
                book['title'] = detail.xpath('./div[@class="title"]/a/text()').extract_first() or 'None'
                author = detail.xpath('./div[@class="meta abstract"]/text()').extract_first() or 'Unkown'
                book['author'] = author.split('/')[0].strip()
                book['rate'] = rate
                book['people'] = detail.xpath('.//span[@class="pl"]/text()').extract_first() or 'None'
                book['link'] = detail.xpath('./div[@class="title"]/a/@href').extract_first() or 'None'
                yield book
        if l >= 15:
            self.page += 15
            next_page = self.basic_url.format(self.search, self.page)
            yield Request(url=next_page, callback=self.parse)
