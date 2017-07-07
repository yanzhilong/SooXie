# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SooxieItem(scrapy.Item):
    # define the fields for your item here like:
    Id = scrapy.Field()
    Title = scrapy.Field()
    Url = scrapy.Field()
    Number = scrapy.Field()
    Price = scrapy.Field()
    Popularity = scrapy.Field()
    UpdateStr = scrapy.Field()
    Market = scrapy.Field()
    Sort = scrapy.Field()
    Sizes = scrapy.Field()
    Colors = scrapy.Field()
    Images = scrapy.Field()
    MainImages = scrapy.Field()
    Properties = scrapy.Field()
