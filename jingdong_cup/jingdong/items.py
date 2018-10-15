# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    creationTime = scrapy.Field()
    productColor = scrapy.Field()
    productSize = scrapy.Field()
    userClientShow = scrapy.Field()
    userLevelName = scrapy.Field()


class IdItem(scrapy.Item):
    id = scrapy.Field()


class CommodityItem(scrapy.Item):
    img_url = scrapy.Field()
    price = scrapy.Field()
    # 简介
    presentation = scrapy.Field()
    # 评价数量
    evaluate_num = scrapy.Field()
    # 店铺
    seller = scrapy.Field()
    title = scrapy.Field()
    img_figer = scrapy.Field()
