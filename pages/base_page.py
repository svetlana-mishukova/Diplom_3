import os
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from locators.base_page_locators import BasePageLocators
from curl import main_site
from selenium.common.exceptions import TimeoutException  

class BasePage: 
        
    def __init__(self, driver, overlay_locator=None):
        self.driver = driver
        self.overlay_locator = overlay_locator

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)    
    
    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ожидание появления/исчезновения элемента")
    def wait_for_element(self, locator, timeout=10, visible=True):
        by, value = locator
        wait = WebDriverWait(self.driver, timeout)
        methods = (wait.until, wait.until_not)
        method = methods[int(not visible)]
        method(expected_conditions.presence_of_element_located((by, value)))

    def wait_for_element_visibility(self, locator, timeout):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
                                                    
    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.wait_for_element(*locator).text
    
    @allure.step("Ввести текст в поле")
    def send_keys_to_input(self, locator, text):
        element = self.wait_for_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Очистить поле ввода")
    def clear_input(self, locator):
        element = self.wait_for_element(locator)
        element.clear()

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        source =self.driver.find_element(*sourse_locator)
        source =self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)  


    @allure.step("Кликнуть на элемент с обработкой перехвата")
    def safe_click(self, locator):
        self.wait_for_overlay_disappear()
        element = self.wait_for_element(locator)
        self.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Проверить состояние оверлея")
    def check_overlay_state(self, state='visible', timeout=10):
        method = (self.wait_for_element_disappear, self.wait_for_element)[state == 'visible']
        return method(self.overlay_locator, timeout)

    @allure.step("Получить локатор оверлея")
    def get_overlay_locator(self):
        return self.overlay_locator  

    def wait_for_overlay_disappear(self, timeout=30):
        self.wait_for_element(self.overlay_locator, timeout, False)

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_disappear(self, locator, timeout):
        self.wait_for_element(locator, timeout, False)   
         
    @allure.step("Найти элемент по локатору")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Ожидание полной загрузки страницы")
    def wait_until_page_loaded(self, timeout=20):
        self.wait_for_element_disappear(self.overlay_locator, timeout)