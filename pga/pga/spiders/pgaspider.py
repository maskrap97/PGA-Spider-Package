import scrapy

class pgaspider(scrapy.Spider):
    name = "pga-clubs"
    start_urls = [
            'https://www.pgatoursuperstore.com/golf-clubs/irons-sets/?sz=156'
        ]
    allowed_domains = ['https://www.pgatoursuperstore.com']

    def parse(self, response):
        yield {
            'name': response.css('h1.product-name::text').get(),
            'brand': response.css('div.product-brand::text').get(),
            'price': response.css('div.bfx-price::text').get()
            }

        next_page = response.css('a.name-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)