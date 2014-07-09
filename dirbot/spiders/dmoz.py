from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.selector import Selector

from dirbot.items import Website



class DmozSpider(CrawlSpider):
    name = "dmoz"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?page=26804&sort=newest"
    ]

    rules = (Rule (SgmlLinkExtractor(allow=(),restrict_xpaths=('//div[@class="pager fl"]/a[@rel="next"]')), callback="parse_items", follow= True),)
    def parse_items(self, response):
        CONCURRENT_REQUESTS = 100
        LOG_LEVEL = 'INFO'
        COOKIES_ENABLED = False
        RETRY_ENABLED = False
        DOWNLOAD_TIMEOUT = 1000
        REDIRECT_ENABLED = False
        AJAXCRAWL_ENABLED = True
        sel = Selector(response)
        sites = sel.xpath('//div[@class="summary"]')
        items = []
        x=0;
        for site in sites:           
            item= Website()
            item['url'] = site.xpath('//h3/a/@href').extract()[x].encode('ascii',errors='ignore')
            item['name'] = site.xpath('//h3/a/text()').extract()[x].encode('ascii',errors='ignore')
            item['description'] = site.xpath('//div[@class="excerpt"]/text()').extract()[x].encode('ascii',errors='ignore')
            items.append(item)
            x=x+1;
        return items

 
