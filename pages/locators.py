# Locators for site page elements

from selenium.webdriver.common.by import By


class SearchLocators:

    RESULTS = (By.XPATH, '//ul[@aria-label="Результаты поиска"]//a')
    RESULTS_TABLE = (By.CSS_SELECTOR, '.main__content')
    SEARCH_FIELD = (By.NAME, "text")
    SUGGEST_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup-content')


class NavigationLocators:

    NAVIGATION_BAR = (By.CSS_SELECTOR, '.services-new__list a')
    IMAGES_LINK = (By.XPATH, '//a[@data-id="images"]')


class ImagesLocators:

    IMAGES_CATEGORIES = (By.CSS_SELECTOR, '.PopularRequestList a')
    IMAGES_CATEGORIES_IMG = (By.CSS_SELECTOR, '.PopularRequestList img')
    IMAGES = (By.CSS_SELECTOR, '.serp-item__link')
    IMAGES_IMG = (By.CSS_SELECTOR, '.serp-item__link  img')
    OPEN_IMG = (By.CSS_SELECTOR,'.MMImage-Origin')
    OPEN_IMG_NAME = (By.CSS_SELECTOR, '.MMOrganicSnippet-Text')
    OPEN_IMG_BUTTONS = (By.CSS_SELECTOR, '.CircleButton-Icon')

