# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http.request import Request

class DeerxiaPipeline(object):
    def process_item(self, item, spider):
        return item
    pass

class ProductImagesPipeLine(ImagesPipeline):
    def get_media_requests(self, item, info):
    	for image_url in item['image_urls']:
    		yield Request("http:" + image_url[0], meta={'productId': item['productId']})
    def item_completed(self, results, item, info):
    	return super(ProductImagesPipeLine, self).item_completed(results, item, info)

    def file_path(self, request, response=None, info=None):
    	f_path = super(ProductImagesPipeLine, self).file_path(request, response, info)
    	f_path = f_path.replace('full', request.meta['productId'], 1)
        return f_path
        pass