# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:32:06 2019

@author: Byron
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:05:08 2019

@author: 15308
"""

import bs4 as bs
import time
import requests
import pandas as pd
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime as dt

#path =  r"D:\Dropbox\Dropbox\3. PK & SK\3.6 HKU MFIN\Course\2.MFIN 7033 Advanced Programming\Other Packages\web_scraping\chromedriver.exe"
path =  r"C:\Users\15308\Desktop\HKU\ADFP\Python\chromedriver.exe"

def NLP():

    browser = webdriver.Chrome(executable_path=path)
    browser.maximize_window()
    for j in range(2,139):
        url_form = 'https://edition.cnn.com/search/?q=trade%20war&size=30&sort=newest&page={}&from={}'
        url = url_form.format(str(j),str(30*(j-1)))
        browser.get(url)
        alls = browser.find_elements_by_xpath('//div[@class="cnn-search__result-contents"]')
        for al in alls:
            links.append(al.find_elements_by_xpath('.//h3[@class="cnn-search__result-headline"]/a')[0].get_attribute("href"))
            headlines.append(al.find_elements_by_xpath('.//h3[@class="cnn-search__result-headline"]/a')[0].text)
            dates.append(al.find_elements_by_xpath(".//div[@class = 'cnn-search__result-publish-date']")[0].text)
            contents.append(al.find_elements_by_xpath('.//div[@class="cnn-search__result-body"]')[0].text)
#            Next = browser.find_elements_by_xpath("//a[@class = 'pagination-arrow pagination-arrow-right cnnSearchPageLink text-active']")
#            Next[0].click()
            
    return alls

#def webpage_content(browser,url):
#    content = []
#    browser.get(url)
#    arl_alls = browser.find_elements_by_xpath('//div[@class="l-container"]')
#    for arl in arl_alls:
#        content.append(arl.text)
#        
#    content_text = ' '.join(content)
#    return content_text

if __name__ == '__main__':
    url_form = 'https://edition.cnn.com/search/?q=trade%20war&size=30&sort=newest&page={}'
    headlines = []
    links = []
    dates=[]
    date_new = []
    contents = []
    alls = NLP()
    for date in dates:
        date_new.append(dt.datetime.strptime(date,'%b %d, %Y').strftime('%Y-%m-%d'))
    df = pd.DataFrame()
    df['headline'] = headlines
    df['link'] = links
    df['content'] = contents
    df.index = date_new
    writer = pd.ExcelWriter(r'C:\Users\15308\Desktop\NLP\result.xlsx')
    df.to_excel(writer)
    writer.save()
 for time3 in time2:
    time_new.append(dt.datetime.strptime(time3[-len(time3):-7],'%b %d, %Y %H:%M').strftime('%Y-%m-%d'))
'''
    browser = webdriver.Chrome(executable_path=path)
    browser.maximize_window()
    browser.get('https://www.ft.com/search?q=trade+war')
    alls = browser.find_elements_by_xpath("//header[@id = 'site-navigation']/nav/div/ul/li/a[@class = 'o-header__nav-link']")
    alls[0].click()
    user_submit = browser.find_elements_by_xpath("//input[@pattern = '\S+@\S+']")
    user_submit[0].send_keys(username)
    Next = browser.find_elements_by_xpath("//button[@id = 'enter-email-next']")
    Next[0].click()
    pass_submit = browser.find_elements_by_xpath("//input[@name = 'password']")
    pass_submit[0].send_keys(password)
    Sign = browser.find_elements_by_xpath("//button[@data-sitekey = '6LfOqTcUAAAAAJsKpZPxujuUf3aSmncO6EA9ENg-']")
    Sign[0].click()
'''