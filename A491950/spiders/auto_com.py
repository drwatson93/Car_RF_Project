from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Auto(BasePortiaSpider):
    name = "www.auto.com"
    allowed_domains = [u'www.auto.com']
    start_urls = [
        u'https://www.auto.com/cars-for-sale/miami-fl/ford-mustang?range=30&zc=33126']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'range=30', u'ford-mustang'),
                deny=(u'es')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.page-content',
                [
                    Field(
                        u'title',
                        '.headline > div > h1 *::text',
                        []),
                    Field(
                        u'price',
                        '.headline > div > .headline-subhead > span:nth-child(1) > strong *::text',
                        []),
                    Field(
                        u'miles',
                        '.headline > div > .headline-subhead > span:nth-child(2) > strong *::text',
                        []),
                    Field(
                        u'pic',
                        '.container > .vehicle-details-container > .primary-images > .right-column > .vehicle-photo-carousel-container > .gallery > .img-live > .carousel-inner > .active > img::attr(src)',
                        []),
                    Field(
                        u'body',
                        '.container > .vehicle-details-container > .vehicle-main-details > ul > li:nth-child(6) > .value *::text',
                        []),
                    Field(
                        u'stock_num',
                        '.container > .vehicle-details-container > .vehicle-main-details > ul > li:nth-child(8) > .value *::text',
                        [])])]]
