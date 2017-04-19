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
                  ]+[rooturl +"/nForm/channel/" +str(n) for n in range(1,6)
                    ]+['http://www.newsmth.net/nForum/section/ADAgents',
                     'http://www.newsmth.net/nForum/section/Estate',
                     'http://www.newsmth.net/nForum/section/SecondHand',
                     'http://www.newsmth.net/nForum/section/Wealth']+[
                    #二级菜单
                    'http://www.newsmth.net/nForum/section/Association',
                    'http://www.newsmth.net/nForum/section/THU',
                    'http://www.newsmth.net/nForum/section/JokeWorld',
                    'http://www.newsmth.net/nForum/section/Pictures',
                    'http://www.newsmth.net/nForum/section/Stars',
                    'http://www.newsmth.net/nForum/section/Basketball',
                    'http://www.newsmth.net/nForum/section/FansClub',
                    'http://www.newsmth.net/nForum/section/AbroadStudy',
                    'http://www.newsmth.net/nForum/section/Job',
                    'http://www.newsmth.net/nForum/section/Travels',
                    'http://www.newsmth.net/nForum/section/Automobile',
                    'http://www.newsmth.net/nForum/section/Coupons',
                    'http://www.newsmth.net/nForum/section/Military',
                    'http://www.newsmth.net/nForum/section/SmartLife',
                    #终止版面，价值待定
                    'http://www.newsmth.net/nForum/section/Closed',
                    'http://www.newsmth.net/nForum/section/Disused',
                    'http://www.newsmth.net/nForum/section/Merged',
                    'http://www.newsmth.net/nForum/section/Removed',
                    #频道推荐/电脑数码里面的二级菜单
                    'http://www.newsmth.net/nForum/section/SmartLife']

    def parse(self, response):
        selector = Selector(response)
        board = selector.xpath("//a/@href[contains(.,'nForum/board/')]").extract()
        i =1
        for boardlist in board:
            i= i+1
            print boardlist
        print i




