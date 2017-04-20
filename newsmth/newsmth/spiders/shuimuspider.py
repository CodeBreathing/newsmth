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
            boardurl = "http://www.newsmth.net" + boardlist+"?ajax"
            yield Request(boardurl, callback=self.parse_list)
    #第二层输入版面首页地址，输出下一页地址
    def parse_list(self, response):
        selector =Selector(response)
        print response.body

        #抓文章内容
        # article = selector.xpath("//a/@href[contains(.,'nForum/article/')]").extract()
        # for art in article:
        #     art ="http://www.newsmth.net"+article
        #     yield Request()
        #处理分页(这样静态处理不行)
        # if "?p=" not in response.url:
        #     page =response.url+"?p="
            #pageurl = selector.xpath('//a/@href[contains(.,"' + page + '")]').extract()
            # for pagenum in pageurl:
            #     nextpage="http://www.newsmth.net"+ pagenum
            #     print nextpage

            #获取主题数







