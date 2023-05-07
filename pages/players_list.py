import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PlayersList(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    download_csv_xpath = "//*[text()='Download CSV']"
    players_list_url = "https://scouts-test.futbolkolektyw.pl/en/players"

    def page_url(self):
        self.wait_for_element_to_be_clickable(self.main_page_xpath)
        assert self.driver.current_url == self.players_list_url
