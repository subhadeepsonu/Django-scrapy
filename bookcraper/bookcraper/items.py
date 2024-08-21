# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductcraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass
class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    mrp = scrapy.Field()
    description = scrapy.Field()
    Fit = scrapy.Field()
    Fabric = scrapy.Field()
    Neck = scrapy.Field()
    Sleeve = scrapy.Field()
    Pattern = scrapy.Field()
    Length = scrapy.Field()
    pass