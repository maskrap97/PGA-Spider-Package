import scrapy

class pgaspider(scrapy.Spider):
    name = "pga-clubs1"
    start_urls = [
            'https://www.pgatoursuperstore.com/golf-clubs/irons-sets/?sz=156'
        ]

    def __init__(self):
        self.declare_xpath()

    def declare_xpath(self):
        self.PlayerProfileXpath = '//li/a[contains(@id,"playerProfile")]'
        self.getAllItemsXpath = '//li/div/div[2]/div[2]/a'
        self.NameXpath = '//*[@id="pdpMain"]/div[1]/h1/text()'
        self.BrandXpath = '//*[@id="pdpMain"]/div[1]/div[1]/text()'
        self.PriceXpath = '//*[@id="display-price"]/text()'
        self.LoftXpath = '//*[@id="techSpecTabpanel"]/div/table[1]/tbody/tr[5]/td[2]/text()'

    def parse(self, response):
        for href in response.xpath(self.getAllItemsXpath):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url=url, callback=self.parse_category, dont_filter=True)
    
    def parse(self, response):
        yield {
            'name': response.css('h1.product-name::text').get(),
            'brand': response.css('div.product-brand::text').get(),
            'price': response.css('div.bfx-price::text').get()
            }