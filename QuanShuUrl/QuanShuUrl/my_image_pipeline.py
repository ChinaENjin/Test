# -*- coding:utf-8 -*-
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from QuanShuUrl.settings import G_IMAGE_SET

__author__ = "JSF"
__date__ = "2018/9/20 8:22"


class MyImagePipeline(ImagesPipeline):
    '''
    下面的这个函数可以用来调试，img_url为空时程序会报错，就可以在if后面添加一句and  item['img_url'] is not None:
    来消除错误，但是空的还是存在，故解决办法还得自己想办法解决
    '''

    # def get_media_requests(self, item, info):
    # if item['img_figer'] not in G_IMAGE_SET and  item['img_url'] is not None:
    #     G_IMAGE_SET.add(item['img_figer'])
    #     # for img_url in item['img_url']:
    #     r = scrapy.Request(item['img_url'])   # 返回的是一个Request对象
    #     yield r
    # else:
    #     raise DropItem("this image has existed.")

    def get_media_requests(self, item, info):
        if item['img_figer'] not in G_IMAGE_SET:  # and  item['img_url'] is not None:接在G_IMAGE_SET后面可以判断None
            G_IMAGE_SET.add(item['img_figer'])
            for img_url in item['img_url']:
                r = scrapy.Request(img_url)
                yield r
        else:
            raise DropItem("this image has existed.")

    def item_completed(self, results, item, info):
        image_path = [data['path'] for status, data in results if status]
        if len(image_path) == 0:
            raise DropItem("this image has not existed.")
        item['img_url'] = image_path
        return item
