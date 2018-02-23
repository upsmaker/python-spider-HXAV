# -*- coding: utf-8 -*-
import scrapy
from AvLink.items import AvlinkItem



class ToupaiSpider(scrapy.Spider):
    name = 'toupai'
    allowed_domains = ['www.hxsq7777.com','template.backgroundimagecache.email']
    start_urls = ['http://www.hxsq7777.com/forum-82-1.html']
#     start_urls = ['http://www.hxsqdd.com/thread-25473-1-1.html']
#     start_urls = ['http://template.backgroundimagecache.email:2200/share/hL3AzKupaMpy4Jtu']
    baseUrl="http://www.hxsq7777.com/"
    def parse(self,response):
        a=response.xpath('//h3/a')
        for u in a:
#             print u.xpath("text()").extract()[0]
            L1=u.xpath('@href').extract()[0]
            print "================L1============="
#          获取如斯：   http://www.hxsq7777.com/thread-25340-1-1.html
            print self.baseUrl+L1
            yield scrapy.Request(self.baseUrl+L1,callback=self.parse_pageL1)
        nextURL=response.xpath("//a[@class='nxt']/@href").extract()[0]
        print "============nextURL:%s"%nextURL
        if nextURL:
            yield scrapy.Request(self.baseUrl+nextURL,callback=self.parse)
    def parse_pageL1(self,response):
#         获取如斯：    http://template.backgroundimagecache.email:2200/share/pWpztU7k1a7o71Ej
        print "================L2============="
        L2=response.xpath("//iframe/@src").extract()[0]
        print L2
        yield scrapy.Request(L2,callback=self.parse_pageL2)

    def parse_pageL2(self,response):
        print "================L3============="
        
        item=AvlinkItem()
        
        labs=response.xpath("//script").extract()
        
#         print labs
        for url in labs:
            if url.find("var")>=0:
                pic=url.split('pic =')[1].split('"')[1].split("1.jpg")[0]
                print pic
                pre_video= pic.split("/")[-2]
                url="http://xz.av56.vip:88"+pic+"mp4/"+pre_video+".mp4"
                print url
                title=response.xpath("//title/text()").extract()[0]
                item['title']=title
                item['url']=url
                yield item
        
