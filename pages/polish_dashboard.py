from pages.base_page import BasePage

class PolishDashboard(BasePage):
    main_page_xpath = "//*[text()='Strona główna']"
    polish_page_url = "https://scouts-test.futbolkolektyw.pl/pl"

    def page_url(self):
        self.wait_for_element_to_be_visible(self.main_page_xpath)
        assert self.driver.current_url == self.polish_page_url