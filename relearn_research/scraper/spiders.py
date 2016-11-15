# -*- coding: utf-8 -*-
from dynamic_scraper.spiders.django_spider import DjangoSpider
from relearn_research.models import Website, Information, InformationItem


class InformationSpider(DjangoSpider):

    name = 'information_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Website, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.link
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Information
        self.scraped_obj_item_class = InformationItem
        super(InformationSpider, self).__init__(self, *args, **kwargs)
