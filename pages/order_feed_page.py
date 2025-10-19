import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from curl import main_site
from generators import generate_registration_data
from selenium.common.exceptions import TimeoutException  

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, OrderFeedPageLocators.OVERLAY)

    @allure.step("Локатор")    
    def get_overlay_locators(self):
        return self.overlay_locator

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(main_site)        
        self.wait_for_element(OrderFeedPageLocators.BURGER, 0)
        self.wait_for_overlay_disappear()

    @allure.step("Регистрация пользователя")
    def registration(self, generate_registration_data): 
        name, email, password = generate_registration_data
        self.click_element(OrderFeedPageLocators.LOGIN_BUTTON)
        self.wait_for_overlay_disappear(OrderFeedPageLocators.OVERLAY)
        self.click_element(OrderFeedPageLocators.REGISTER_BUTTON)
        self.wait_for_overlay_disappear(OrderFeedPageLocators.OVERLAY)
        self.send_keys_to_input(OrderFeedPageLocators.NAME, name)
        self.send_keys_to_input(OrderFeedPageLocators.EMAIL, email)
        self.send_keys_to_input(OrderFeedPageLocators.PASSWORD, password)
        self.click_element(OrderFeedPageLocators.REG_BUTTON)
        self.wait_for_overlay_disappear()

    @allure.step("Авторизация и переход в раздел Лента заказов")
    def from_personal_account_to_the_designer(self, generate_registration_data): 
        _, email, password = generate_registration_data 
        self.click_element(OrderFeedPageLocators.LOGIN_BUTTON)
        self.wait_for_overlay_disappear()  
        self.send_keys_to_input(OrderFeedPageLocators.EMAIL_AUTH, email)
        self.send_keys_to_input(OrderFeedPageLocators.PASS_AUTH, password)
        self.click_element(OrderFeedPageLocators.BUTTON)
        self.wait_for_overlay_disappear()

    @allure.step("Перетащить булочку в конструктор")
    def drag_and_drop_ingredient_to_constructor_bun(self, timeout=10):
        self.wait_for_element(OrderFeedPageLocators.CONSTR, timeout).click()
        self.wait_for_element(OrderFeedPageLocators.BURGER, timeout)
        self.wait_for_overlay_disappear(OrderFeedPageLocators.OVERLAY)
        bun = self.wait_for_element(OrderFeedPageLocators.BUN)
        drag = self.wait_for_element(OrderFeedPageLocators.DRAG)
        self.drag_and_drop_element(bun, drag)
        self.wait_for_ingredient_update()
        self.wait_for_overlay_disappear()

    @allure.step("Скролл до секции Соус")  
    def scroll_to_sause(self):
        self.wait_for_element(OrderFeedPageLocators.SAUCE).click()
        self.wait_for_element(OrderFeedPageLocators.ACTIVE_TAB_SAUCE)
        self.wait_for_overlay_disappear()

    @allure.step("Перетащить соус в конструктор")
    def drag_and_drop_ingredient_to_constructor_sause(self):
        sause = self.wait_for_element(OrderFeedPageLocators.SAUSE_CONT)
        drag = self.wait_for_element(OrderFeedPageLocators.DRAG)
        self.drag_and_drop_element(sause, drag)
        self.wait_for_ingredient_update()
        self.wait_for_overlay_disappear()

    @allure.step("Скролл до секции Начинки")  
    def scroll_to_filling(self):
        self.wait_for_element(OrderFeedPageLocators.FILLING).click()
        self.wait_for_element(OrderFeedPageLocators.ACTIVE_TAB_FILLING)
        self.wait_for_overlay_disappear()
        
    @allure.step("Перетащить начинку в конструктор и нажать кнопку Оформить")
    def drag_and_drop_ingredient_to_constructor_filling(self):
       filling = self.wait_for_element(OrderFeedPageLocators.FILLING_CONT)
       drag = self.wait_for_element(OrderFeedPageLocators.DRAG)
       self.drag_and_drop_element(filling, drag)
       self.wait_for_element(OrderFeedPageLocators.BURGER)  
       self.wait_for_element(OrderFeedPageLocators.CONSTR)  
       self.wait_for_element_disappear(OrderFeedPageLocators.OVERLAY)
       self.find_element(OrderFeedPageLocators.ORDER).click()
       self.wait_for_overlay_disappear()

    @allure.step("Получение номера заказа")
    def wait_for_order_number(self, loading_timeout=10, number_timeout=30):
        self.check_overlay_state(state='hidden', timeout=loading_timeout)
        self.wait_for_element(OrderFeedPageLocators.LOADING, timeout=loading_timeout, visible=False)
        element = self.wait_for_element(OrderFeedPageLocators.NUMBER_CONTAINER, timeout=number_timeout)
        number = element.text
        self.wait_for_overlay_disappear()
        return number if len(number) == 6 and number.isdigit() else None
    
    @allure.step("Ожидание появления и клика кнопки закрытия")
    def close_and_verify_modal(self, driver, close_timeout=10, verify_timeout=10):
        self.click_element(OrderFeedPageLocators.CLOSE_BUT, close_timeout)  
        self.wait_for_overlay_disappear(verify_timeout)
    
    @allure.step("Получение количества заказов За все время ДО оформления заказа")
    def get_completed_orders_count_BEFORE(self, driver, timeout=10):
       self.click_element(OrderFeedPageLocators.LENTA_BUT)
       self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
       self.wait_for_overlay_disappear()  
       counter_element = self.wait_for_element(OrderFeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME)
       return int(counter_element.text)

    @allure.step("Получение количества заказов За все время ПОСЛЕ оформления заказа")
    def get_completed_orders_count_AFTER(self, timeout=10):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
        self.wait_for_overlay_disappear()  
        order_locator = OrderFeedPageLocators.ORDER_LOCATOR
        return bool(self.wait_for_element(order_locator, 30, silent=True))
        
    @allure.step("Получение количества заказов Выполнено за сегодня ДО оформления заказа")
    def get_today_orders_count_BEFORE(self, driver, timeout=10):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
        self.wait_for_overlay_disappear()  
        counter_element = self.wait_for_element(OrderFeedPageLocators.TEXT_COUNTER_COMPLETED_FOR_TODAY)
        return int(counter_element.text)

    @allure.step("Получение количества заказов Выполнено за сегодня ПОСЛЕ оформления заказа")
    def verify_today_orders_increased_AFTER(self, driver, initial_count, timeout=10):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
        self.wait_for_overlay_disappear() 
        final_count_element = self.wait_for_element(OrderFeedPageLocators.TEXT_COUNTER_COMPLETED_FOR_TODAY, timeout)
        final_count = int(final_count_element.text)
        return final_count if final_count > initial_count else None
    
    @allure.step("Проверка появления номера заказа в разделе В работе")
    def verify_order_in_progress(self, driver, order_number, timeout=30):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
        self.wait_for_overlay_disappear() 
        order_locator = OrderFeedPageLocators.ORDER_LOCATOR.format(order_number)
        return bool(self.wait_for_element(order_locator, timeout, silent=True))
    
    @allure.step("Проверка наличия конкретного номера заказа в списке элементов раздела В работе")           
    def check_order_number_exists(self, driver, order_number):
       order_locator = OrderFeedPageLocators.ORDER_LOCATOR.format(order_number)
       self.wait_for_overlay_disappear()
       return bool(self.wait_for_element(order_locator, silent=True))

    @allure.step("Переход в раздел Лента")
    def click_element_lenta_but(self):
        element = self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_overlay_disappear()
        return element

    @allure.step("Ожидать появления ленты заказов")
    def wait_for_element_lenta(self, timeout=30):
       lenta_element = self.wait_for_element(OrderFeedPageLocators.LENTA, timeout)
       self.wait_for_overlay_disappear()
       return lenta_element
    
    @allure.step("Проверить наличие заказа в разделе «В работе»")
    def check_order_in_progress(self):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA)
        self.wait_for_overlay_disappear()
        return self.wait_for_element(OrderFeedPageLocators.ORDER_LOCATOR, 30, silent=True) is not None
    
    @allure.step("Проверить количество выполненных заказов")
    def check_completed_orders_count(self):
        self.click_element(OrderFeedPageLocators.LENTA_BUT)
        self.wait_for_element(OrderFeedPageLocators.LENTA)
        self.wait_for_overlay_disappear()
        counter_element = self.wait_for_element(OrderFeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME)
        current_count = int(counter_element.text)
        return current_count
    
    @allure.step("Ожидание обновления ингредиента в конструкторе")
    def wait_for_ingredient_update(self, timeout=10):
        self.wait_for_overlay_disappear()
        self.wait_for_element(OrderFeedPageLocators.BURGER, timeout)
        self.wait_for_element(OrderFeedPageLocators.DRAG, timeout)
        self.wait_for_element(OrderFeedPageLocators.CONSTR, timeout)