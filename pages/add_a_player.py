import time

from pages.base_page import BasePage


class AddAPlayer(BasePage):

    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath = "//*[@name='phone']"
    # weight_xpath =
    # height_xpath =
    # age_xpath =
    # leg_xpath =
    # club_xpath =
    # level_xpath =
    # main_position_xpath =
    # second_position_xpath =
    # district_xpath =
    # achievements_xpath =
    # add_language_xpath =
    # submit_xpath =
    # clear_xpath =

    expected_title = "Add player"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title