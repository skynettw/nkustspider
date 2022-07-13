
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class NkustspiderPipeline:
    def __init__(self):
        self.conn = MongoClient("mongodb://root:example@localhost:27017/")
        self.db = self.conn.quoteDB
        self.collection = self.db.quotes    
        
    def process_item(self, item, spider):
        try:
            self.collection.insert_one(dict(item))
        except:
            pass
        return item
