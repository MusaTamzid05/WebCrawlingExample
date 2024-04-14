from selenium import webdriver
from lib.list_page_crawler import ListPageCrawler
from lib.data_saver import DataSaver


class Spider:
    def __init__(self):
        self.crawler_list = [
                    {
                        "url" :  "https://shop.adidas.jp/item/?gender=mens&category=wear&group=tops&type=t_shirts&condition=6",
                        "start_page_index" : 0,
                        "product_index" : 0

                    }
                ]
        self.page_crawler_driver =  webdriver.Chrome()
        self.page_crawler_driver.maximize_window()


    def start(self):

        parse_data_list = []

        try:
            for crawl_info in self.crawler_list:
                url = crawl_info["url"]
                start_page_index = crawl_info["start_page_index"]
                product_index = crawl_info["product_index"]

                list_crawler = ListPageCrawler(
                        url=url,
                        driver=self.page_crawler_driver,
                        page_index=start_page_index,
                        product_index=product_index
                        )
                parse_data_list += list_crawler.start()
        except Exception as e:
            print(f"Exception in Spider {e}")

        finally:
            print(f"Saving total data {len(parse_data_list)}")
            data_saver = DataSaver(data=parse_data_list)
            data_saver.start()
            
