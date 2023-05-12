import os
import unittest
import time
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player_form import AddAPlayer


class TestClearAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_clear_add_a_player_form(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_a_player_button()
        add_a_player = AddAPlayer(self.driver)
        add_a_player.type_in_email('jan.kowalski@jk.com')
        add_a_player.type_in_name('Jan')
        add_a_player.type_in_surname('Kowalski')
        add_a_player.type_in_phone('123456789')
        add_a_player.type_in_weight('68')
        add_a_player.type_in_height('180')
        add_a_player.type_in_age('01.01.2001')
        add_a_player.select_leg('right')
        add_a_player.type_in_club('FC JK')
        add_a_player.type_in_level('1')
        add_a_player.type_in_main_position('goalkeeper')
        add_a_player.type_in_second_position('defender')
        add_a_player.select_district('Silesia')
        add_a_player.type_in_achievements('no achievements')
        add_a_player.click_add_language_button()
        add_a_player.type_in_languages('English')
        add_a_player.type_in_laczy_nas_pilka('www.laczynaspilka.pl/jankowalski')
        add_a_player.type_in_dziewiecdziesiat_minut('www.90minut.pl/jankowalski')
        add_a_player.type_in_facebook('www.facebook.com/jankowalski')
        add_a_player.click_add_link_to_youtube_button()
        add_a_player.type_in_link_to_youtube('https://www.youtube.com/watch?v=A-FKkuqXeRg')
        add_a_player.click_clear_button()
        add_a_player.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()