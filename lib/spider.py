from selenium import webdriver
from lib.list_page_crawler import ListPageCrawler


class Spider:
    def __init__(self):
        self. urls = ["https://shop.adidas.jp/item/?gender=mens&category=wear&group=tops&type=t_shirts&condition=6"]
        self.page_crawler_driver =  webdriver.Chrome()
        self.page_crawler_driver.maximize_window()


    def start(self):
       
        
        for url in self.urls:
            list_crawler = ListPageCrawler(url=url,
                                           driver=self.page_crawler_driver,
                                          )
            list_crawler.start()
            
