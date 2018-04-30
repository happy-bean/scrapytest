#!/usr/bin/python
# -*- coding: UTF-8 -*-


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#从优信二手车
from scrapytest.items import Car


class DmozSpider(CrawlSpider):
    name = "scrapytest"

    allowed_domains = ["www.xin.com"]


    start_urls = [
        "http://www.xin.com/beijing/sitemap.html",
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'http://www.xin.com/((?!\/)\w)+?/s/$', r'http://www.xin.com/((?!\/)\w)+?/$'))),
        Rule(LinkExtractor(allow=(r'http://www.xin.com/((?!\/)\w)+?/sn_p\d{0,2}-\d{0,2}/i\d+?/$',))),
        Rule(LinkExtractor(allow=(r'http://www.xin.com/((?!\/)\w)+?/i\d+?/$',))),
        Rule(LinkExtractor(allow=(r'http://www.xin.com/((?!\/)\w)+?/sn_p\d{0,2}-\d{0,2}/$',))),
        Rule(LinkExtractor(allow=(r'http://www.xin.com/cw_sh\d{10}/$',))),
        Rule(LinkExtractor(allow=(r'http://www.xin.com/((?!\/)\w)+?/che\d+?\.html',)), callback='parse_item'),
    )

    def parse_item(self, response):
        car = Car()
        car["title"] = response.xpath('//span[@class="cd_m_h_tit"]/text()').extract_first().replace("\n", "").strip()
