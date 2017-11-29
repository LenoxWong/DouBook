# -*- coding: utf-8 -*-
import scrapy


class DbSpider(scrapy.Spider):
    name = 'DB'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/']

    def parse(self, response):
        pass
