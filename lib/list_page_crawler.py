from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import time

from lib.product_parser import ProductParser

class ListPageCrawler:
    def __init__(self, url, driver, page_index, product_index):
        self.root_url = url
        self.driver = driver
        self.start_page_index = page_index
        self.start_product_index = product_index
      
    def start(self):
        page_index = self.start_page_index

        if page_index == 0:
            self.driver.get(self.root_url)
        else:
            self.driver.get(f"{self.root_url}&page={page_index + 1}")

        total_pages = int(self.driver.find_element(By.CSS_SELECTOR, ".pageTotal").text)


        last_page_index = total_pages - 1
        running = True
        product_driver = None
        results_data = []


        try:
            while running:

                if page_index == self.start_page_index:
                    index = self.start_product_index
                else:
                    index = 0
                print(f"Page index {page_index}, Product index {index}")
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".itemCardArea-cards.test-card")))
                
                links_dr = self.driver.find_elements(By.CSS_SELECTOR, ".itemCardArea-cards.test-card")

                
                while index < len(links_dr):
                    link_dr = links_dr[index]
                    
                    try:
                        image_dr = link_dr.find_element(By.CSS_SELECTOR, ".image_link.test-image_link")
                        link = image_dr.get_attribute("href")
                        print(f"page => {page_index}, product_index => {index} , link  => {link}")
                        
                        if product_driver is None:
                            product_driver = webdriver.Chrome()
                            product_driver.maximize_window()
                            
                        parser = ProductParser(target_url=link, driver=product_driver)
                        parse_data, skip = parser.parse()

                        if skip == True:
                            index += 1

                        for key, value in parse_data.items():
                            print(key)
                            print(value)
                            print("\n")


                        results_data.append(parse_data)
                        print("*" * 20)
                            
                    except NoSuchElementException :
                        self.driver.execute_script('window.scrollBy(0, 500)')
                        print("Scolling")
                        time.sleep(1.0)
                        continue
                        
                    index += 1
            
                page_index += 1
                
            
                if page_index <= last_page_index:
                    self.driver.execute_script('window.scrollBy(0, 1500)')
                    print("scooring to the end")
                    time.sleep(3.0)
                    
                    self.driver.get(f"{self.root_url}&page={page_index + 1}")
                else:
                    running = False


            return results_data

        except Exception as e:
            print(f"Exception in page crawler {e}")
            return results_data





if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    target_url = "https://shop.adidas.jp/item/?gender=mens&category=wear&group=tops&type=t_shirts&condition=6"

    page_crawler = ListPageCrawler(driver=driver, url=target_url)
    page_crawler.start()

