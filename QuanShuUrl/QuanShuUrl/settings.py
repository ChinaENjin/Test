# -*- coding: utf-8 -*-


# 爬虫项目的名字（自动生成）
BOT_NAME = 'QuanShuUrl'

SPIDER_MODULES = ['QuanShuUrl.spiders']
NEWSPIDER_MODULE = 'QuanShuUrl.spiders'
# ================== redis start ==============
# Redis数据库url
REDIS_URL = 'redis://127.0.0.1:6379'
# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True
# ================= redis end ===================

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# ########日志的相关配置############
LOG_LEVEL = "INFO"

from datetime import datetime
import os

today = datetime.now()

LOG_DIR = "log"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)
# ##################日志配置的结束##############

# Scrapy downloader 并发请求(concurrent requests)的最大值（默认16）
CONCURRENT_REQUESTS = 100

# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数
DOWNLOAD_DELAY = 1  # 默认0
CONCURRENT_REQUESTS_PER_DOMAIN = 100  # 默认16
CONCURRENT_REQUESTS_PER_IP = 100  # 默认16
# 禁用cookies可以避免被ban
COOKIES_ENABLED = False
# Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值（默认100）
# CONCURRENT_ITEMS = 100

# Disable cookies (enabled by default)
# 禁用cookies可以避免被ban
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
# ===============start=====================
# Override the default request headers:
# Scrapy HTTP Request使用的默认header
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# ================end======================
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'QuanShuUrl.middlewares.QuanshuurlSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'QuanShuUrl.middlewares.QuanshuurlDownloaderMiddleware': 543,
    'QuanShuUrl.middlewares.IpProxiesSpiderMiddleware': 410,
    'QuanShuUrl.middlewares.RotateUserAgentMiddleware': 550,
}
# ############ mysql  settings begin ################
MYSQL_SETTINGS = {
    'HOST': '数据库地址',
    'DATABASE': '数据库名称',
    'USER': '登陆用户名',
    'PASSWORD': '登陆密码',
    'CHARSET': 'utf8',
}

SPIDER_DB_OP_DISPATCH = {
    "quanbook": ("INSERT INTO quanbook(book_name, book_author, img_url, overflow_url, overflow) " \
                 "VALUES (%s,%s,%s,%s,%s)",
                 ['book_name', 'book_author', 'img_url', 'overflow_url', 'overflow']),
}

# ############ mysql  settings end ################

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'QuanShuUrl.pipelines.QuanshuurlPipeline': None,
    'QuanShuUrl.mysql_pipelines.MysqlPipeline': 400,
    'QuanShuUrl.my_image_pipeline.MyImagePipeline': 500,
    # 启用RedisPipeline
    'scrapy_redis.pipelines.RedisPipeline': 300
}

IMAGES_STORE = './images'
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
G_IMAGE_SET = set()

# 爬取网站最大允许的深度(depth)值。如果为0，则没有限制
# DEPTH_LIMIT = 0


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 用户代理池
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
]
IP_PROXY = [{"ipaddr": "61.129.70.131:8080"},
            {"ipaddr": '127.0.0.1:8123'},
            {"ipaddr": '167.99.197.73:8080'},
            {"ipaddr": '185.22.174.69:1448'},
            {"ipaddr": '58.65.175.102:80'},
            {"ipaddr": '94.242.58.108:10010'},
            {"ipaddr": '187.44.1.167:8080'},
            {"ipaddr": '119.196.18.50:8080'},
            {"ipaddr": '109.173.7.85:8081'},
            {"ipaddr": '108.61.246.98:8088'},
            {"ipaddr": '159.203.174.2:3128'},
            {"ipaddr": '185.216.35.170:3128'},
            {"ipaddr": '66.70.166.200:80'},
            {"ipaddr": '118.193.26.18:8080'},
            {"ipaddr": '37.187.99.146:3128'},
            {"ipaddr": '101.50.1.2:80'},
            {"ipaddr": '5.152.158.4:8080'},
            {"ipaddr": '185.44.192.243:3128'},
            {"ipaddr": '94.242.58.14:1448'},
            {"ipaddr": '167.99.205.69:8080'},
            {"ipaddr": '178.128.221.122:3128'},
            {"ipaddr": '37.59.80.69:8082'},
            {"ipaddr": '76.190.78.10:3128'},
            {"ipaddr": '178.128.221.121:3128'},
            {"ipaddr": '178.128.208.132:8080'},
            {"ipaddr": '47.75.48.149:80'},
            {"ipaddr": '115.84.179.229:443'},
            {"ipaddr": '60.250.79.187:80'},
            {"ipaddr": '185.118.26.10:80'},
            {"ipaddr": '94.242.58.108:1448'},
            {"ipaddr": '167.99.153.166:8080'},
            {"ipaddr": '94.242.59.135:10010'},
            {"ipaddr": '213.136.105.54:443'},
            {"ipaddr": '213.136.105.54:3128'},
            {"ipaddr": '200.216.227.141:53281'},
            {"ipaddr": '183.88.232.207:8080'},
            {"ipaddr": '185.118.26.10:8080'},
            {"ipaddr": '155.4.12.61:8080'},
            {"ipaddr": '117.202.20.66:555'},
            {"ipaddr": '185.22.172.94:1448'},
            {"ipaddr": '128.199.179.106:8080'},
            {"ipaddr": '94.242.58.14:10010'},
            {"ipaddr": '201.204.174.226:3130'},
            {"ipaddr": '103.251.36.41:80'},
            {"ipaddr": '159.89.22.167:8080'},
            {"ipaddr": '121.152.17.96:3128'},
            {"ipaddr": '209.97.167.247:8080'},
            {"ipaddr": '121.156.109.92:8080'},
            {"ipaddr": '91.121.208.196:3128'},
            {"ipaddr": '197.243.34.228:3128'},
            {"ipaddr": '142.4.209.32:3128'},
            {"ipaddr": '94.130.92.60:3128'},
            {"ipaddr": '47.75.64.102:80'},
            {"ipaddr": '223.197.56.102:80'},
            {"ipaddr": '54.37.74.196:80'},
            {"ipaddr": '185.22.174.69:10010'},
            {"ipaddr": '94.242.58.142:10010'},
            {"ipaddr": '46.101.145.206:3128'},
            {"ipaddr": '128.140.225.41:80'},
            {"ipaddr": '125.21.43.82:8080'},
            {"ipaddr": '178.128.217.141:3128'},
            {"ipaddr": '128.199.142.35:3128'},
            {"ipaddr": '37.187.116.199:80'},
            {"ipaddr": '145.239.93.131:80'},
            {"ipaddr": '115.127.68.70:8080'},
            {"ipaddr": '89.22.175.42:8080'},
            {"ipaddr": '154.119.45.254:53281'},
            {"ipaddr": '165.227.188.89:80'},
            {"ipaddr": '145.255.137.20:8087'},
            {"ipaddr": '213.222.34.200:53281'},
            {"ipaddr": '93.190.142.240:80'},
            {"ipaddr": '177.234.178.120:3128'},
            {"ipaddr": '98.142.237.108:80'},
            {"ipaddr": '94.20.21.37:3128'},
            {"ipaddr": '188.166.175.238:80'},
            {"ipaddr": '137.74.254.242:3128'},
            {"ipaddr": '197.155.158.22:80'},
            {"ipaddr": '188.166.119.186:80'},
            {"ipaddr": '178.250.92.18:8080'},
            {"ipaddr": '139.255.97.12:53281'},
            {"ipaddr": '144.76.62.29:3128'},
            {"ipaddr": '188.165.240.92:3128'},
            {"ipaddr": '138.68.152.99:80'},
            {"ipaddr": '101.4.136.34:8080'},
            {"ipaddr": '213.136.105.54:80'},
            {"ipaddr": '128.199.54.182:8080'},
            {"ipaddr": '47.91.223.245:80'},
            {"ipaddr": '200.255.122.170:8080'},
            {"ipaddr": '189.58.100.169:53281'},
            {"ipaddr": '202.148.20.218:80'},
            {"ipaddr": '202.125.94.139:1234'},
            {"ipaddr": '195.91.200.216:8080'},
            {"ipaddr": '187.65.49.137:3128'},
            {"ipaddr": '75.150.88.59:80'},
            {"ipaddr": '200.54.108.54:80'},
            {"ipaddr": '217.24.161.98:8080'},
            {"ipaddr": '35.225.208.4:80'},
            {"ipaddr": '83.169.202.2:3128'},
            {"ipaddr": '185.8.238.188:8181'},
            {"ipaddr": '119.28.37.58:80'},
            {"ipaddr": '83.64.253.168:80'},
            {"ipaddr": '24.245.100.212:48678'},
            {"ipaddr": '103.9.124.210:8080'},
            {"ipaddr": '195.234.87.211:53281'},
            {"ipaddr": '54.39.46.86:3128'}
            ]
