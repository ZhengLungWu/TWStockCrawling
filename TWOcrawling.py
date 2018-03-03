#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 16:45:24 2018

@author: wuzhenglung
"""

from selenium import webdriver
#import selenium
#from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime



class Open_WebSite:
    def __init__(self):
        self.Stockurl='http://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html'
        self.OTCstockurl='http://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote.php?l=zh-tw'
        chromedriver='/Users/wuzhenglung/Desktop/stock_mac/chromedriver'
        self.driver=webdriver.Chrome(chromedriver)

        self.getTodayStock()
        self.getTodayOTC()
        self.driver.close()
        time.sleep(2)
        
        
        
    def getDailyStockinfo(self,datetime):
        self.driver.get(self.Stockurl)
        #selecttype=self.driver.find_element_by_xpath("//select[@name='selectType']")
        #print(selecttype.text)
        option=self.driver.find_element_by_xpath("//option[@value='ALLBUT0999']")
        #option.click()
        #print('---------------')
        #print(option.text)
        dateele=self.driver.find_element_by_xpath("//input[@name='qdate']")
        dateele.clear()
        dateele.send_keys(datetime)
        qu=self.driver.find_element_by_xpath("//input[@name='query-button']")
        qu.click()
        dwcsv=self.driver.find_element_by_xpath("//a[@class='csv']")
        dwcsv.click()
    def getTodayStock(self):
        self.driver.get(self.Stockurl)
        g=self.driver
        option=g.find_element_by_xpath("//option[@value='ALLBUT0999']")
        option.click()
        btn=g.find_element_by_xpath("//a[@class='button search']")
        btn.click()
        time.sleep(2)
        
        dwcsv=g.find_element_by_xpath("//a[@class='csv']")
        
        dwcsv.click()
        
        time.sleep(4)

    def getContinStockinfo(self):
        
        self.driver.get(self.Stockurl)
       
        option=self.driver.find_element_by_xpath("//option[@value='ALLBUT0999']")
        option.click()
        dateele=self.driver.find_element_by_xpath("//input[@name='qdate']")
        T=datetime.date.today()-datetime.timedelta(365)
        for i in range(90):
            T=T-datetime.timedelta(1)
            G=str(T)
            G=self.YMDConv(G)
            dateele.clear()
            dateele.send_keys(G)
            dwcsv=self.driver.find_element_by_xpath("//button[@class='dl-csv board']")
            dwcsv.click()
        
    def getDailyOTC(self,datetime):
        #self.driver.implicitly_wait(5)
        
        self.driver.get(self.OTCstockurl)
        #time.sleep(10)
        date=self.driver.find_element_by_xpath("//input[@id='input_date']")       
        date.clear()
        date.send_keys(u'\ue007')
        #
        date.clear()
        date.send_keys(datetime)
        date.send_keys(u'\ue007')
        '''
        actions=webdriver.ActionChains(self.driver)
        actions.move_to_element_with_offset(date,-150,-50)
        actions.click()
        actions.perform()
        '''
        
        #self.driver.implicitly_wait(5)
        time.sleep(5)
        dwcsv=self.driver.find_element_by_xpath("//button[@onclick='downloadCSV()']")
        dwcsv.click()
    def getTodayOTC(self):
        self.driver.get(self.OTCstockurl)
        time.sleep(2)
        dwcsv=self.driver.find_element_by_xpath("//button[@onclick='downloadCSV()']")
        dwcsv.click()
        time.sleep(3)
    
    def getContinOTC(self):
        self.driver.get(self.OTCstockurl)
        #time.sleep(10)
        date=self.driver.find_element_by_xpath("//input[@id='input_date']")       
        #date.clear()
        #date.send_keys(u'\ue007')
        #time.sleep(5)
        T=datetime.date.today()
        for i in range(23):
            T=T-datetime.timedelta(1)
            G=str(T)
            G=self.YMDConv(G)
            date.clear()
            date.send_keys(G)
            date.send_keys(u'\ue007') 
            time.sleep(1)
            
            dwcsv=self.driver.find_element_by_xpath("//button[@onclick='downloadCSV()']")
            dwcsv.click()
    def YMDConv(self,DateStr):
        G=DateStr
        if '2018' in G:
            G=G.replace('2018','107')
        elif '2017' in G:
            G=G.replace('2017','106')
        elif '2016' in G:
            G=G.replace('2016','105')
        G=G.replace('-','/')
        return G
        
        
        
if __name__ == "__main__":
    a=Open_WebSite()
    