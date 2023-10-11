import allure
from Pages.find_page import KinopoiskFindPage

@allure.feature('Kinopoisk Find Film')
class TestFind:

    @allure.title('Search a movie by title')
    def test_find_film(self, driver):
        find_page = KinopoiskFindPage(driver,'https://www.kinopoisk.ru/s/')
        find_page.open()
        find_page.find_film()
        assert find_page.check_top_five() == True