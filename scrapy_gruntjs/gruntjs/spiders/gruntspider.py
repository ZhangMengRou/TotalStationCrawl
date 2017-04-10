
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from gruntjs.items import ImageItem


class GruntSpider(CrawlSpider):
    name = "grunt"
    allowed_domains = ['gruntjs.com']
    download_delay = 2

    start_urls = ['http://www.gruntjs.com/']

    rules = [Rule(LinkExtractor(allow=()), callback='parse_item', follow=True)]

    def parse_item(self, response):

        page = response.url[20:];
        page = page.replace('/', '_')
        with open("html/" + page + ".html", 'wb') as f:
            f.write(response.body)

        l = ItemLoader(item=ImageItem(), response=response)
        imgs = response.selector.xpath("//img/@src").extract()
        for img in imgs:
            if 'http' in img:
                l.add_value('image_urls', img)

            else:
                l.add_value('image_urls', response.urljoin(img))

        return l.load_item()