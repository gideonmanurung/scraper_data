# -*- coding: utf-8 -*-
import scrapy
import csv


class CarmudispiderSpider(scrapy.Spider):
    name = 'carmudispider'
    # allowed_domains = ['https://www.carmudi.co.id/cars/condition:all/?page=2']
    start_urls = []
    for i in range(1,1083):
        start_urls.append("https://www.carmudi.co.id/cars/condition:all/?page="+str(i))

    def parse(self, response):
        LIST_SELECTOR = '//*[@id="catalog-index"]/section/section/div/div/div/div[1]/div/div/a/@href'
        """
        yield {
            'list_car': response.xpath(LIST_SELECTOR).extract(),
        }
        """
        with open('people.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            for car_path in response.xpath(LIST_SELECTOR).extract():
                writer.writerows(car_path)
