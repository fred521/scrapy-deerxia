# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeerxiaItem(scrapy.Item):
    # define the fields for your item here like:
	productName = scrapy.Field()
	productId = scrapy.Field()
	productUrl = scrapy.Field()
	productSmallImg = scrapy.Field()
	productScriptImgs = scrapy.Field()
	image_urls = scrapy.Field()
	images = scrapy.Field()