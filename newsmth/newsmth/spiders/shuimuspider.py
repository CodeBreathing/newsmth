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
                 # +[rooturl +"/nForum/channel/" +str(n) for n in range(1,6)
                 #    ]+['http://www.newsmth.net/nForum/section/ADAgents',
                 #     'http://www.newsmth.net/nForum/section/Estate',
                 #     'http://www.newsmth.net/nForum/section/SecondHand',
                 #     'http://www.newsmth.net/nForum/section/Wealth']+[
                 #    #二级菜单
                 #    'http://www.newsmth.net/nForum/section/Association',
                 #    'http://www.newsmth.net/nForum/section/THU',
                 #    'http://www.newsmth.net/nForum/section/JokeWorld',
                 #    'http://www.newsmth.net/nForum/section/Pictures',
                 #    'http://www.newsmth.net/nForum/section/Stars',
                 #    'http://www.newsmth.net/nForum/section/Basketball',
                 #    'http://www.newsmth.net/nForum/section/FansClub',
                 #    'http://www.newsmth.net/nForum/section/AbroadStudy',
                 #    'http://www.newsmth.net/nForum/section/Job',
                 #    'http://www.newsmth.net/nForum/section/Travels',
                 #    'http://www.newsmth.net/nForum/section/Automobile',
                 #    'http://www.newsmth.net/nForum/section/Coupons',
                 #    'http://www.newsmth.net/nForum/section/Military',
                 #    'http://www.newsmth.net/nForum/section/SmartLife',
                 #    #终止版面，价值待定
                 #    'http://www.newsmth.net/nForum/section/Closed',
                 #    'http://www.newsmth.net/nForum/section/Disused',
                 #    'http://www.newsmth.net/nForum/section/Merged',
                 #    'http://www.newsmth.net/nForum/section/Removed',
                 #    #频道推荐/电脑数码里面的二级菜单
                 #    'http://www.newsmth.net/nForum/section/SmartLife']
    #在这一层处理目录，抓取目录里面所有的版面首页
    def parse(self, response):
        selector = Selector(response)
        board = selector.xpath("//a/@href[contains(.,'nForum/board/')]").extract()

        for boardlist in board:
            boardurl = "http://www.newsmth.net" + boardlist
            yield Request(boardurl, callback=self.parse_getpage)
    #第二层输入版面首页地址，输出可用的每一页地址
    def parse_getpage(self, response):
        selector =Selector(response)
        #在这里抓第一页的各个标题链接
        # article = selector.xpath("//a/@href[contains(.,'nForum/article/')]").extract()
        # for list in article:
        #     print list
        #有5页的话抓5页,没有的话不往下抓
        for n in range(2,6):
            page = response.url + "?p="+str(n)
            toparticle=selector.xpath("//a/@href[contains(.,'nForum/article/')]").extract()[0]
            yield Request(page, callback=self.parse_list,meta={'toparticle':toparticle})


    #第三层：抓取所有可用页数的article
    def parse_list(self, response):
        selector=Selector(response)
        #抓取所有文章标题
        article = selector.xpath("//a/@href[contains(.,'nForum/article/')]").extract()[0]
        if article !=response.meta['toparticle']:
            article = selector.xpath("//a/@href[contains(.,'nForum/article/')]").extract()
            for list in article:
                print list
                #yield Request(list, )








