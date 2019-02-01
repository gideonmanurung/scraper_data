# -*- coding: utf-8 -*-
import scrapy
import pandas as pd


class ImagecarmudispiderSpider(scrapy.Spider):
    name = 'imagecarmudispider'
    #allowed_domains = ['https://www.carmudi.co.id']
    start_urls = []
    list_car = pd.read_csv('list_car.csv')
    for i in range(0,len(list_car)):
        list_temp = list_car["list_car"][i].split(",")
        for j in range(0,len(list_temp)):
            start_urls.append('https://www.carmudi.co.id'+str(list_temp[j]))

    def parse(self, response):
        LIST_IMAGE = '//*[@id="main-content-container"]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div'
        print(response.xpath(LIST_IMAGE))
