import scrapy

# NB: This doesn't work, since the site doesn't like crawlers

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
class GuitarsSpider(scrapy.Spider):
    name = "guitars"

    def start_requests(self):
        yield scrapy.Request(url="https://www.guitar-list.com/find", callback=self.parse_brands, headers={"User-Agent": USER_AGENT})
        yield scrapy.Request(url="https://www.guitar-list.com/brandname/3092", callback=self.parse_brands, headers={"User-Agent": USER_AGENT})

    def parse_brands(self, response):
        import pdb; pdb.set_trace()
        for brand_option in response.xpath('//select[@id="edit-jump"]//option').getall():
            value = brand_option.attrib['value']
            if not value:
                continue

