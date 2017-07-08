# -*- coding: utf-8 -*-
import scrapy
from Sooxie.domain.Sooxie import *
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.domain.Shoe import Image as ImageDomain
from Sooxie.domain.Shoe import MainImage as MainImageDomain
from Sooxie.domain.Shoe import Property as PropertyDomain
from Sooxie.domain.Shoe import Size as SizeDomain
from Sooxie.domain.Shoe import Color as ColorDomain
from Sooxie.domain.Shoe import TbProperty as TbPropertyDomain
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.image import Image as ImageDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.db.property import Property as PropertyDb
from Sooxie.db.size import Size as SizeDb
from Sooxie.db.color import Color as ColorDb
from Sooxie.db.tbproperty import TbProperty as TbPropertyDb
from Sooxie.domain.taobao import *
from Sooxie.domain.taobao import *
from Sooxie.items import SooxieItem
from Sooxie import db

import re
import uuid
from scrapy import FormRequest
from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "db"

    page = 1  # 页数
    count = 0  # 宝贝计数
    baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页
    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    def parse(self, response):

        # 添加属性到数据库
        tbproperty = TbPropertyDb()

        # ks = []
        # for key in tbproperty_kuangshi:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_kuangshi[key]
        #     property.TbPropertyCategoryId = "970a51ef-4c61-438c-a26b-096f6e5cb8e9"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_bihe:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_bihe[key]
        #     property.TbPropertyCategoryId = "f35464ec-c880-46fd-95d1-9e730e0f94dc"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_bangmiancaizhi:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_bangmiancaizhi[key]
        #     property.TbPropertyCategoryId = "c1d06a63-5615-4142-bbce-7853bdfed12e"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_xiemianneilicaizhi:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_xiemianneilicaizhi[key]
        #     property.TbPropertyCategoryId = "6b687d10-97f7-4088-91ca-b77e5358cafc"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_neilicaizhi:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_neilicaizhi[key]
        #     property.TbPropertyCategoryId = "22ba2f99-5172-4b9f-8a3a-3fe0258574e1"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_xgg:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_xgg[key]
        #     property.TbPropertyCategoryId = "27d290c1-21dc-469d-ba08-9239b552d373"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_gdks:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_gdks[key]
        #     property.TbPropertyCategoryId = "3e1e63f3-e764-4818-8b1d-997bc3534679"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_xdcz:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_xdcz[key]
        #     property.TbPropertyCategoryId = "066f3205-00be-4487-87a6-abd25036e2ab"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_ta:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_ta[key]
        #     property.TbPropertyCategoryId = "7c8cdc4d-0a03-4c71-9806-51b07a4f9f1f"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_lxys:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_lxys[key]
        #     property.TbPropertyCategoryId = "5ef57a3d-c9a5-43b6-b0a3-20d497ef0415"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_ch:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_ch[key]
        #     property.TbPropertyCategoryId = "b4a6159e-1a5f-4d33-b34f-9619161ac54a"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_fg:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_fg[key]
        #     property.TbPropertyCategoryId = "92a9bfe8-19aa-49a8-935b-a194dfa8d1d4"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_jj:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_jj[key]
        #     property.TbPropertyCategoryId = "6fdfec3f-dfc7-4fe2-9798-f0bebb44f8be"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_gn:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_gn[key]
        #     property.TbPropertyCategoryId = "7b7dc769-0ee9-4780-a1c7-7cbf0eb41080"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_xzzgy:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_xzzgy[key]
        #     property.TbPropertyCategoryId = "00187b5d-0bd5-4928-ac50-26a069745020"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_sydx:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_sydx[key]
        #     property.TbPropertyCategoryId = "3da22a3a-2a09-4f63-b3b6-a4438aa9e2cf"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        # ks = []
        # for key in tbproperty_cm:
        #     property = TbPropertyDomain()
        #     property.Id = str(uuid.uuid1())
        #     property.Name = key
        #     property.ValueKey = tbproperty_cm[key]
        #     property.TbPropertyCategoryId = "92edb2a8-cdcb-4bd0-a062-35a5043cc4f7"
        #     ks.append(property)
        # tbproperty.addentrys(ks)

        ks = []
        for key in tbproperty_ys:
            property = TbPropertyDomain()
            property.Id = str(uuid.uuid1())
            property.Name = key
            property.ValueKey = tbproperty_ys[key]
            property.TbPropertyCategoryId = "27c5b0fa-5d6d-45f3-99bb-bc912eaa81b6"
            ks.append(property)
        tbproperty.addentrys(ks)