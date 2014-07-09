# Scrapy settings for dirbot project
import sys
import os
sys.path.insert(0,'c:/python27/scraptest')

os.environ['DJANGO_SETTINGS_MODULE'] = 'scraptest.settings' 
SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'
     
ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1,
         			'dirbot.pipelines.DirbotPipeline': 1000,
         }

 

