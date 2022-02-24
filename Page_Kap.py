from Locator_Kap import *
from Element_Kap import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "login"

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Kapaga" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    #def ValidUsername(self):
        #type = self.driver.find_element(*SearchResultsPageLocators.Search_bar)

class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
