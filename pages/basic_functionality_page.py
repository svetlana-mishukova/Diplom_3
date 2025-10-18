import allure
import pytest
import allure
from locators.base_page_locators import BasePageLocators  
from locators.basic_functionality_page_locators import BasicFunctionalityLocators
from pages.base_page import BasePage
from curl import main_site
from selenium.common.exceptions import TimeoutException  



class BasicFunctionalityPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, BasicFunctionalityLocators.OVERLAY)

    @allure.step("Проверка состояния оверлея")
    def check_overlay_state(self, state='visible', timeout=10):
        methods = (self.wait_for_element, self.wait_for_element_disappear)
        method = methods[state == 'invisible']
        return method(self.overlay_locator, timeout)

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_url(main_site)
        self.wait_for_element(BasicFunctionalityLocators.BURGER, timeout=20)
        self.wait_for_overlay_disappear()
       

    @allure.step("Перейти в раздел 'Лента заказов'")
    def navigate_to_orders(self):
        self.click_element(BasicFunctionalityLocators.LENTA_BUT)
        self.wait_for_element(BasicFunctionalityLocators.LENTA, timeout=20)
        self.verify_orders_title()
        self.wait_for_overlay_disappear()
           
    @allure.step("Перейти в раздел 'Конструктор'")
    def navigate_to_constructor(self):
        self.click_element(BasicFunctionalityLocators.CONSTR)
        self.wait_for_element(BasicFunctionalityLocators.BURGER, timeout=20)
        self.verify_constructor_title()
        self.wait_for_overlay_disappear()
       

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_element(BasicFunctionalityLocators.BUN)
        self.wait_for_element(BasicFunctionalityLocators.DETAILS, timeout=30)        
       
    @allure.step("Закрыть детали ингредиента")
    def close_ingredient_details(self):
        self.click_element(BasicFunctionalityLocators.CROSS)  
        self.wait_for_element(BasicFunctionalityLocators.BURGER, timeout=10)
               
    @allure.step("Получить заголовок деталей")
    def get_details_title(self):
        return self.get_element_text(BasicFunctionalityLocators.DETAILS)
    
    @allure.step("Проверить закрытие окна деталей")
    def is_details_closed(self):
        return len(self.driver.find_elements(*BasicFunctionalityLocators.DETAILS)) == 0 
    
    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient(self):    
        initial_count = self.get_ingredient_count()
        self.drag_and_drop_ingredient_to_constructor() 
        final_count = self.get_ingredient_count() 
        assert final_count == initial_count + 2
        return final_count  
            
    @allure.step("Перетащить ингредиент в конструктор")
    def drag_and_drop_ingredient_to_constructor(self):
        bun = self.wait_for_element(BasicFunctionalityLocators.BUN, timeout=10)
        drag = self.wait_for_element(BasicFunctionalityLocators.DRAG, timeout=10)
        self.drag_and_drop_element(bun, drag)
        self.wait_for_ingredient_update()
    
    @allure.step("Получить количество ингредиента")
    def get_ingredient_count(self):
        count_element = self.wait_for_element(BasicFunctionalityLocators.COUNTER, timeout=10)
        counter_text = count_element.text.strip()
        return int(counter_text)
    
    @allure.step("Проверить счетчик ингредиентов")
    def check_ingredient_counter(self, expected_count):
        actual_count = self.get_ingredient_count()
        assert actual_count == expected_count, f"Ожидалось: {expected_count}, получено: {actual_count}"
        return actual_count
    
    @allure.step("Ожидание обновления ингредиентов")
    def wait_for_ingredient_update(self):
        self.wait_for_element(BasicFunctionalityLocators.COUNTER, timeout=20)
        self.wait_for_overlay_disappear()
        self.wait_for_element(BasicFunctionalityLocators.BURGER_CONSTR, timeout=20)
    
    @allure.step("Проверить заголовок страницы Конструктора")
    def verify_constructor_title(self):
        actual_title = self.get_element_text(BasicFunctionalityLocators.BURGER)
        assert actual_title == "Соберите бургер", f"Неверный заголовок: {actual_title}"

    @allure.step("Проверить заголовок страницы Ленты заказов")
    def verify_orders_title(self):
        actual_title = self.get_element_text(BasicFunctionalityLocators.LENTA)
        assert actual_title == "Лента Заказов", f"Неверный заголовок: {actual_title}"

    @allure.step("Проверить заголовок окна деталей ингредиента")
    def verify_ingredient_details_title(self):
        actual_title = self.get_element_text(BasicFunctionalityLocators.DETAILS)
        assert actual_title == "Детали ингредиента", f"Неверный заголовок: {actual_title}"

    @allure.step("Получить заголовок Ленты заказов")
    def get_lenta_title(self):
        return self.get_element_text(BasicFunctionalityLocators.LENTA)

    @allure.step("Получить заголовок Конструктора")
    def get_constructor_title(self):
        return self.get_element_text(BasicFunctionalityLocators.BURGER)

    @allure.step("Получить заголовок деталей ингредиента")
    def get_ingredient_details_title(self):
        return self.get_element_text(BasicFunctionalityLocators.DETAILS)
    
    @allure.step("Проверить корректность добавления ингредиента")
    def verify_ingredient_addition(self):
        initial_count = self.get_ingredient_count()
        self.add_ingredient()
        final_count = self.get_ingredient_count()
        assert final_count == initial_count + 1, "Ингредиент не был добавлен"
        return final_count
    
    @allure.step("Проверить отсутствие оверлея")
    def verify_overlay_absence(self):
        self.check_overlay_state('invisible')