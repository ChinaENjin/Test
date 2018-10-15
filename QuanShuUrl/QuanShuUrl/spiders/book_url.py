# -*- coding: utf-8 -*-
import hashlib
import logging
import scrapy
from QuanShuUrl.items import QuanshuurlItem
from scrapy_redis.spiders import RedisSpider


def create_hash_msg(input_str, type="sha1"):
    hash_inst = hashlib.sha1(input_str.encode('utf8')) \
        if type == "sha1" else hashlib.md5(input_str.encode('utf8'))
    return hash_inst.hexdigest()


# class BookUrlSpider(scrapy.Spider):
class BookUrlSpider(RedisSpider):
    name = 'book_url'
    allowed_domains = ['quanshuwang.com']
    # start_urls = ['http://www.quanshuwang.com/list/{}_1.html'.format(i) for i in
    #               range(1, 13)]  # 返回一个列表，取值可以使用for in循环得到里面的值
    # start_urls = ['http://www.quanshuwang.com/list/1_1.html']
    redis_key = "book_url:start_urls"

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div/section/ul/li')
        self.log(f'response current_url:{response.url}, fetch {len(div_list)} count.', level=logging.INFO)
        for div in div_list:
            img_url = div.xpath('./a/img/@src').extract_first()  # .//a/img/@src  这种方法以后自己可以试试，也可以取到值
            img_figer = create_hash_msg(img_url) if img_url != None else ''
            book_name = div.xpath('./span/a/@title').extract_first()
            book_author = div.xpath('./span/a[2]/text()').extract_first()
            overflow_url = div.xpath('./span/em/a/@href').extract_first()
            # book_item = QuanshuurlItem(overflow_url=overflow_url)
            book_item = QuanshuurlItem(img_url=[img_url], book_name=book_name, book_author=book_author,
                                       overflow_url=overflow_url, img_figer=img_figer)
            # print(book_item)
            # 详情页
            res = scrapy.Request(overflow_url, meta={"book_item": book_item}, callback=self.parse_detail)
            yield res

        # 下一页
        next_url = response.xpath('//div[@class="pages"]/div/a[@class="next"]/@href').extract_first()
        # print(f'current_url:{response.url},下一页的网址：{next_url}')
        next_request = scrapy.Request(next_url, callback=self.parse) if next_url else "暂无下一页"
        yield next_request
        # 导航条的网址
        for next_urls in self.start_urls:
            next_urls = scrapy.Request(next_urls, callback=self.parse)  # 返回的是一个Request对象，对象不能遍历
            #     print(f'导航条的网址：{next_urls}')
            yield next_urls

    def parse_detail(self, response):
        book_item = response.meta.get("book_item")
        overflow = response.xpath('//*[@id="waa"]/text()').extract_first()
        book_item['overflow'] = overflow
        # print(overflow)
        start_yuedus = response.xpath('//div[@class="b-info"]/div/a/@href').extract()[2]
        start_yuedu = scrapy.Request(start_yuedus, meta={"start_yuedus": start_yuedus}, callback=self.yuedu_detail)
        # print(start_yuedu)
        yield book_item
        yield start_yuedu

    def yuedu_detail(self, response):
        '''获取小说目录'''
        catalogs = response.xpath('//div[@class="chapterNum"]/ul/div/li/a/@href').extract_first()
        # print(catalogs)
        catalog = scrapy.Request(catalogs, meta={"catalogs": catalogs}, callback=self.Zwen)
        yield catalog

    def Zwen(self, response):
        '''爬取小说正文'''
        zwen = response.xpath('//div[@class="bookInfo"]/div/text()').extract_first()
        print(zwen)
