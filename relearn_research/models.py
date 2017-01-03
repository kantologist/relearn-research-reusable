from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.


@python_2_unicode_compatible
class Website(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime,
                                        blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Information(models.Model):
    title = models.CharField(max_length=200)
    website = models.ForeignKey(Website)
    description = models.TextField(blank=True)
    url = models.URLField()
    thumbnail = models.ImageField(blank=True)
    date = models.TextField(blank=True)
    checker_runtime = models.ForeignKey(SchedulerRuntime,
                                        blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class InformationItem(DjangoItem):
    django_model = Information


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):

    if isinstance(instance, Website):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()

    if isinstance(instance, Information):
            if instance.checker_runtime:
                instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)
