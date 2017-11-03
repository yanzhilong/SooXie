# -*- coding: utf-8 -*-


# 宝贝实体
class Shoe:

    def __init__(self):
        self.Id = None
        self.Title = None
        self.Url = None
        self.Number = None  # 货号
        self.Price = None
        self.Popularity = None
        self.UpdateStr = None
        self.Market = None
        self.Sort = None
        self.MainImages = None


# 主图实体
class MainImage:

    def __init__(self):
        self.Id = None
        self.Url = None
        self.Sort = None
        self.ShoeId = None
