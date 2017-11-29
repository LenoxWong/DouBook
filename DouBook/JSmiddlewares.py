#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LenoxWong'


from scrapy.http import HtmlResponse

class PhantomJSDownloaderMiddleware(object):

    @classmethod
    def process_request(cls, request, spider):
        if spider.name == 'DB':
            __pt_driver__ = spider.__pt_driver__
            __pt_driver__.get(request.url)
            body = __pt_driver__.page_source
            return HtmlResponse(request.url, body=body, encoding='utf-8', request=request)
        else:
            return None
