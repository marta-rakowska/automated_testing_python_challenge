import time

from pages.base_page import BasePage

class AddAPlayer(BasePage):
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*[@name='age']"
    leg_xpath = "//*[@name='leg']"
    club_xpath = "//*[@name='club']"
    level_xpath = "//*[@name='level']"
    main_position_xpath = "//*[@name='mainPosition']"
    second_position_xpath = "//*[@name='secondPosition']"
    achievements_xpath = "//*[@name='achievements']"
    add_language_xpath = "//*/div[2]/div/div[15]/button"
    languages_xpath = "//*/div[15]/div/div/div/input"
    remove_language_xpath = "//*[@title='Remove language']"
    laczy_nas_pilka_xpath = "//*[@name='webLaczy']"
    dziewiecdziesiat_minut_xpath = "//*[@name='web90']"
    facebook_xpath = "//*[@name='webFB']"
    add_link_to_youtube_xpath = "//*/div[2]/div/div[19]/button"
    link_to_youtube_xpath = "//*/form/div[2]/div/div[19]/div/div/div/input"
    remove_link_to_youtube_xpath = "//*/form/div[2]/div/div[19]/div/button"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"

    expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.age_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_leg(self, leg):
        self.field_send_keys(self.leg_xpath, leg)

    def type_in_club(self, club):
        self.field_send_keys(self.club_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_xpath, level)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_xpath, second_position)

    def click_district_menu(self):
        self.click_on_the_element(self.menu_district_xpath)

    def click_silesian_district_option(self):
        self.click_on_the_element(self.district_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_xpath, achievements)

    def click_add_language_button(self):
        self.click_on_the_element(self.add_language_xpath)
    def type_in_languages(self, languages):
        self.field_send_keys(self.languages_xpath, languages)

    def click_remove_language_button(self):
        self.click_on_the_element(self.remove_language_xpath)

    def type_in_laczy_nas_pilka(self, laczy_nas_pilka):
        self.field_send_keys(self.laczy_nas_pilka_xpath, laczy_nas_pilka)

    def type_in_dziewiecdziesiat_minut(self, dziewiecdziesiat_minut):
        self.field_send_keys(self.dziewiecdziesiat_minut_xpath, dziewiecdziesiat_minut)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_xpath, facebook)

    def click_add_link_to_youtube_button(self):
        self.click_on_the_element(self.add_link_to_youtube_xpath)

    def type_in_link_to_youtube(self, link_to_youtube):
        self.field_send_keys(self.link_to_youtube_xpath, link_to_youtube)

    def click_remove_link_to_youtube_button(self):
        self.click_on_the_element(self.remove_link_to_youtube_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_xpath)

    def click_clear_button(self):
        self.click_on_the_element(self.clear_xpath)
