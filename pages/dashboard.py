from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div/div[1]"
    matches_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[1]"
    reports_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[3]/div/div[1]"
    events_count_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[4]/div/div[1]"
    dev_team_contact_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    add_player_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    logo_scouts_panel_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]"
    shortcuts_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/h2"
    activity_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/h2"
    last_created_player_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[1]"
    last_updated_player_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[2]"
    last_created_match_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[3]"
    last_updated_match_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[4]"
    last_updated_report_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[5]"

    pass