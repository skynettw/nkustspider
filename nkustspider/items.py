# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NkustspiderItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    birthday = scrapy.Field()
    bornplace = scrapy.Field()
