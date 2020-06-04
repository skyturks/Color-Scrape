import scrapy
import cssutils


class PantoneScrape(scrapy.Spider):
    name = "pantoneScrape"

    def start_requests(self):
        urls = [
            "http://www.novact.info/id40.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        colorCodes = []

        for index, item in enumerate(response.xpath('//*[@id="family"]/tbody/tr')):
            hexCode = response.xpath(
                '//*[@id="family"]/tbody/tr' + str([index]) + "/td[2]/font/text()"
            ).get()

            colorCodes.append("#" + str(hexCode))

        print(colorCodes)
