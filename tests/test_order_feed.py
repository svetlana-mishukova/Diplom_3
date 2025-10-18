import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from curl import *
from generators import generate_registration_data
from pages.order_feed_page import OrderFeedPage
from selenium.common.exceptions import TimeoutException

class TestPersonalAccount:
    
    @allure.title("Счётчик «Выполнено за всё время»")
    @allure.description("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_counter_all_time_completed(self, driver):
        with allure.step("Авторизация и переход в конструктор"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open_main_page()
            order_feed_page.check_overlay_state()
            order_feed_page.registration()
            order_feed_page.from_personal_account_to_the_designer()
        with allure.step("Сохранение начального значения счетчика"):
            initial_count = order_feed_page.get_completed_orders_count_BEFORE()  
        with allure.step("Создание заказа"):           
            order_feed_page.drag_and_drop_ingredient_to_constructor_bun()
            order_feed_page.scroll_to_sause()
            order_feed_page.drag_and_drop_ingredient_to_constructor_sause()
            order_feed_page.scroll_to_filling()
            order_feed_page.drag_and_drop_ingredient_to_constructor_filling()
        with allure.step("Проверка номера заказа и закрытие модального окна"):   
            order_feed_page.check_overlay_state()
            order_number = order_feed_page.wait_for_order_number()
            order_feed_page.check_overlay_state()
            order_feed_page.close_and_verify_modal()
        with allure.step("Проверка увеличения счетчика"): 
            final_count = order_feed_page.get_completed_orders_count_AFTER()
            assert final_count > initial_count, "Счетчик 'Выполнено за всё время' не увеличился"

    @allure.title("Счётчик «Выполнено за сегодня»")
    @allure.description("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_counter_completed_today(self, driver):
        with allure.step("Авторизация и переход в конструктор"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open_main_page()
            order_feed_page.check_overlay_state()
            order_feed_page.registration()
            order_feed_page.from_personal_account_to_the_designer()
        with allure.step("Сохранение начального значения счетчика"):
            initial_today_count = order_feed_page.get_today_orders_count_BEFORE()   
        with allure.step("Создание заказа"):             
            order_feed_page.drag_and_drop_ingredient_to_constructor_bun()
            order_feed_page.scroll_to_sause()
            order_feed_page.drag_and_drop_ingredient_to_constructor_sause()
            order_feed_page.scroll_to_filling()
            order_feed_page.drag_and_drop_ingredient_to_constructor_filling()
        with allure.step("Проверка номера заказа и закрытие модального окна"): 
            order_feed_page.check_overlay_state()
            order_number = order_feed_page.wait_for_order_number()
            order_feed_page.check_overlay_state()
            order_feed_page.close_and_verify_modal()
        with allure.step("Проверка увеличения счетчика"): 
            final_today_count = order_feed_page.verify_today_orders_increased_AFTER()
            assert final_today_count > initial_today_count, "Счетчик 'Выполнено за сегодня' не увеличился"

    @allure.title("Раздел «В работе»")
    @allure.description("После оформления заказа его номер появляется в разделе «В работе»")
    def test_section_in_progress(self, driver):
        with allure.step("Авторизация и переход в конструктор"):
            order_feed_page = OrderFeedPage(driver)
            order_feed_page.open_main_page()
            order_feed_page.check_overlay_state()
            order_feed_page.registration()
        with allure.step("Создание заказа"):              
            order_feed_page.drag_and_drop_ingredient_to_constructor_bun()
            order_feed_page.scroll_to_sause()
            order_feed_page.drag_and_drop_ingredient_to_constructor_sause()
            order_feed_page.scroll_to_filling()
            order_feed_page.drag_and_drop_ingredient_to_constructor_filling()
        with allure.step("Получение номера заказа и закрытие модального окна"): 
            order_feed_page.check_overlay_state()
            order_number = order_feed_page.wait_for_order_number()
            order_feed_page.check_overlay_state()
            order_feed_page.close_and_verify_modal()
        with allure.step("Проверка появления заказа в разделе В работе"): 
            order_feed_page.click_element_lenta_but
            order_feed_page.wait_for_element_lenta
            is_order_present = order_feed_page.check_order_in_progress(order_number)
            assert is_order_present, f"Заказ {order_number} не обнаружен в разделе «В работе»"    
