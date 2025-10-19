from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  


class OrderFeedPageLocators: 
    # Локаторы для регистрации
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'a[href="/register"]')

    NAME = (By.CSS_SELECTOR, "fieldset:nth-child(1) input.text_type_main-default")
    EMAIL = (By.CSS_SELECTOR, "fieldset:nth-child(2) input.text_type_main-default")
    PASSWORD = (By.NAME, "Пароль")
    REG_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    ERROR_M = (By.CSS_SELECTOR, "p.input__error.text_type_main-default")

    LOGIN = (By.LINK_TEXT, "Войти")

    # Локаторы для авторизации
    EMAIL_AUTH = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    PASS_AUTH = (By.NAME, "Пароль")
    BUTTON = (By.XPATH, "//button[text()='Войти']")
    DES_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    ACCOUNT = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")
    FORM_1 = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")
    FORM_2 = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")
    FORM_PASS_1 = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    FORM_PASS_2 = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login']")
    FORM_PASS_3 = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default")

    LENTA_BUT = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    LENTA = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']")
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, ".//*[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")
    BUN = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']")
    DRAG = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7']//span[contains(text(), 'Перетяните булочку сюда')]")
    SAUCE = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    SAUSE_CONT = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")
    FILLING = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
    FILLING_CONT = (By.XPATH, "//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8' and @href='/ingredient/61c0c5a71d1f82001bdaaa70' and @draggable='true']")
    ORDER = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']")
    LOADING = (By.XPATH, "//h2contains(@class, 'Modal_modal__title') and text()='9999'")
    NUMBER_CONTAINER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    CLOSE_BUT = (By.XPATH, "//button@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'")
    MODAL_WINDOW = (By.XPATH, "//div@class='Modal_modal__contentBox__sCy8X pt-30 pb-30'")
    CONSTR = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")
    TEXT_COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, ".//*[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    ORDER_LOCATOR = (By.XPATH, "//div[contains(@class, 'Modal_modal__content')]/h2[text()='{}']")

    ACTIVE_TAB_SAUCE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']")
    ACTIVE_TAB_FILLING = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']")
    ACTIVE_TAB_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']")




        

    
    
  
   
    
   
    
