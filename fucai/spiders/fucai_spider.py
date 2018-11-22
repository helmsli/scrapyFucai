# encoding=utf8
import scrapy


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

        div=response.xpath('.//div[@class="lott_cont"]')
        print div
        print "table:"
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[1]/th[1]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[1]/th[2]/text()'))

        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[1]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[2]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[3]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[4]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[5]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[6]/text()'))
        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td[7]/text()'))

        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[1]/th/text()').extract())

        print(response.xpath('//div[@class="lott_cont"]/table[1]/tr[2]/td/text()').extract())
        print "table1:"
        atable = response.xpath('//*[@id="lottery_tabs"]/div/table[1]')
        print atable
        print"table2:"
        print response.xpath('//*[@id="lottery_tabs"]/div/table[1]/tbody/tr[1]/td[1]')
        content = response.xpath('//table[@border="1"]/tr[2]/td/text()').extract()

        with open('lottery','wb') as f:
            lott_cont_div=response.xpath('.//div[@class="lott_cont"]/text()').extract()
            for result in lott_cont_div:
                print 'result:' + result +":end"
                f.write(result)
                break
        '''
        print response.body
        print "body:*****************"
        # print response.xpath('body')
        '''