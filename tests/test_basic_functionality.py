import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basic_functionality_page import BasicFunctionalityPage
from curl import *
from selenium.common.exceptions import TimeoutException


class TestSectionConstructor:

    @allure.title("Навигация")
    @allure.description("Переход в Лента Заказов")
    def test_lenta_navigation(self, driver):
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.open_main_page()
        basic_functionality_page.navigate_to_orders()
        basic_functionality_page.wait_until_page_loaded()
        expected_text = "Лента Заказов"
        actual_text = basic_functionality_page.get_lenta_title()
        assert actual_text == expected_text


    @allure.title("Навигация")
    @allure.description("Переход в Конструктор")
    def test_constructor_navigation(self, driver):
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.open_main_page()
        expected_text = "Соберите бургер"
        actual_text = basic_functionality_page.get_constructor_title() 
        assert actual_text == expected_text    

    @allure.title("Всплывающее окно")
    @allure.description("Открытие и закрытие деталей ингредиента")
    def test_ingredient_details(self, driver):
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.open_main_page()
        with allure.step('Проверка начального состояния'):
            assert basic_functionality_page.is_details_closed()
        with allure.step('Открытие деталей ингредиента'):
            basic_functionality_page.open_ingredient_details()
            assert not basic_functionality_page.is_details_closed()
            title = basic_functionality_page.get_details_title()
            assert title 
        with allure.step('Закрытие деталей ингредиента'):
            basic_functionality_page.close_ingredient_details()
            assert basic_functionality_page.is_details_closed()


    @allure.title("Добавление ингредиента")
    @allure.description("Проверка увеличения счетчика при добавлении ингредиента")
    def test_ingredient_counter(self, driver):
        basic_functionality_page = BasicFunctionalityPage(driver)
        basic_functionality_page.open_main_page()
        with allure.step("Получение начального значения счетчика"):
            initial_count = basic_functionality_page.get_ingredient_count()
            basic_functionality_page.check_ingredient_counter()
        with allure.step("Добавление ингредиента"):             
            basic_functionality_page.add_ingredient()
            basic_functionality_page.drag_and_drop_ingredient_to_constructor()
            basic_functionality_page.wait_for_ingredient_update()
            basic_functionality_page.wait_for_overlay_disappear(30)
        with allure.step("Проверка увеличения счетчика"):    
            final_count = basic_functionality_page.get_ingredient_count()
        assert final_count == initial_count + 2, (
            f"Ожидаемое количество: {initial_count + 2}",
            f"Фактическое количество: {final_count}"
        )   
       


   