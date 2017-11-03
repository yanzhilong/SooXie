# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from scrapy.exceptions import DropItem


class SooxiePipeline(object):
    def open_spider(self, spider):
        print(u'开始爬虫')

    def process_item(self, item, spider):

        print(u'最后保存')
        # 增加
        shoedomain = ShoeDomain()
        shoedomain.Id = item['Id']
        shoedomain.Title = item['Title']
        shoedomain.Url = item['Url']
        shoedomain.Number = item['Number']
        shoedomain.Price = item['Price']
        shoedomain.Popularity = item['Popularity']
        shoedomain.UpdateStr = item['UpdateStr']
        shoedomain.Market = item['Market']
        shoedomain.Sort = item['Sort']
        # shoedomain.MainImages = item['MainImages']

        shoedb = ShoeDb()
        mainimagedb = MainImageDb()

        shoedb.addentry(shoedomain)
        # mainimagedb.addentrys(shoedomain.MainImages)

        return item

    def close_spider(self, spider):
        print(u'爬虫关闭')