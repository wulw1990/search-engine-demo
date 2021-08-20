import os
import scrapy
from mySpider.items import ItcastItem
from bs4 import BeautifulSoup

keywords = ['开发',
            '系统',
            '教育',
            '政策',
            '国务院',
            '政府',
            '服务',
            '程序',
            '开源',
            '数据库',
            '资讯',
            '中国',
            '美国',
            '试题',
            '考试',
            '数学',
            '地理',
            '语文',
            '教材',
            '历史',
            '人物',
            '中华',
            '展览',
            '美术',
            '音乐'
            ]

class ItcastSpider(scrapy.Spider):
    name = 'itcast'

    def start_requests(self):
        urls = [
            'http://www.itcast.cn/',
            'http://www.gov.cn/',
            'https://www.csdn.net/',
            'https://www.ifeng.com/',
            'https://sx.zxxk.com/',
            'https://dl.zxxk.com/',
            'https://www.pep.com.cn/czyw/',
            'https://www.jianglishi.cn/',
            'http://www.namoc.org/',
            'https://music.taihe.com/'

        ]
        for i in urls:
             yield scrapy.Request(url = i, callback=self.parse)

    def parse(self, response):
        print()
        print()
        print()
        print('parse url:', response.url)
        freq = {}
        for word in keywords:
            freq[word] = response.body.decode('utf-8').count(word)
        # items = []
        # item = ItcastItem()
        # item['url'] = response.url
        # item['freq'] = freq
        # # item['freq'] = 'xxxx'
        # items.append(item)
        # return items

        item = {
            'url': response.url,
            'freq': freq,
        }
        yield item

    #     html = response.body
    #     soup = BeautifulSoup(html,'html5lib')
    #     for link in soup.findAll('a'):
    #         link = link.get('href')
    #         if not link.startswith(response.url):
    #             link = os.path.join(response.url, link)
    #         yield scrapy.Request(link, callback=self.parse_item)

    # def parse_item(self,response):
    #     freq = {}
    #     for word in keywords:
    #         freq[word] = response.body.decode('utf-8').count(word)
    #     items = []
    #     item = ItcastItem()
    #     item['url'] = response.url
    #     item['freq'] = freq
    #     items.append(item)

    #     yield items
