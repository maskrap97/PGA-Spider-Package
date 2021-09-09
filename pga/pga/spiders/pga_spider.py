import scrapy

class pgaspider(scrapy.Spider):
    name = "pga-clubs"

    def start_requests(self):
        urls = [
            'https://www.pgatoursuperstore.com/launcher-uhx-iron-set-w%2F-steel-shafts/2000000008506.html?cgid=golf-clubs-ironsets#sz=24&start=1',
            'https://www.pgatoursuperstore.com/sim2-max-irons-w%2F-steel-shafts/2000000018854.html?cgid=golf-clubs-ironsets#sz=36&start=1'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        yield {
            'name': response.css('h1.product-name::text').get(),
            'brand': response.css('div.product-brand::text').get(),
            'price': response.css('div.bfx-price::text').get()
            }

        next_page = response.css('something').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)