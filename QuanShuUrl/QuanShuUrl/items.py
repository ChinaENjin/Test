# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanshuurlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # div = scrapy.Field()
    img_url = scrapy.Field()
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    overflow_url = scrapy.Field()
    overflow = scrapy.Field()
    next_url = scrapy.Field()
    img_figer = scrapy.Field()


