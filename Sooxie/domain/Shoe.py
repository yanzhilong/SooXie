# -*- coding: utf-8 -*-


# 宝贝实体
class Shoe:

    def __init__(self):
        self.Id = None
        self.Title = None
        self.Url = None
        self.No = None  # 货号
        self.Price = None
        self.Popularity = None
        self.Update = None
        self.Market = None
        self.Sizes = None
        self.Colors = None
        self.Images = None
        self.MainImages = None
        self.Properties = None


# 详情图实体
class Image:

    def __init__(self):
        self.Id = None
        self.Url = None
        self.ShoeId = None


# 主图实体
class MainImage:

    def __init__(self):
        self.Id = None
        self.Url = None
        self.ShoeId = None


# 属性实体
class Property:

    def __init__(self):
        self.Id = None
        self.Name = None
        self.ShoeId = None


# 尺码实体
class Size:

    def __init__(self):
        self.Id = None
        self.Num = None
        self.ShoeId = None


# 颜色实体
class Color:

    def __init__(self):
        self.Id = None
        self.Name = None
        self.ShoeId = None
