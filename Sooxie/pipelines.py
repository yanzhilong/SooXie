# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.image import Image as ImageDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.db.property import Property as PropertyDb
from Sooxie.db.size import Size as SizeDb
from Sooxie.db.color import Color as ColorDb


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
        shoedomain.No = item['No']
        shoedomain.Price = item['Price']
        shoedomain.Popularity = item['Popularity']
        shoedomain.Update = item['Update']
        shoedomain.Market = item['Market']
        shoedomain.Sizes = item['Sizes']
        shoedomain.Colors = item['Colors']
        shoedomain.Images = item['Images']
        shoedomain.MainImages = item['MainImages']
        shoedomain.Properties = item['Properties']

        shoedb = ShoeDb()
        imagedb = ImageDb()
        mainimagedb = MainImageDb()
        propertydb = PropertyDb()
        sizedb = SizeDb()
        colordb = ColorDb()

        shoedb.addentry(shoedomain)
        imagedb.addentrys(shoedomain.Images)
        mainimagedb.addentrys(shoedomain.MainImages)
        propertydb.addentrys(shoedomain.Properties)
        sizedb.addentrys(shoedomain.Sizes)
        colordb.addentrys(shoedomain.Colors)

        return item

    # def process_item(self, item, spider):
    #     print(u'最后保存')


    def close_spider(self, spider):
        print(u'爬虫关闭')