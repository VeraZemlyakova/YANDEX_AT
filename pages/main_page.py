from pages.base_page import WebPage
from pages.locators import SearchLocators, NavigationLocators, ImagesLocators
import time


class SearchBlock(WebPage):

    def find_search_field(self):
        return self.find_element(SearchLocators.SEARCH_FIELD)

    def get_search_results(self):
        return self.get_attrs(SearchLocators.RESULTS, 'href')

    def results_table_is_displayed(self):
        # Checking the visibility of results table
        return self.is_visible(SearchLocators.RESULTS_TABLE)

    def send_search_text(self, text):
        # Send search text in the search field
        search_field = self.find_search_field()
        search_field.click()
        search_field.send_keys(text)
        # return search_field

    def suggest_table_is_displayed(self):
        # Checking the visibility of suggest table
        return self.is_visible(SearchLocators.SUGGEST_TABLE)


class ImagesBlock(WebPage):

    def click_on_images_link(self):
        # Send search text in the search field
        search_field = self.find_images_link()
        search_field.click()
        time.sleep(2)

    def click_on_forward_button(self):
        # Send search text in the search field
        buttons = self.find_elements(ImagesLocators.OPEN_IMG_BUTTONS)
        buttons[3].click()

    def click_on_back_button(self):
        # Send search text in the search field
        buttons = self.find_elements(ImagesLocators.OPEN_IMG_BUTTONS)
        buttons[0].click()

    def find_images_link(self):
        return self.find_element(NavigationLocators.IMAGES_LINK)

    def get_images_alt(self):
        return self.get_attrs(ImagesLocators.IMAGES_IMG, 'alt')

    def get_images_href(self):
        return self.get_attrs(ImagesLocators.IMAGES, 'href')

    def get_cat_alt(self):
        return self.get_attrs(ImagesLocators.IMAGES_CATEGORIES_IMG, 'alt')

    def get_cat_href(self):
        return self.get_attrs(ImagesLocators.IMAGES_CATEGORIES, 'href')

    def get_nav_bar_text(self):
        return self.get_texts(NavigationLocators.NAVIGATION_BAR)

    def get_search_text(self):
        return self.get_attr(SearchLocators.SEARCH_FIELD, 'value')

    def get_open_img_src(self):
        return self.get_attr(ImagesLocators.OPEN_IMG, 'src')

    def get_open_img_name(self):
        return self.get_text(ImagesLocators.OPEN_IMG_NAME)

    def go_to_cat(self, num: int):
        url = self.get_cat_href()[num]
        self.driver.get(url=url)

    def go_to_img(self, num: int):
        url = self.get_images_href()[num]
        self.driver.get(url=url)
        return self.get_open_img_src()
