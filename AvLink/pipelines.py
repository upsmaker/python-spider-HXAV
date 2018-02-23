# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class AvlinkPipeline(object):
    def open_spider(self,spider):
        print "=================Open spider"
        print spider.name
        if cmp(spider.name,"toupai")==0:
            
            self.ftoupai=open('toupai.json','w+')
        elif cmp(spider.name, "yzsq")==0:
            self.fyzsq=open('yzsq.json','w+')
        pass
    def process_item(self, item, spider):
        if cmp(spider.name,"yzsq")==0:
            print "===========YZSQ"
            self.fyzsq.write(json.dumps(dict(item))+"\n")
        elif cmp(spider.name,"toupai")==0:
            print "===========TOUPAI"
            self.ftoupai.write(json.dumps(dict(item))+"\n")
        return item
    def close_spider(self,spider):
        print "=================Close spider"
        if cmp(spider.name,"toupai")==0:
            self.ftoupai.close()
        elif cmp(spider.name, "yzsq")==0:
            self.fyzsq.close()
        
        
        