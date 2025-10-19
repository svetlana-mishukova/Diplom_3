from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  

class BasePageLocators:
    BURGER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and contains(., 'Соберите бургер')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")