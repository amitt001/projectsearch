from scrapy.contrib.djangoitem import DjangoItem
from myapp.models import Crawl

class Website(DjangoItem):
    django_model = Crawl