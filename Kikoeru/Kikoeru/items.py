# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KikoeruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class WorkInfoItem(scrapy.Item):
    #年龄限制级
    age_category_string = scrapy.Field()
    #所属的圈子名称
    circle_name = scrapy.Field()
    #被创建的时间
    create_date = scrapy.Field()
    #dl上的销量
    dl_count = scrapy.Field()
    #时长
    duration = scrapy.Field()
    #是否存在字幕
    has_subtitle = scrapy.Field()
    #RJ号，在6位数的情况下直接加上RJ，7位数的情况下需要补0
    RJ = scrapy.Field()
    #是否为nsfw
    nsfw = scrapy.Field()
    #原始作品，一般为日文
    original_workno = scrapy.Field()
    #日元售价
    price = scrapy.Field()
    #评分
    rate_average_2dp = scrapy.Field()
    #销量
    rate_count = scrapy.Field()
    #tags
    tags = scrapy.Field()
    #标题
    title = scrapy.Field()
    #CV的名称可能有多个
    vas = scrapy.Field()
    #语言版本
    language_editions = scrapy.Field()

class ImagesItem(scrapy.Item):
    #图片文件的路径以及名称
    images_path_name = scrapy.Field()
    #图片的url
    image_urls = scrapy.Field()
    images = scrapy.Field()

class FileItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    path = scrapy.Field()
