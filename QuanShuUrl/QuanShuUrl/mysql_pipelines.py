# -*- coding:utf-8 -*-
import logging

from twisted.enterprise import adbapi

from QuanShuUrl.settings import MYSQL_SETTINGS

__author__ = "JSF"
__date__ = "2018/9/20 8:21"


class MysqlPipeline(object):
    def __init__(self, dbpool):
        self.__dbpool = dbpool

    @classmethod
    def from_crawler(cls, settings):
        dbparams = dict(
            host=MYSQL_SETTINGS['HOST'],
            db=MYSQL_SETTINGS['DATABASE'],
            user=MYSQL_SETTINGS['USER'],
            password=MYSQL_SETTINGS['PASSWORD'],
            charset=MYSQL_SETTINGS['CHARSET'],
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        defferd = self.__dbpool.runInteraction(self.db_insert, item)
        defferd.addErrback(self.db_error_handle, item, spider)
        return item

    def db_error_handle(self, failure, item, spider):
        logging.error(f'db_error_handle has error with {item}')
        print(failure)

    def db_insert(self, cursor, item):
        insrt_sql = "INSERT INTO quanbook(book_name, book_author, img_url, overflow_url, overflow) VALUES (%s,%s,%s,%s,%s)"
        item_values = [item["book_name"], item["book_author"], item["img_url"], item["overflow_url"], item["overflow"]]
        cursor.execute(insrt_sql, item_values)
        return True
