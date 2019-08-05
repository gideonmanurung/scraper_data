# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os
import re
from skimage import io
import cv2

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
        LIST_IMAGE = '//*[@id="main-content-container"]/div[1]/div[1]/div[1]/div[3]/div[2]'
        #print(response.xpath(LIST_IMAGE).extract())
        res = response.xpath(LIST_IMAGE).extract()
        res_new = res[0].split('</div>')
        for item in res_new:
            m = re.search('//(.+?).jpg',item)
            if m:
                found = m.group(1)
                image = io.imread(str(found)+".jpg")
                cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                cv2.imwrite(str(found)+".jpg",image)
