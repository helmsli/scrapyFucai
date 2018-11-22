# encoding=utf8
import scrapy
from fucai.items import FucaiItem

class FucaiSpider(scrapy.Spider):
    name = "fucai"
    allowed_domains = ["bwlc.net"]
    start_urls = [
        "http://www.bwlc.net/bulletin/slto.html"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        print "*********************"


        #获取双色球开奖中的头信息，表明是红球号码还是蓝球号码
        shuangseqiuTableTr1 = response.xpath('//div[@class="lott_cont"]/table[1]/tr[1]/th/text()').extract()
        shuangseqiuTableTr2 = response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td/text()').extract()
        item=FucaiItem()
        ballStartWithRed = False
        ballList = shuangseqiuTableTr1
        print(type(ballList))
        print( len(shuangseqiuTableTr1))
        if len(shuangseqiuTableTr1)==2:

            ballList=shuangseqiuTableTr2
            if shuangseqiuTableTr1[0].find("红") >= 0:
                ballStartWithRed=True
            elif shuangseqiuTableTr1[0].find("蓝")>=0:
                ballStartWithRed = False
        elif  len(shuangseqiuTableTr2)==2:
            ballList = shuangseqiuTableTr1
            if shuangseqiuTableTr2[0].find("红") >= 0:
                ballStartWithRed = True
            elif shuangseqiuTableTr2[0].find("蓝") >= 0:
                ballStartWithRed = False
        print(len(ballList))
        print((ballList))

        if ballStartWithRed:
            item['redBall']=ballList[0:5]
            item['blueBall'] = ballList[5:7]
        else:
            item['redBall'] = ballList[2:7]
            item['blueBall'] = ballList[0:2]
        print(( item['redBall']))
        period = lott_cont_div=response.xpath('.//div[@class="lott_cont"]/text()').extract()
        print(period[0])
        item['period']=period[0]
        fileName = item['period'].strip()
        with open(fileName+'.txt','wb') as f:
            f.write("period:")
            f.write(item['period'].strip())
            f.write('\n')
            f.write("redBall:")
            for s in item['redBall']:
                f.write(s +',')
            f.write('\n')
            f.write("blueBall:")
            for s in item['blueBall']:
                f.write(s +',')

            f.write('\n')
        '''
        print response.body
        print "body:*****************"
        # print response.xpath('body')
        '''