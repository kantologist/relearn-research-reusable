from __future__ import unicode_literals
from django.contrib import admin
from .models import Website, Information

# Register your models here.


class WebsiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'url_', 'scraper')
    list_diplay_link = ('name',)

    def url_(self, instance):
        return '<a href={url} target="_blank">{title}</a>'.format(url=instance.url,
                                                                  title=instance.url)
    url_.allow_tags = True


class InformationAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'website', 'date', 'url_')
    list_diplay_link = ('title',)
    raw_id_fields = ('checker_runtime',)

    def url_(self, instance):
        return'<a href={url} target="_blank"">{title}</a>'.format(url=instance.url,
                                                                  title=instance.url)
    url_.allow_tags = True


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Information, InformationAdmin)
