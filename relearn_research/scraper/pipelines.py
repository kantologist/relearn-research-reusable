# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import logging
from django.db.utils import IntegrityError
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
#import psycopg2
#from sqlalchemy import create_engine
#from sqlalchemy.engine.url import URL
#from . import settings


class DjangoWriterPipeline(object):
#    def __init__(self):
#        self.connection = psycopg2.connect(host='localhost',
#                                            database='research',
#                                            user='kantologist',
#                                            password='murphy')

        #self.engine = create_engine(URL(**settings.DATABASE))
        #self.cursor = self.connection.cursor()

    def process_item(self, item, spider):

        if spider.conf['DO_ACTION']:

            try:
                item['website'] = spider.ref_object

                checker_rt = SchedulerRuntime(runtime_type='C')
                checker_rt.save()
                item['checker_runtime'] = checker_rt

                item.save()
                spider.action_successful = True
                spider.log("Item saved.", logging.INFO)

            except IntegrityError as e:
                spider.log(str(e), logging.ERROR)
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")
        else:
            if not item.is_valid():
                spider.log(str(item._errors), logging.ERROR)
                raise DropItem("Missing attribute.")

        return item