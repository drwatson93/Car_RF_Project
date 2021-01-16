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


class Cars(BasePortiaSpider):
    name = "www.cars.com"
    allowed_domains = [u'www.auto.com']
    start_urls = [
        u'https://www.auto.com/cars-for-sale/davie-fl/ford-mustang?per_page=15&sort=best_match&stc=used']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
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
                u'.css-1i2p757:nth-child(2)',
                [
                    Field(
                        u'img',
                        'a > .css-119z7e2 > .css-61pf4t > img::attr(src)',
                        []),
                    Field(
                        u'Title',
                        '.css-rx3zap > .css-1ma8s7p > .css-ipgzs2 *::text',
                        []),
                    Field(
                        u'Price',
                        '.css-rx3zap > .css-1ma8s7p > .listing-deal-price > .listing-price *::text',
                        []),
                    Field(
                        u'Miles',
                        '.css-rx3zap > .css-9p4c09 > .css-10p7a9u > .hideMoreDetails > li:nth-child(1) > span *::text',
                        []),
                    Field(
                        u'link',
                        '.css-rx3zap > .css-9p4c09 > .css-iv06io > .viewDetailsButtonDesktop > a::attr(href)',
                        [])])]]
