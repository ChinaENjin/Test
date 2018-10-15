# -*- coding: utf-8 -*-

import scrapy
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from jingdong.settings import G_IMAGE_SET
from jingdong import settings


# class JingdongSpiderdongPipeline(object):
#
#     def __init__(self):
#         client = MongoClient('mongodb://localhost:27017')
#         db = client['jingdong']
#         self.collection = db["jingdong_cup"]
#
#     def process_item(self, item, spider):
#         content = dict(item)
#         self.collection.insert_one(content)
#         return "OK!"


class JingdongSpiderPipeline(object):
    def __init__(self):
        self.__json_file = open("cup.json", "wb")
        self.__exporter = JsonItemExporter(self.__json_file, encoding="utf-8")
        self.__exporter.start_exporting()

    def close_spider(self, spider):
        self.__exporter.finish_exporting()
        self.__json_file.close()

    def process_item(self, item, spider):
        self.__exporter.export_item(item)
        return item


# class CupImagePipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         if item['img_figer'] not in G_IMAGE_SET:
#             G_IMAGE_SET.add(item['img_figer'])
#             for img_url in item['img_url']:
#                 r = scrapy.Request(img_url)
#                 yield r
#         else:
#             raise DropItem("this image has existed.")
#
#     def item_completed(self, results, item, info):
#         image_path = [data['path'] for status, data in results if status]
#         if len(image_path) == 0:
#             raise DropItem("this image has not existed.")
#         item['img_url'] = image_path
#         return item
