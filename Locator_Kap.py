from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.CLASS_NAME, "icon-lock-open")


class SearchResultsPageLocators(object):
    Search_bar = (By.ID, "ClientLoginFormLogin")
