# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class FucaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #红球
    redBall = scrapy.Field()
    #蓝球
    blueBall = scrapy.Field()
    #期号
    period = scrapy.Field()
    pass
