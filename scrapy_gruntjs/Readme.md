# gruntjs爬虫

------

##1 安装scrapy
```
pip install scrapy
```

##2 创建工程
```
scrapy startproject gruntjs
```

创建工程后进入spider目录下,新建gruntspider.py
```python
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
        #下载html
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
```
GruntSpider继承CrawlSpider, CrawSpider它是Spider的派生类，首先在说下Spider，它是所有爬虫的基类，对于它的设计原则是只爬取start_url列表中的网页，根据rules中的规则爬取的网页中获取link并继续爬取的工作CrawlSpider类更适合。
图片下载使用了Scrapy自带的ImagePipeLine，由于自带的pipeline不能保存原来的名称，所以对ImagePipeLine继承改写filepath方法

ImageItem
```python
import scrapy

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
```
ImagePipeLine
```python
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return '%s' % (image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
```

最后在setting.py中设置PipeLine和图片保存位置
```python
import os
ITEM_PIPELINES = {
    'gruntjs.pipelines.MyImagesPipeline': 300,
}

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_STORE = os.path.join(CUR_DIR, '..', 'images')
IMAGES_URLS_FIELD = 'image_urls'
IMAGES_RESULT_FIELD = 'images'
```

