import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from takasbank.items import Article


class TakasSpider(scrapy.Spider):
    name = 'takas'
    allowed_domains = ['takasbank.com.tr']
    start_urls = ['https://www.takasbank.com.tr/tr/duyurular?page=1']

    def parse(self, response):
        next_page = response.xpath('//a[@class="next"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse, dont_filter=True)
            yield response.follow(response.url, self.parse_page, dont_filter=True)

    def parse_page(self, response):
        articles = response.xpath('//div[@class="col-md-6"]')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = " ".join(article.xpath('.//div[@class="text"]//text()').getall()).strip()
            date = " ".join(article.xpath('.//div[@class="date"]//text()').getall()).strip()
            category = " ".join(article.xpath('.//div[@class="category"]//text()').getall()).strip()
            link = article.xpath('.//div[@class="text"]/a/@href').get()

            item.add_value('title', title)
            item.add_value('date', " ".join(date.split()))
            item.add_value('category', category)
            item.add_value('link', response.urljoin(link))

            return item.load_item()

