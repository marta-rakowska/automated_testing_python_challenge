from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    main_page_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    matches_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    reports_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[3]/div[2]/span"
    polski_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[1]/div[2]/span"
    sign_out_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[3]/div[2]/div[2]/span"
    my_team_xpath = "//*[@name='myTeam']"
    enemy_team_xpath = "//*[@name='enemyTeam']"
    my_team_score_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_xpath = "//*[@name='enemyTeamScore']"
    date_xpath = "//*[@name='date']"
    match_at_home_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[2]"
    match_out_home_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[2]"
    tshirt_color_xpath = "//*[@name='tshirt']"
    league_xpath = "//*[@name='league']"
    time_played_xpath = "//*[@name='timePlayed']"
    number_xpath = "//*[@name='number']"
    web_match_xpath = "//*[@name='webMatch']"
    general_xpath = "//*[@name='general']"
    rating_xpath = "//*[@name='rating']"
    submit_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    clear_xpath = "//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"

    pass