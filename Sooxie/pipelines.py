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
from scrapy.exceptions import DropItem


class SooxiePipeline(object):
    def open_spider(self, spider):
        print(u'开始爬虫')

    def process_item(self, item, spider):

        if self.fileter(item) is None:
            raise DropItem(u"不符合")
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
        shoedomain.Sizes = item['Sizes']
        shoedomain.Colors = item['Colors']
        # shoedomain.Images = item['Images']
        shoedomain.MainImages = item['MainImages']
        shoedomain.Properties = item['Properties']

        shoedb = ShoeDb()
        imagedb = ImageDb()
        mainimagedb = MainImageDb()
        propertydb = PropertyDb()
        sizedb = SizeDb()
        colordb = ColorDb()

        shoedb.addentry(shoedomain)
        # imagedb.addentrys(shoedomain.Images)
        mainimagedb.addentrys(shoedomain.MainImages)
        propertydb.addentrys(shoedomain.Properties)
        sizedb.addentrys(shoedomain.Sizes)
        colordb.addentrys(shoedomain.Colors)

        return item

    # 过滤数据
    def fileter(self, item):
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
        shoedomain.Sizes = item['Sizes']
        shoedomain.Colors = item['Colors']
        shoedomain.Images = item['Images']
        shoedomain.MainImages = item['MainImages']
        shoedomain.Properties = item['Properties']
        # 判断属性
        for pro in shoedomain.Properties:
            if pro.Name == u"雪地靴":
                return None
        # 判断标题
        if u"女" in shoedomain.Title:
            return None
        # 判断尺码，没有42以上的就是女鞋
        checksize = False;
        for size in shoedomain.Sizes:
            if size.Num == u"42":
                checksize = True
                break
        if not checksize:
            return None

        # 结束
        return item

    def close_spider(self, spider):
        print(u'爬虫关闭')