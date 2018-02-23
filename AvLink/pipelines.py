# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class AvlinkPipeline(object):
    def __init__(self):
        self.fsave=open('toupai.json','w+')
        pass
    def process_item(self, item, spider):
        self.fsave.write(json.dumps(dict(item))+"\n")
        return item
    def closed(self):
        self.fsave.close()
        pass