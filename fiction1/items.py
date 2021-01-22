# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FictionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    # heading = scrapy.Field()
    # sub_head = scrapy.Field()
    pic = scrapy.Field()
    viewer = scrapy.Field()
    isComplete = scrapy.Field()
    #currentchap = scrapy.Field()
    numOfchap = scrapy.Field()
    #latestupdatetime = scrapy.Field()
    commentCount = scrapy.Field()
    favouriteCount = scrapy.Field()
    ratingCount = scrapy.Field()
    url = scrapy.Field()
    pass