import json
import allure
from Locators.kinopoisk_page_locators import KinopoiskPageLocators
from Pages.base_page import BasePage

class KinopoiskFindPage(BasePage):
    locators = KinopoiskPageLocators()
    with open('settings.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())
    
    @allure.step('Fill fields and submit')
    def find_film(self):
        with allure.step('Filling fields'):
            self.elements_is_visible(self.locators.INPUT_FILM_TITLE).send_keys(self.settings['film']['title'])
            self.elements_is_visible(self.locators.SELECT_COUNTRY).send_keys(self.settings['film']['country'])
            self.elements_is_visible(self.locators.SELECT_GENRE).send_keys(self.settings['film']['genre'])
        with allure.step('Click submit'):
            self.elements_is_present(self.locators.SUBMIT).click()

    
    def check_top_five(self):
        name_list = self.elements_are_present(self.locators.FILM_TITLE)
        for element in range(1,6):
            if self.settings['film']['title'] == name_list[element].text:
                return True
        return False