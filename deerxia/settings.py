# -*- coding: utf-8 -*-

# Scrapy settings for deerxia project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'deerxia'

SPIDER_MODULES = ['deerxia.spiders']
NEWSPIDER_MODULE = 'deerxia.spiders'
COOKIES_ENABLED = True
RETRY_ENABLED = True
#DOWNLOAD_TIMEOUT = 15
LOG_FILE = 'tb.log'
COOKIES_DEBUG = True
ensure_ascii = False
DOWNLOADER_MIDDLEWARES = {
     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
     'deerxia.spiders.custom_useragent.CustomUserAgentMiddleware' : 400
}
CONCURRENT_ITEMS = 1
ITEM_PIPELINES = {'deerxia.pipelines.DeerxiaPipeline': 1, 'deerxia.pipelines.ProductImagesPipeLine': 1}
IMAGES_STORE = './products'
#DOWNLOAD_DELAY = 10

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'deerxia (+http://www.yourdomain.com)'
