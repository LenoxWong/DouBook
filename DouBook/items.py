# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

__author__ = 'LenoxWong'


from scrapy import Item, Field

class DoubookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    author = Field()
    rate = Field()
    people = Field()
    link = Field()
