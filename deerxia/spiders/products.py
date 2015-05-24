# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from deerxia.items import DeerxiaItem
import sys
import os
from subprocess import call
import re
reload(sys)


class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["taobao.com", "dsc.taobaocdn.com"]
    start_urls = (
        'http://item.taobao.com/item.htm?id=36188760898',
    )
    taobaoCookie = {"thw": "glo", "cna": "JWy7DfgG+h4CARgF6TIoX3OB", "swfstore": "299644", "linezing_session": "eaZdnY8oBL1GFCvDXteHSAyY_1431674955128cuFZ_3", "ck1": "", "v": "0", "uc3": "nk2=D8rzF8PaHQ%3D%3D&id2=UoCMhBdp7r25&vt3=F8dAT%2BLPkJcIUziEQCc%3D&lg2=UtASsssmOIJ0bQ%3D%3D", "existShop": "MTQzMjIyNzk0MA%3D%3D", "unt": "liuch58%26center", "lgc": "liuch58", "tracknick": "liuch58", "sg": "836", "cookie2": "1cab4123c77020c5ea33f64b3f58a2e0", "mt": "np=&ci=16_1", "cookie1": "VWsthkiL75zl7yox0ePobQZ6ckq5UNz3ocpBZqjw138%3D", "unb": "115530703", "t": "1cc1d849ce348d2b0d7876a387f366c5", "_cc_": "UtASsssmfA%3D%3D", "tg": "0", "_l_g_": "Ug%3D%3D", "_nk_": "liuch58", "cookie17": "UoCMhBdp7r25", "pnm_cku822":
                    "121UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockt1SnVKf0R4THlDfig%3D%7CU2xMHDJ7G2AHYg8hAS8WKQcnCU8uSDRFaz1r%7CVGhXd1llXGJdYl1oU29bblRpXmNBeEZ%2FQHhGfEZ7R39Lc0txSHNdCw%3D%3D%7CVWldfS0SMggwECkJJwMnGmtFE0U%3D%7CVmhIGCcePgI2AzsbJxIqEjINNgIiHioVKAg0CTwBIR0pFisLNwoyCV8J%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D", "x": "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0", "whl": "-1%260%260%260", "uc1": "lltime=1432225580&cookie14=UoW0EP9aVl%2Fn4Q%3D%3D&existShop=true&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=U%2BGCWk%2F7owY3j65szkPmZQ%3D%3D&tag=2&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0", "_tb_token_": "e5ee6789e835e", "ucn": "center", "isg": "4374392BADFC36131D8A619E3CDABE4D", "l": "AS6byhBQLpKuEnvMvQJgf64Srp2uEi6S"}

    def make_requests_from_url(self, url):
        # item = MyItem()

        # assign url
        # item['start_url'] = url
        request = scrapy.http.Request(url, cookies=self.taobaoCookie)

        # set the meta['item'] to use the item in the next call back
        # request.meta['item'] = item
        return request

    def parse(self, response):
        sel = Selector(response)
        print "start"
        dynamicScript = sel.xpath("//head/script")
        match = re.search(
            '(\/\/dsc.taobaocdn.com\/.*)\"', dynamicScript.extract()[0].encode('UTF-8'))
        # item = response.request.meta['item']
        item = DeerxiaItem()
        item['productScriptImgs'] = match.group()
        item['productId'] = "1234"
        print item['productScriptImgs']
        yield scrapy.http.Request("http:" + item['productScriptImgs'], meta={'item': item}, cookies=self.taobaoCookie, callback=self.product_detail_image_page)
        pass

    def product_detail_image_page(self, response):
        print "get images"
        item = response.meta['item']
        productDetailImages = Selector(response)
        for productBigImage in productDetailImages.xpath("//img/@src"):
        	print productBigImage
        	item['image_urls'] = "http:" + productBigImage.extract()
        return item
