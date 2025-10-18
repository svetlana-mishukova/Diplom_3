from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  

class BasicFunctionalityLocators:
  
    LENTA_BUT = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    LENTA = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(., 'Лента Заказов')]")    
    CONSTR = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(., 'Конструктор')]")
    BURGER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and contains(., 'Соберите бургер')]")
    BUN = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient') and contains(., 'булка')]")
    DETAILS = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified')]")
    CROSS = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    BURGER_CONSTR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    DRAG = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//span[contains(text(), 'Перетяните')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")

