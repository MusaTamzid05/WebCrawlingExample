from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

import time



class ProductParser:
    def __init__(self, driver, target_url,  src_url= "https://shop.adidas.jp"):
        self.driver = driver
        self.driver.get(target_url)
        self.src_url = src_url

    def parse(self):
        print("parsing data")
        parse_data = {}
        
        image_urls = self.get_image_urls()

        parse_data["image_urls"] = image_urls



        breadcrumb_categories = self.get_breadcrumb_categories()
      
        parse_data["breadcrumb_categories"] = breadcrumb_categories

        sizes = self.get_sizes()
        parse_data["sizes"] = sizes


        title_prices = self.get_title_and_price()
        parse_data["title_prices"] = title_prices
        self.driver.execute_script('window.scrollBy(0, 1200)') 
        time.sleep(0.5)

        coordinates = self.get_coordinates()
        parse_data["coordinates"] = coordinates


        inner_data = self.get_inner_data()
        parse_data["inner_data"] = inner_data

        

        chart_size = self.get_chart_size()
        parse_data["chart_size"] = chart_size

        tags = self.get_tags()
        parse_data["tags"] = tags

    

        ratting = self.get_rattings()

        if len(ratting) == 0:
            return parse_data

        reviews = self.get_user_reviews()
        parse_data["reviews"] = reviews

        scene_of_conforts = self.get_sence_of_comfort()
        parse_data["scene_of_comforts"] = scene_of_conforts

        return parse_data
        
            

    def get_image_urls(self):
        bs_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        image_container = bs_obj.select(".article_image_wrapper")[0]

        image_obj = image_container.select(".test-image")
        image_urls  = []
    
        for row_obj in image_obj:
            if "static" in row_obj["src"]:
                continue
            image_urls.append(self.src_url + row_obj["src"])
    
        return image_urls

    def get_breadcrumb_categories(self):
        
        bs_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        breadcrumb_obj  = bs_obj.select(".breadcrumb_wrap")[0]
        breadcrumb_items_obj  = breadcrumb_obj.select(".breadcrumbListItem")
        results = []
        
        for index, row in enumerate(breadcrumb_items_obj):
            if index == 0:
                continue
            results.append(row.select("a")[0].text)
            
        return "   /   ".join(results)
        
    def get_sizes(self):
        
        sizes = []
        bs_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        article_obj = bs_obj.select(".articlePurchaseBox")[0]
        article_name = article_obj.select(".articleNameHeader > .groupName")[0].text
        print(f"Article name {article_name}")
        article_size_obj = article_obj.select(".sizeSelectorListItem")
        
        for row in article_size_obj:
            sizes.append(row.text)
    
        return sizes

    def get_title_and_price(self):
        result = {}
        bs_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        article_obj = bs_obj.select(".articlePurchaseBox")[0]
        title_obj = article_obj.select(".itemTitle")[0]
        result["title"] = title_obj.text
    
        price_obj = article_obj.select(".price-value")[0]
        result["price"] = price_obj.text
        
        return result
    
    def get_coordinates(self):
        coordinate_dr = None
        
        try:

            coordinate_dr = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".coordinate_box")))
            #coordinate_dr = self.driver.find_element(By.CSS_SELECTOR, ".coordinate_box")
        except TimeoutException:
            print("No coordinates")
            return []
        

        coordinate_list_items_dr = coordinate_dr.find_elements(By.CSS_SELECTOR, ".carouselListitem")
        coordinates  = []
        
        for coordinate_list_item_dr in coordinate_list_items_dr:
            coordinate_button_dr = coordinate_list_item_dr.find_element(By.CSS_SELECTOR, ".coordinate_item_tile")
            
            coordinate_button_dr.click()
            
    
            info = {}
          
        

            time.sleep(1.0)
            parser = BeautifulSoup(self.driver.page_source, "html.parser")
            selected_obj  = parser.select(".coordinate_item_container")[0]
            url_obj = selected_obj.select(".test-link_a")[0]
            info["url"] = url_obj["href"]
            #time.sleep(0.5)
        
            image_obj = url_obj.select(".coordinate_item_image")[0]
            info["image_url"] = image_obj["src"]
            title_obj = selected_obj.select(".title")[0]
            info["title"] = title_obj.text
            price_obj = selected_obj.select(".price-value")[0]
            info["price"] = price_obj.text
        
            coordinates.append(info)
        
            coordinate_button_dr.click()
            time.sleep(0.2)
        
        return coordinates


    def get_inner_data(self):
        result = {}
        bs_obj = BeautifulSoup(self.driver.page_source, "html.parser")
    
        inner_obj = bs_obj.select(".inner")[0]
        inner_description = inner_obj.select(".description_part")[0].text
        
        #print(iner_description)
        result["description"] = inner_description
        
        heading_obj = inner_obj.select(".heading.itemFeature")[0]
        heading = heading_obj.text
       
        result["heading"] = heading
        
        inner_articles_obj  = inner_obj.select(".articleFeaturesItem")
        
        inner_articles = []
        
        for inner_article_obj in inner_articles_obj:
            inner_articles.append(inner_article_obj.text)
    
        result["points"] = inner_articles
    
        return result

    def get_chart_size(self):

        self.driver.execute_script('window.scrollBy(0, 500)') 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-zn7duo")))

        bs_chart_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        chart_root_obj = bs_chart_obj.select(".css-zn7duo")[0]
        #print(chart_root_obj)
        #chart_obj = chat_root_obj.select(".sizeChartTRow")
        chart_des_obj = chart_root_obj.select(".sizeDescription")[0]
        chart_cell_objs = chart_des_obj.select(".sizeChartTCell")
        
        headers = []
        
        for chart_cell_obj in chart_cell_objs:
            text = chart_cell_obj.text
            if len(text) > 3:
                break
            headers.append(text)
            
        #index = 6
        header_index = 0
        row = {}
        size_data = []
        for i in range(len(headers), len(chart_cell_objs)):
            row[headers[header_index]] = chart_cell_objs[i].text
        
            if len(row) == len(headers):
                size_data.append(row)
                row ={}
                header_index = 0
                continue
            header_index += 1
        
        
        
        
        
        size_header_obj = chart_des_obj.select(".sizeChartTHeader")[0]
        size_header_row_obj = size_header_obj.select(".sizeChartTRow")
        
        size_headers = []
        for row_header in size_header_row_obj:
            if len(row_header.text) == 0:
                continue
            size_headers.append(row_header.text)
        
        
        chart_size_dict = {}
        
        for i in range(len(size_headers)):
            chart_size_dict[size_headers[i]] = size_data[i]
        
        
        return chart_size_dict

    def get_rattings(self):
        
        info = {}

        try:
            
            
            review_score_obj = BeautifulSoup(self.driver.page_source, "html.parser")
            number_obj = review_score_obj.select(".BVRRRatingNormalOutOf")[0]
            info["user_ratting"] = number_obj.select(".BVRRNumber")[0].text
            info["user_text"] = review_score_obj.select(".BVRRBuyAgainTotal")[0].text
            info["perentage"] = review_score_obj.select(".BVRRBuyAgainPercentage")[0].text
            return info
            
        except IndexError:
            print("No ratting")

        return info

    def get_user_reviews(self):
        reviews = []
    
        review_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        review_obs = review_obj.select(".BVRRReviewDisplayStyle5")
        
        
        for review_ob in review_obs:
            info = {}
            current_ob = review_ob.select(".BVRRRatingNormalImage")[0]
            image_obj = current_ob.select("img")[0]
            info["title"] = image_obj["title"]
            info["title"] = review_ob.select(".BVRRReviewTitle")[0].text
            info["text"]  = review_ob.select(".BVRRReviewText")[0].text
            info["username"] = review_ob.select(".BVRRNickname")[0].text
            info["date"] = review_ob.select(".BVRRReviewDate")[0].text
            reviews.append(info)
            
        return reviews

    def get_sence_of_comfort(self):
        
        ratting_obj = BeautifulSoup(self.driver.page_source, "html.parser")
        radio_objs = ratting_obj.select(".BVRRRatingContainerRadio")[0]
        radio_obs = radio_objs.select(".BVRRRating")
    
        results = []
        
        for radio_ob in radio_obs:
            info = {}
            label_obs = radio_ob.select(".BVRRLabel")
            info["min"] = label_obs[0].text
            info["max"] = label_obs[1].text
            image_container_obj = radio_ob.select(".BVRRRatingRadioImage")[0]
            image_obj = image_container_obj.select("img")[0]
            info["title"] = image_obj["title"]
    
            results.append(info)
            
        return results
    
    def get_tags(self):
        tags = []
        main_page = BeautifulSoup(self.driver.page_source, "html.parser")
        tag_container = main_page.select(".itemTagsPosition")[0]
        tag_objs = tag_container.select(".inner")[0].select("a")
        
        for tag_obj in tag_objs:
            tags.append(tag_obj.text)

        return tags


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()

    urls = [
            "https://shop.adidas.jp/products/IA4846/",
            "https://shop.adidas.jp/products/IU2341/"
            ]

    for url in urls:
        parser = ProductParser(driver=driver, target_url= url)
        data = parser.parse()
        print(data)
    
       
