# -*-coding:utf8-*-

from scrapy.selector import Selector
from newsmth.items import NewsmthItem
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
import json


class newsmthSpider(CrawlSpider):

    name = "newsmth"
    rooturl ="http://www.newsmth.net"

    start_urls = [rooturl+"/nForum/section/"+str(m) for m in range(1,10)
                  ]


    def parse(self, response):
        selector = Selector(response)
        board = selector.xpath("//a/@href[contains(.,'nForum/board/')]").extract()
        i =1
        for boardlist in board:
            i= i+1
            print boardlist
        print i




