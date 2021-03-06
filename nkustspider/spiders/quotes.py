import scrapy
from nkustspider.items import NkustspiderItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        target = response.css("body > div > div:nth-child(2) > div.col-md-8 > div")
        for t in target:
            data = NkustspiderItem()
            data['quote'] = t.css("span.text::text").extract_first()
            data['author'] = t.css("span small.author::text").extract_first()
            author_desc_link = response.urljoin(t.css("a::attr(href)").extract_first())
            yield scrapy.Request(author_desc_link, meta={"data": data}, callback=self.parse_author)
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        data = response.meta["data"]
        data['birthday'] = response.css("span.author-born-date::text").extract_first()
        data['bornplace'] = response.css("span.author-born-location::text").extract_first()
        return data