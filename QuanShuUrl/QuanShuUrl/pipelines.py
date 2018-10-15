# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

import scrapy
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi

from QuanShuUrl.settings import G_IMAGE_SET, MYSQL_SETTINGS


class QuanshuurlPipeline(object):
    def __init__(self):
        self.__json_file = open("全网书城.json", "wb")
        self.__exporter = JsonItemExporter(self.__json_file, encoding="utf-8")
        self.__exporter.start_exporting()

    def close_spider(self, spider):
        self.__exporter.finish_exporting()
        self.__json_file.close()

    def process_item(self, item, spider):
        self.__exporter.export_item(item)
        return item

# class MyImagePipeline(ImagesPipeline):
#
#     def get_media_requests(self, item, info):
#         '''
#         从item数据里面提取image url, 产生Request对象
#         将Request发送给scheduler
#         :param item:
#         :param info:
#         :return:
#         '''
#         if item['img_figer'] not in G_IMAGE_SET:
#             G_IMAGE_SET.add(item['img_figer'])
#             for image_url in item['img_url']:
#                 r = scrapy.Request(image_url)
#                 yield r
#         else:
#             raise DropItem("this image has existed.")
#
#     def item_completed(self, results, item, info):
#         '''
#         当image_url request对象处理完成返回response对象后，下载完成后
#         :param results:
#         :param item:
#         :param info:
#         :return:
#         '''
#         image_path = [data['path'] for status, data in results if status]
#         if len(image_path) == 0:
#             raise DropItem("this image has not existed.")
#         item['img_url'] = image_path
#         return item


# class MysqlPipeline(object):
#     def __init__(self, dbpool):
#         self.__dbpool = dbpool
#
#     @classmethod
#     def from_crawler(cls, settings):
#         dbparams = dict(
#             host=MYSQL_SETTINGS['HOST'],
#             db=MYSQL_SETTINGS['DATABASE'],
#             user=MYSQL_SETTINGS['USER'],
#             password=MYSQL_SETTINGS['PASSWORD'],
#             charset=MYSQL_SETTINGS['CHARSET'],
#         )
#         dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         defferd = self.__dbpool.runInteraction(self.db_insert, item)
#         defferd.addErrback(self.db_error_handle, item, spider)
#         return item
#
#     def db_error_handle(self, failure, item, spider):
#         logging.error(f'db_error_handle has error with {item}')
#         print(failure)
#
#     def db_insert(self, cursor, item):
#         insrt_sql = "INSERT INTO quanbook(book_name, book_author, img_url, overflow_url, overflow) VALUES (%s,%s,%s,%s,%s)"
#         item_values = (item["book_name"], item["book_author"], item["img_url"], item["overflow_url"], item["overflow"])
#         cursor.execute(insrt_sql, item_values)
#         return True
