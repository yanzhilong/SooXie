# -*- coding: utf-8 -*-
import csv
import threading
#  淘宝类目字典

cid_dict = {"低帮鞋": "50012906", "高帮": "50012907", "凉鞋": "50011745", "拖鞋": "50011746"}

tbproperty_xietou = {
    # 高帮低帮鞋头款式
    "圆头": "30233", "尖头": "30232", "扁头": "6280721", "方头": "30234",

    # 凉鞋鞋头款式
    "露趾": "3226297", "套趾": "139173", "夹趾": "139172", "包头": "46112",
}


tbproperty_xietou = {
    # 高帮低帮鞋头款式
    "圆头": "30233", "尖头": "30232", "扁头": "6280721", "方头": "30234",

    # 凉鞋鞋头款式
    "露趾": "3226297", "套趾": "139173", "夹趾": "139172", "包头": "46112",
}

tbproperty_kuangshi = {
    # 拖鞋款式
    "软木拖鞋": "9575796", "鸟巢拖鞋": "21640537", "人字拖": "134273", "一字拖": "3226299",
    "T型": "139170",
}

tbproperty_bihe = {
    # 低帮闭合方式、凉鞋高帮闭合方式
    "搭扣": "139183", "魔术贴": "3227269", "松紧带": "9887404", "套脚": "3267935", "系带": "28102", "套筒": "3226327"
}

tbproperty_bangmiancaizhi = {
    # 帮面材质
    "二层牛皮（除牛反绒）": "668430252", "棉布": "53908", "孔雀皮": "126870948",
    "涤沦": "21852311", "网布": "3702871", "灯芯绒": "28344", "鳄鱼皮": "44858", "牛仔布": "28343",
    "头层牛皮（除牛反绒）": "668328569", "头层猪皮": "26834269", "绸缎": "28354", "太空革": "18339161",
    "亮片布": "14461751", "毛线": "28685", "二层猪皮": "6474787", "多种材质拼接": "28855009",
    "磨砂皮": "9994999", "牛反绒": "668360480", "绒面": "3227901", "珍珠鱼皮": "6856831", "羊反绒（羊猄）": "668304701",
    "羊皮毛一体": "14461016", "羊皮（除羊反绒/羊猄）": "743634287", "羊驼皮": "107798468", "腹膜皮": "57871492",
    "藤草": "14461857", "蛇皮": "44857", "袋鼠皮": "28400", "超纤": "15099895", "马皮": "44855",
    "高丝光反绒皮": "235494498", "鳗鱼皮": "19304060", "鸵鸟皮": "11029301", "鹿皮": "44854", "麂皮": "44673",
    "人造革": "28404", "布": "3804702", "塑胶": "20370",
}


tbproperty_zhengpicaizhi = {
    # 真皮材质工艺、鞋面内里材质
    "水染皮": "18344312", "摔纹皮": "18344313", "半粒面": "113700976", "疯马皮": "18344310",
    "擦色皮": "19440496", "印花皮": "14464884", "贴膜皮": "18344316", "裂纹皮": "18344317", "粒面皮": "18344309", "反绒皮": "18033040",
    "油蜡皮": "18344311", "纳帕纹": "18344314", "压花皮": "14464883", "漆皮": "28402", "树膏皮": "28394027",
    "植鞣": "99579637", "打蜡皮": "6042236", "修面皮": "18344315",
}

tbproperty_xiemianneilicaizhi = {
    # 真皮材质工艺、鞋面内里材质
    "水染皮": "18344312", "摔纹皮": "18344313", "半粒面": "113700976", "疯马皮": "18344310",
    "擦色皮": "19440496", "印花皮": "14464884", "贴膜皮": "18344316", "裂纹皮": "18344317", "粒面皮": "18344309", "反绒皮": "18033040",
    "油蜡皮": "18344311", "纳帕纹": "18344314", "压花皮": "14464883", "漆皮": "28402", "树膏皮": "28394027",
    "植鞣": "99579637", "打蜡皮": "6042236", "修面皮": "18344315",
}

tbproperty_neilicaizhi = {
    # 内里材质
    "无内里": "119244974", "仿毛": "3670020", "兔毛": "21122", "头层牛皮": "3880992", "狐狸毛": "46278",
    "羊毛羊绒混纺": "59182921", "羊皮": "28398",
    "网纱": "9115784", "人造长毛绒": "14465078", "人造短毛绒": "14465077",
}


tbproperty_xgg = {
    # 鞋跟高
    "平跟(小于等于1cm)": "30228", "低跟(1-3cm)": "29069296", "中跟(3-5cm)": "24574746", "高跟(5cm及以上)": "3673609",
}

tbproperty_gdks = {
    # 跟底款式
    "跟底款式": "121296261", "松糕底": "44634045", "内增高": "3994116", "厚底": "19550002",
}

tbproperty_xdcz = {
    # 鞋底材质
    "纯羊毛": "3229201",
    "EVA": "3376399", "EVA发泡胶": "77117384", "MD": "27366", "PU": "3323086",
    "PVC": "29228", "TPR(牛筋）": "807070564", "tpu": "7097887", "橡胶发泡": "19308111", "烟胶": "127517938",
    "皮": "3353142", "聚氨酯": "18956417", "麻": "3267653", "泡沫": "134280", "橡胶": "30161", "木": "3260684",
    "复合底": "3268018", "软木": "18859111",
}

tbproperty_ta = {
    # 图案
    "纯色": "29454", "格子": "29453", "拼色": "3222561", "手绘": "29455",
}


tbproperty_lxys = {
    # 流行元素
    "素面": "3302333", "豹纹": "3255041", "奢华马毛": "91477857", "图腾": "123658", "翻边": "29950",
    "荧光": "6330860", "雕花": "3341344", "迷彩": "52813", "金属": "20369", "马衔扣": "29033539", "车缝线": "115775",
    "皮草装饰": "43735669", "镂空": "115771", "编制": "3347671", "铆钉": "115776", "绣花": "29957",
    "亮片": "29959", "流苏": "115777", "皮革拼接": "3226301", "水钻": "28209",
}

tbproperty_ch = {
    # 场合
    "沙滩": "103414", "宴会": "139179", "办公室": "122738", "约会": "3267767", "日常": "3224795",
    "居家": "4068154", "运动休闲": "3325552", "结婚": "3267768",
}

tbproperty_fg = {
    # 风格
    "青春潮流": "48816930", "复古": "43747", "休闲": "29535", "简约": "109835873", "韩版": "28105", "朋克": "29931",
    "商务": "28908", "日系": "3411108", "英伦": "3291373", "欧美": "125200612", "运动": "1628", "民族风": "132483",
}

tbproperty_jj = {
    # 季节
    "夏季": "29457", "冬季": "29458", "春秋": "29456",
}

tbproperty_gn = {
    # 功能
    "矫正": "599790307", "增高": "112301", "轻质": "25380975", "防水": "3217611", "减震": "7200622", "保暖": "4194098",
    "耐磨": "4526599", "透气": "137928",
}

tbproperty_xzzgy = {
    # 鞋制作工艺
    "固特异": "3280045", "缝制鞋": "14545463", "胶粘鞋": "14545464", "硫化鞋": "3272885", "注压鞋": "14545465",
}

tbproperty_sydx = {
    # 适用对象
    "青年（18-40周岁）": "3267959", "中年（40-60周岁）": "3267960", "老年（60周岁以上）": "101181",
    "儿童（18周岁以下）": "27845"
}

tbproperty_cm = {
    # 适用对象
    "49": "29544",  #
    "50": "29545",  #
    "47": "28396",  # 47
    "46": "28395",  # 46
    "45": "28394",  # 45
    "44": "28393",  # 44
    "43": "28392",  # 43
    "42": "28391",  # 42
    "41": "28390",  # 41
    "40": "28389",  # 40
    "39": "672",  # 39
    "38": "28388",  # 38
    "37": "29542",  # 37
    "36": "671",  # 36
    "35": "670",  # 35
}


tbproperty_ys = {
    # 适用对象
    "黑色": "28341", #
    "乳白色": "28321",  #
    "白色": "28320",  #
    "米白色": "4266701",  #
    "浅灰色": "28332",  #
    "深灰": "3232478",  #
    "灰色": "28334",  #
    "银色": "28330",  #
    "红色": "28326",  #
    "卡其色": "28331",  #
    "金色": "28328",  #
    "黄色": "28324",  #
    "宝蓝色": "3707775",  #
    "深蓝色": "28340",  #
    "蓝色": "28338",  #
    "咖啡色": "129819",  #
    "浅棕色": "30158",  #
    "深棕色": "6588790",  #
    "褐色": "132069",  #
    "粉红色": "3232480",  #
    "桔红色": "4950473", #
    "酒红色": "28327",  #
    "军绿色": "3232483",  #
    "绿色": "28335",  #
    "青色": "3455405",  #
    "天蓝色": "3232484",  #
    "湖蓝色": "5483105",  #
    "深紫色": "3232479",  #
    "紫红色": "5167321",  #
    "紫色": "28329",  #
    "自定义颜色1": "-1001",  #  需要在自定义属性项中添加
    "自定义颜色2": "-1002",  #  同上
}
property_dict = {














}


# 宝贝属性的key
cateProps = {
    "20000": "29534",  # 品牌:other/其他
    "122276315": "",  # 款式
    "122216563": "",  # 鞋底材质
    "20608": "",  # 风格
    "124128491": "",  # 鞋面材质
    "122216629": "",  # 真皮材质工艺
    "122216345": "",  # 适用季节
    "122216632": "",  # 鞋制作工艺
    "20603": "",  # 图案
    "34272": "",  # 流行元素
    "122216561": "",  # 鞋跟、跟底款式
    "122216515": "",  # 场合
    "20019": "",  # 功能
    "122216608": "",  # 适合对象
    "122216351": "",  # 鞋头款式
    "20490": "",  # 闭合方式
    "1626698": "",  # 鞋跟高
    "122216587": "",  # 鞋面内里材料
    "139520082": "",  # 帮面内里材质
}

# 销售属性的key
skuProps = {
    "1627207": "",  # 颜色
    "20549": "",  # 尺码
}
skuProps = {
    "29544": "",  # 49
    "29545": "",  # 50
    "28396": "",  # 47
    "28395": "",  # 46
    "28394": "",  # 45
    "28393": "",  # 44
    "28392": "",  # 43
    "28391": "",  # 42
    "28390": "",  # 41
    "28389": "",  # 40
    "672": "",  # 39
    "28388": "",  # 38
    "29542": "",  # 37
    "671": "",  # 36
    "670": "",  # 35

}
# 销售属性的value


# 第一行英文标题
rows_eng = {
    "title": "",
    "cid": "",
    "seller_cids": "",
    "stuff_status": "",
    "location_state": "",
    "location_city": "",
    "item_type": "",
    "price": "",
    "auction_increment": "",
    "num": "",
    "valid_thru": "",
    "freight_payer": "",
    "post_fee": "",
    "ems_fee": "",
    "express_fee": "",
    "has_invoice": "",
    "has_warranty": "",
    "approve_status": "",
    "has_showcase": "",
    "list_time": "",
    "description": "",
    "cateProps": "",
    "postage_id": "",
    "has_discount": "",
    "modified": "",
    "upload_fail_msg": "",
    "picture_status": "",
    "auction_point": "",
    "picture": "",
    "video": "",
    "skuProps": "",
    "inputPids": "",
    "inputValues": "",
    "outer_id": "",
    "propAlias": "",
    "auto_fill": "",
    "num_id": "",
    "local_cid": "",
    "navigation_type": "",
    "user_name": "",
    "syncStatus": "",
    "is_lighting_consigment": "",
    "is_xinpin": "",
    "foodparame": "",
    "features": "",
    "buyareatype": "",
    "global_stock_type": "",
    "global_stock_country": "",
    "sub_stock_type": "",
    "item_size": "",
    "item_weight": "",
    "sell_promise": "",
    "custom_design_flag": "",
    "wireless_desc": "",
    "barcode": "",
    "sku_barcode": "",
    "newprepay": "",
    "subtitle": "",
    "cpv_memo": "",
    "input_custom_cpv": "",
    "qualification": "",
    "add_qualification": "",
    "o2o_bind_service": "",
}

rows_cntitle = {
    "title": "宝贝名称",
    "cid": "宝贝类目",
    "seller_cids": "店铺类目",
    "stuff_status": "新旧程度",
    "location_state": "省",
    "location_city": "城市",
    "item_type": "出售方式",
    "price": "宝贝价格",
    "auction_increment": "加价幅度",
    "num": "宝贝数量",
    "valid_thru": "有效期",
    "freight_payer": "运费承担",
    "post_fee": "平邮",
    "ems_fee": "EMS",
    "express_fee": "快递",
    "has_invoice": "发票",
    "has_warranty": "保修",
    "approve_status": "放入仓库",
    "has_showcase": "橱窗推荐",
    "list_time": "开始时间",
    "description": "宝贝描述",
    "cateProps": "宝贝属性",
    "postage_id": "邮费模版ID",
    "has_discount": "会员打折",
    "modified": "修改时间",
    "upload_fail_msg": "上传状态",
    "picture_status": "图片状态",
    "auction_point": "返点比例",
    "picture": "新图片",
    "video": "视频",
    "skuProps": "销售属性组合",
    "inputPids": "用户输入ID串",
    "inputValues": "用户输入名 - 值对",
    "outer_id": "商家编码",
    "propAlias": "销售属性别名",
    "auto_fill": "代充类型",
    "num_id": "数字ID",
    "local_cid": "本地ID",
    "navigation_type": "宝贝分类",
    "user_name": "用户名称",
    "syncStatus": "宝贝状态",
    "is_lighting_consigment": "闪电发货",
    "is_xinpin": "新品",
    "foodparame": "食品专项",
    "features": "尺码库",
    "buyareatype": "采购地",
    "global_stock_type": "库存类型",
    "global_stock_country": "国家地区",
    "sub_stock_type": "库存计数",
    "item_size": "物流体积",
    "item_weight": "物流重量",
    "sell_promise": "退换货承诺",
    "custom_design_flag": "定制工具",
    "wireless_desc": "无线详情",
    "barcode": "商品条形码",
    "sku_barcode": "sku 条形码",
    "newprepay": "7天退货",
    "subtitle": "宝贝卖点",
    "cpv_memo": "属性值备注",
    "input_custom_cpv": "自定义属性值",
    "qualification": "商品资质",
    "add_qualification": "增加商品资质",
    "o2o_bind_service": "关联线下服务",
}



default_value = {
    "宝贝名称": "",
    "宝贝类目": "",
    "店铺类目": "",
    "新旧程度": "1",
    "省": "福建",
    "城市": "泉州",
    "出售方式": "1",  # 一口价
    "宝贝价格": "",
    "加价幅度": "0",
    "宝贝数量": "1000",
    "有效期": "7",
    "运费承担": "2",  # 使用模版
    "平邮": "",
    "EMS": "",
    "快递": "0",
    "发票": "0",
    "保修": "0",
    "放入仓库": "1",
    "橱窗推荐": "0",
    "开始时间": "",
    "宝贝描述": "",
    "宝贝属性": "",
    "邮费模版ID": "9213395490",  # 申通部分不包邮
    "会员打折": "0",
    "修改时间": "2017/3/29  16:08:05",
    "上传状态": "200",
    "图片状态": "1;1;1;1;-1;-1;-1;",  # 上了几个图就前面几个1
    "返点比例": "0",

    # (..本地的文件):1:0(这个是主图的顺序0,1,2,3,4):|[这里可选的指定一个在线的图片]'
    "新图片": "1b37f....8:1:0:|;2f6....8b0c17:1:1:|https://www..._074026.jpg;",
    "视频": "",

    # 红色,尺码49价格20数量19
    # 20:19::1627207:28326;20549:29544;
    # 绿色,尺码:49,价格:20,数量:19,SKU:20
    # 20:19:20:1627207:28335;20549:29544;
    # 绿色,尺码:50,价格:30,数量:30
    # 30:30::1627207:28335;20549:29545;
    "销售属性组合": "",
    "用户输入ID串": "13021751",
    "用户输入名 - 值对": "", # 商家编码
    "商家编码": "", # 商家编码
    "销售属性别名": "",
    "代充类型": "0",
    "数字ID": "0",
    "本地ID": "0",
    "宝贝分类": "1", # 未选
    "用户名称": "gfdonx", # 淘宝名称
    "宝贝状态": "6", # 本地库存宝贝(不确定)
    "闪电发货": "216",
    "新品": "241",
    "食品专项": "",
    "尺码库": "mysize_tp:-1;sizeGroupId:29148;sizeGroupName:欧码;sizeGroupType:men_shoes;tags:52290,50370",
    "采购地": "0",
    "库存类型": "-1",
    "国家地区": "",
    "库存计数": "2",
    "物流体积": "bulk:0.000000",
    "物流重量": "1",
    "退换货承诺": "0",
    "定制工具": "",
    "无线详情": "",
    "商品条形码": "",
    "sku 条形码": "",
    "7天退货": "1",
    "宝贝卖点": "",
    "属性值备注": "",
    "自定义属性值": "",
    "商品资质": "%7B%20%20%7D",
    "增加商品资质": "0",
    "关联线下服务": "",
}


class Rowsitem:
    def __init__(self):
        self.title = None
        self.cid = None
        self.seller_cids = None
        self.stuff_status = None
        self.location_state = None
        self.location_city = None
        self.item_type = None
        self.price = None
        self.auction_increment = None
        self.num = None
        self.valid_thru = None
        self.freight_payer = None
        self.post_fee = None
        self.ems_fee = None
        self.express_fee = None
        self.has_invoice = None
        self.has_warranty = None
        self.approve_status = None
        self.has_showcase = None
        self.list_time = None
        self.description = None
        self.cateProps = None
        self.postage_id = None
        self.has_discount = None
        self.modified = None
        self.upload_fail_msg = None
        self.picture_status = None
        self.auction_point = None
        self.picture = None
        self.video = None
        self.skuProps = None
        self.inputPids = None
        self.inputValues = None
        self.outer_id = None
        self.propAlias = None
        self.auto_fill = None
        self.num_id = None
        self.local_cid = None
        self.navigation_type = None
        self.user_name = None
        self.syncStatus = None
        self.is_lighting_consigment = None
        self.is_xinpin = None
        self.foodparame = None
        self.features = None
        self.buyareatype = None
        self.global_stock_type = None
        self.global_stock_country = None
        self.sub_stock_type = None
        self.item_size = None
        self.item_weight = None
        self.sell_promise = None
        self.custom_design_flag = None
        self.wireless_desc = None
        self.barcode = None
        self.sku_barcode = None
        self.newprepay = None
        self.subtitle = None
        self.cpv_memo = None
        self.input_custom_cpv = None
        self.qualification = None
        self.add_qualification = None
        self.o2o_bind_service = None
        self.init_default_value()

    titles = [
        "title",
        "cid",
        "seller_cids",
        "stuff_status",
        "location_state",
        "location_city",
        "item_type",
        "price",
        "auction_increment",
        "num",
        "valid_thru",
        "freight_payer",
        "post_fee",
        "ems_fee",
        "express_fee",
        "has_invoice",
        "has_warranty",
        "approve_status",
        "has_showcase",
        "list_time",
        "description",
        "cateProps",
        "postage_id",
        "has_discount",
        "modified",
        "upload_fail_msg",
        "picture_status",
        "auction_point",
        "picture",
        "video",
        "skuProps",
        "inputPids",
        "inputValues",
        "outer_id",
        "propAlias",
        "auto_fill",
        "num_id",
        "local_cid",
        "navigation_type",
        "user_name",
        "syncStatus",
        "is_lighting_consigment",
        "is_xinpin",
        "foodparame",
        "features",
        "buyareatype",
        "global_stock_type",
        "global_stock_country",
        "sub_stock_type",
        "item_size",
        "item_weight",
        "sell_promise",
        "custom_design_flag",
        "wireless_desc",
        "barcode",
        "sku_barcode",
        "newprepay",
        "subtitle",
        "cpv_memo",
        "input_custom_cpv",
        "qualification",
        "add_qualification",
        "o2o_bind_service",
    ]

    rows_cn_titles = {
        "title": "宝贝名称",
        "cid": "宝贝类目",
        "seller_cids": "店铺类目",
        "stuff_status": "新旧程度",
        "location_state": "省",
        "location_city": "城市",
        "item_type": "出售方式",
        "price": "宝贝价格",
        "auction_increment": "加价幅度",
        "num": "宝贝数量",
        "valid_thru": "有效期",
        "freight_payer": "运费承担",
        "post_fee": "平邮",
        "ems_fee": "EMS",
        "express_fee": "快递",
        "has_invoice": "发票",
        "has_warranty": "保修",
        "approve_status": "放入仓库",
        "has_showcase": "橱窗推荐",
        "list_time": "开始时间",
        "description": "宝贝描述",
        "cateProps": "宝贝属性",
        "postage_id": "邮费模版ID",
        "has_discount": "会员打折",
        "modified": "修改时间",
        "upload_fail_msg": "上传状态",
        "picture_status": "图片状态",
        "auction_point": "返点比例",
        "picture": "新图片",
        "video": "视频",
        "skuProps": "销售属性组合",
        "inputPids": "用户输入ID串",
        "inputValues": "用户输入名 - 值对",
        "outer_id": "商家编码",
        "propAlias": "销售属性别名",
        "auto_fill": "代充类型",
        "num_id": "数字ID",
        "local_cid": "本地ID",
        "navigation_type": "宝贝分类",
        "user_name": "用户名称",
        "syncStatus": "宝贝状态",
        "is_lighting_consigment": "闪电发货",
        "is_xinpin": "新品",
        "foodparame": "食品专项",
        "features": "尺码库",
        "buyareatype": "采购地",
        "global_stock_type": "库存类型",
        "global_stock_country": "国家地区",
        "sub_stock_type": "库存计数",
        "item_size": "物流体积",
        "item_weight": "物流重量",
        "sell_promise": "退换货承诺",
        "custom_design_flag": "定制工具",
        "wireless_desc": "无线详情",
        "barcode": "商品条形码",
        "sku_barcode": "sku 条形码",
        "newprepay": "7天退货",
        "subtitle": "宝贝卖点",
        "cpv_memo": "属性值备注",
        "input_custom_cpv": "自定义属性值",
        "qualification": "商品资质",
        "add_qualification": "增加商品资质",
        "o2o_bind_service": "关联线下服务",
    }

    rows_eng_value = {
        "title": "",
        "cid": "",
        "seller_cids": "",
        "stuff_status": "",
        "location_state": "",
        "location_city": "",
        "item_type": "",
        "price": "",
        "auction_increment": "",
        "num": "",
        "valid_thru": "",
        "freight_payer": "",
        "post_fee": "",
        "ems_fee": "",
        "express_fee": "",
        "has_invoice": "",
        "has_warranty": "",
        "approve_status": "",
        "has_showcase": "",
        "list_time": "",
        "description": "",
        "cateProps": "",
        "postage_id": "",
        "has_discount": "",
        "modified": "",
        "upload_fail_msg": "",
        "picture_status": "",
        "auction_point": "",
        "picture": "",
        "video": "",
        "skuProps": "",
        "inputPids": "",
        "inputValues": "",
        "outer_id": "",
        "propAlias": "",
        "auto_fill": "",
        "num_id": "",
        "local_cid": "",
        "navigation_type": "",
        "user_name": "",
        "syncStatus": "",
        "is_lighting_consigment": "",
        "is_xinpin": "",
        "foodparame": "",
        "features": "",
        "buyareatype": "",
        "global_stock_type": "",
        "global_stock_country": "",
        "sub_stock_type": "",
        "item_size": "",
        "item_weight": "",
        "sell_promise": "",
        "custom_design_flag": "",
        "wireless_desc": "",
        "barcode": "",
        "sku_barcode": "",
        "newprepay": "",
        "subtitle": "",
        "cpv_memo": "",
        "input_custom_cpv": "",
        "qualification": "",
        "add_qualification": "",
        "o2o_bind_service": "",
    }

    def rows_values(self):
        self.rows_eng_value["title"] = self.title
        self.rows_eng_value["cid"] = self.cid
        self.rows_eng_value["seller_cids"] = self.seller_cids
        self.rows_eng_value["stuff_status"] = self.stuff_status
        self.rows_eng_value["location_state"] = self.location_state
        self.rows_eng_value["location_city"] = self.location_city
        self.rows_eng_value["item_type"] = self.item_type
        self.rows_eng_value["price"] = self.price
        self.rows_eng_value["auction_increment"] = self.auction_increment
        self.rows_eng_value["num"] = self.num
        self.rows_eng_value["valid_thru"] = self.valid_thru
        self.rows_eng_value["freight_payer"] = self.freight_payer
        self.rows_eng_value["post_fee"] = self.post_fee
        self.rows_eng_value["ems_fee"] = self.ems_fee
        self.rows_eng_value["express_fee"] = self.express_fee
        self.rows_eng_value["has_invoice"] = self.has_invoice
        self.rows_eng_value["has_warranty"] = self.has_warranty
        self.rows_eng_value["approve_status"] = self.approve_status
        self.rows_eng_value["has_showcase"] = self.has_showcase
        self.rows_eng_value["list_time"] = self.list_time
        self.rows_eng_value["description"] = self.description
        self.rows_eng_value["cateProps"] = self.cateProps
        self.rows_eng_value["postage_id"] = self.postage_id
        self.rows_eng_value["has_discount"] = self.has_discount
        self.rows_eng_value["modified"] = self.modified
        self.rows_eng_value["upload_fail_msg"] = self.upload_fail_msg
        self.rows_eng_value["picture_status"] = self.picture_status
        self.rows_eng_value["auction_point"] = self.auction_point
        self.rows_eng_value["picture"] = self.picture
        self.rows_eng_value["video"] = self.video
        self.rows_eng_value["skuProps"] = self.skuProps
        self.rows_eng_value["inputPids"] = self.inputPids
        self.rows_eng_value["inputValues"] = self.inputValues
        self.rows_eng_value["outer_id"] = self.outer_id
        self.rows_eng_value["propAlias"] = self.propAlias
        self.rows_eng_value["auto_fill"] = self.auto_fill
        self.rows_eng_value["num_id"] = self.num_id
        self.rows_eng_value["local_cid"] = self.local_cid
        self.rows_eng_value["navigation_type"] = self.navigation_type
        self.rows_eng_value["user_name"] = self.user_name
        self.rows_eng_value["syncStatus"] = self.syncStatus
        self.rows_eng_value["is_lighting_consigment"] = self.is_lighting_consigment
        self.rows_eng_value["is_xinpin"] = self.is_xinpin
        self.rows_eng_value["foodparame"] = self.foodparame
        self.rows_eng_value["features"] = self.features
        self.rows_eng_value["buyareatype"] = self.buyareatype
        self.rows_eng_value["global_stock_type"] = self.global_stock_type
        self.rows_eng_value["global_stock_country"] = self.global_stock_country
        self.rows_eng_value["sub_stock_type"] = self.sub_stock_type
        self.rows_eng_value["item_size"] = self.item_size
        self.rows_eng_value["item_weight"] = self.item_weight
        self.rows_eng_value["sell_promise"] = self.sell_promise
        self.rows_eng_value["custom_design_flag"] = self.custom_design_flag
        self.rows_eng_value["wireless_desc"] = self.wireless_desc
        self.rows_eng_value["barcode"] = self.barcode
        self.rows_eng_value["sku_barcode"] = self.sku_barcode
        self.rows_eng_value["newprepay"] = self.newprepay
        self.rows_eng_value["subtitle"] = self.subtitle
        self.rows_eng_value["cpv_memo"] = self.cpv_memo
        self.rows_eng_value["input_custom_cpv"] = self.input_custom_cpv
        self.rows_eng_value["qualification"] = self.qualification
        self.rows_eng_value["add_qualification"] = self.add_qualification
        self.rows_eng_value["o2o_bind_service"] = self.o2o_bind_service
        return self.rows_eng_value


    # 初始化值
    def init_default_value(self):
        global default_value
        self.title = default_value["宝贝名称"]
        self.cid = default_value["宝贝类目"]
        self.seller_cids = default_value["店铺类目"]
        self.stuff_status = default_value["新旧程度"]
        self.location_state = default_value["省"]
        self.location_city = default_value["城市"]
        self.item_type = default_value["出售方式"]
        self.price = default_value["宝贝价格"]
        self.auction_increment = default_value["加价幅度"]
        self.num = default_value["宝贝数量"]
        self.valid_thru = default_value["有效期"]
        self.freight_payer = default_value["运费承担"]
        self.post_fee = default_value["平邮"]
        self.ems_fee = default_value["EMS"]
        self.express_fee = default_value["快递"]
        self.has_invoice = default_value["发票"]
        self.has_warranty = default_value["保修"]
        self.approve_status = default_value["放入仓库"]
        self.has_showcase = default_value["橱窗推荐"]
        self.list_time = default_value["开始时间"]
        self.description = default_value["宝贝描述"]
        self.cateProps = default_value["宝贝属性"]
        self.postage_id = default_value["邮费模版ID"]
        self.has_discount = default_value["会员打折"]
        self.modified = default_value["修改时间"]
        self.upload_fail_msg = default_value["上传状态"]
        self.picture_status = default_value["图片状态"]
        self.auction_point = default_value["返点比例"]
        self.picture = default_value["新图片"]
        self.video = default_value["视频"]
        self.skuProps = default_value["销售属性组合"]
        self.inputPids = default_value["用户输入ID串"]
        self.inputValues = default_value["用户输入名 - 值对"]
        self.outer_id = default_value["商家编码"]
        self.propAlias = default_value["销售属性别名"]
        self.auto_fill = default_value["代充类型"]
        self.num_id = default_value["数字ID"]
        self.local_cid = default_value["本地ID"]
        self.navigation_type = default_value["宝贝分类"]
        self.user_name = default_value["用户名称"]
        self.syncStatus = default_value["宝贝状态"]
        self.is_lighting_consigment = default_value["闪电发货"]
        self.is_xinpin = default_value["新品"]
        self.foodparame = default_value["食品专项"]
        self.features = default_value["尺码库"]
        self.buyareatype = default_value["采购地"]
        self.global_stock_type = default_value["库存类型"]
        self.global_stock_country = default_value["国家地区"]
        self.sub_stock_type = default_value["库存计数"]
        self.item_size = default_value["物流体积"]
        self.item_weight = default_value["物流重量"]
        self.sell_promise = default_value["退换货承诺"]
        self.custom_design_flag = default_value["定制工具"]
        self.wireless_desc = default_value["无线详情"]
        self.barcode = default_value["商品条形码"]
        self.sku_barcode = default_value["sku 条形码"]
        self.newprepay = default_value["7天退货"]
        self.subtitle = default_value["宝贝卖点"]
        self.cpv_memo = default_value["属性值备注"]
        self.input_custom_cpv = default_value["自定义属性值"]
        self.qualification = default_value["商品资质"]
        self.add_qualification = default_value["增加商品资质"]
        self.o2o_bind_service = default_value["关联线下服务"]



def function():
    print("测试是否有空值")
    for key, value in property_dict.items():
        if key is None:
            print value
        if value is None:
            print key

class SooXie:
    def __init__(self):
        self.url = None  # 链接地址
        self.title = None  # 标题
        self.mainimg = None  # 主图列表
        self.shoeno = None  # 货号
        self.price = None  # 价格
        self.popularity = None  # 人气
        self.update = None  # 更新时间
        self.sizes = None  # 尺码
        self.colors = None  # 颜色
        self.images = None  # 图片链接地址
        self.property = None  # 属性
        self.market = None  # 市场

def create_csv():
    rowsitem = Rowsitem()
    # with open("Taobao/shoes.csv", 'wb') as csvfile:
    with open("Taobao/shoes.csv", 'a+') as csvfile: #设置为追加
        writer = csv.DictWriter(csvfile, fieldnames=rowsitem.titles)  # 写入标题行
        writer.writeheader()
        writer.writerow(rowsitem.rows_cn_titles)  # 写入中文行

        # 写入标题
        rowsitem.title = "标题"



        # 写入数据文件
        writer.writerow(rowsitem.rows_values())



        # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def ccreate_csvnew():
    rowsitem = Rowsitem()
    csvfile = file('Taobao/shoes.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(["version 1.00"])
    # writer.writerow(rowsitem.titles)
    # writer.writerows(rowsitem.rows_cn_titles)
    csvfile.close()


def _add_row(rowsitem):
    # with open("Taobao/shoes.csv", 'a+') as csvfile:  # 单独运行的时候
    with open("sooxie/spiders/Taobao/shoes.csv", 'a+') as csvfile:  # 设置为追加,通过爬虫运行的时候
        print "写入开始"
        writer = csv.DictWriter(csvfile, fieldnames=rowsitem.titles)  # 写入标题行
        # 写入标题
        rowsitem.title = "标题"

        # 写入数据文件
        writer.writerow(rowsitem.rows_values())
        csvfile.close()
        print "写入结束"


def get_cid(sooxie):
    # 返加宝贝类目

    return cid_dict["低帮鞋"];

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""

def operator_title(title):

    return ""


def add_row(sooxie):
    # 添加一行数据
    rowsitem = Rowsitem()
    rowsitem.title = sooxie.title;
    rowsitem.cid = get_cid(sooxie);  # 宝贝类目
    rowsitem.seller_cids = "";  # 店铺类目固定,可以为空
    rowsitem.price = sooxie.price;  # 宝贝价格







    def __init__(self):
        self.url = None  # 链接地址
        self.title = None  # 标题
        self.mainimg = None  # 主图列表
        self.shoeno = None  # 货号
        self.price = None  # 价格
        self.popularity = None  # 人气
        self.update = None  # 更新时间
        self.sizes = None  # 尺码
        self.colors = None  # 颜色
        self.images = None  # 图片链接地址
        self.property = None  # 属性
        self.market = None  # 市场

    # _add_row(rowsitem)

    # self.url = None  # 链接地址
    # self.title = None  # 标题
    # self.mainimg = None  # 主图列表
    # self.shoeno = None  # 货号
    # self.price = None  # 价格
    # self.popularity = None  # 人气
    # self.update = None  # 更新时间
    # self.sizes = None  # 尺码
    # self.colors = None  # 颜色
    # self.images = None  # 图片链接地址
    # self.property = None  # 属性
    # self.market = None  # 市场
    #
    # self.title = None
    # self.cid = None
    # self.seller_cids = None
    # self.stuff_status = None
    # self.location_state = None
    # self.location_city = None
    # self.item_type = None
    # self.price = None
    # self.auction_increment = None
    # self.num = None
    # self.valid_thru = None
    # self.freight_payer = None
    # self.post_fee = None
    # self.ems_fee = None
    # self.express_fee = None
    # self.has_invoice = None
    # self.has_warranty = None
    # self.approve_status = None
    # self.has_showcase = None
    # self.list_time = None
    # self.description = None
    # self.cateProps = None
    # self.postage_id = None
    # self.has_discount = None
    # self.modified = None
    # self.upload_fail_msg = None
    # self.picture_status = None
    # self.auction_point = None
    # self.picture = None
    # self.video = None
    # self.skuProps = None
    # self.inputPids = None
    # self.inputValues = None
    # self.outer_id = None
    # self.propAlias = None
    # self.auto_fill = None
    # self.num_id = None
    # self.local_cid = None
    # self.navigation_type = None
    # self.user_name = None
    # self.syncStatus = None
    # self.is_lighting_consigment = None
    # self.is_xinpin = None
    # self.foodparame = None
    # self.features = None
    # self.buyareatype = None
    # self.global_stock_type = None
    # self.global_stock_country = None
    # self.sub_stock_type = None
    # self.item_size = None
    # self.item_weight = None
    # self.sell_promise = None
    # self.custom_design_flag = None
    # self.wireless_desc = None
    # self.barcode = None
    # self.sku_barcode = None
    # self.newprepay = None
    # self.subtitle = None
    # self.cpv_memo = None
    # self.input_custom_cpv = None
    # self.qualification = None
    # self.add_qualification = None
    # self.o2o_bind_service = None
    # self.init_default_value()

def add_row_test():
    rowsitem = Rowsitem()
    rowsitem.title = "测试标题";

    threads = []
    t1 = threading.Thread(target=_add_row, args=(rowsitem,))
    threads.append(t1)
    t2 = threading.Thread(target=_add_row, args=(rowsitem,))
    threads.append(t2)
    t3 = threading.Thread(target=_add_row, args=(rowsitem,))
    threads.append(t3)
    t4 = threading.Thread(target=_add_row, args=(rowsitem,))
    threads.append(t4)
    t5 = threading.Thread(target=_add_row, args=(rowsitem,))
    threads.append(t5)
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
    # _add_row(rowsitem)

def function_run():
    print("--------------------")
    function()
    print("--------------------")
    # create_csv()
    add_row_test()
    print("--------------------")


if __name__ == "__main__":
    function_run()
