# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os
import re
from carmudiscraper.items import CarmudiscraperItem

class ImagecarmudispiderSpider(scrapy.Spider):
    name = 'imagecarmudispider'
    #allowed_domains = ['https://www.carmudi.co.id']
    start_urls = []
    list_car = pd.read_csv('list_car.csv')
    for i in range(0,len(list_car)):
        list_temp = list_car["list_car"][i].split(",")
        for j in range(0,len(list_temp)):
            start_urls.append('http://www.carmudi.co.id'+str(list_temp[j]))

    def parse(self, response):
        try:
            LIST_IMAGE = '//*[@id="main-content-container"]/div[1]/div[1]/div[1]/div[2]/div[6]'
            #print(response.xpath(LIST_IMAGE).extract())
            res = response.xpath(LIST_IMAGE).extract()
            res_new = res[0].split('</div>')
            for item in res_new:
                m = re.search('//(.+?).jpg',item)
                if m:
                    found = m.group(1)
                    yield CarmudiscraperItem(file_urls=str(found)+".jpg")
        except:
            LIST_IMAGE = '//*[@id="main-content-container"]/div[1]/div[1]/div[1]/div[2]/div[5]'
            #print(response.xpath(LIST_IMAGE).extract())
            res = response.xpath(LIST_IMAGE).extract()
            res_new = res[0].split('</div>')
            for item in res_new:
                m = re.search('//(.+?).jpg',item)
                if m:
                    found = m.group(1)
                    print(found)
                    yield CarmudiscraperItem(image_urls=str(found)+".jpg")
