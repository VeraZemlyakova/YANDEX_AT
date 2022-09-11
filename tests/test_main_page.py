import pytest
from pytest_check import check_func
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.main_page import SearchBlock, ImagesBlock
from data import TITLE_MAIN, SEARCH_TEXT, SEARCH_LINK, IMAGES_LINK_SAMPLE, IMAGES_LINK_NAME


@check_func
def is_link(result):
    assert SEARCH_LINK in result


#  Checking search in Yandex
class TestSearch:

    def test_go_to_yandex(self, browser):
        """ Checking go to Yandex """
        pytest.page = SearchBlock(browser)
        pytest.page.go_to_url()
        assert browser.title == TITLE_MAIN, f"Wrong site title on browser tab"

    def test_search_field_exist(self, browser):
        """ Checking a search field exists """
        assert pytest.page.find_search_field()

    def test_send_text_in_search(self):
        """ Checking suggest tabl is displayed """
        pytest.page.send_search_text(SEARCH_TEXT)
        assert pytest.page.suggest_table_is_displayed()

    def test_search_results_table_is_displayed(self, browser):
        """ Checking the search results tabl is displayed"""
        ActionChains(browser).key_down(Keys.ENTER).perform()
        assert pytest.page.results_table_is_displayed()

    def test_search_results(self):
        """ Checking the search results """
        for result in pytest.page.get_search_results()[:5]:
            is_link(result)


# Checking Images on Yandex
class TestImages:

    def test_images_link_on_yandex(self, browser):
        """ Checking the Images link is on the page """
        pytest.page = ImagesBlock(browser)
        pytest.page.go_to_url()
        elements = pytest.page.get_nav_bar_text()
        assert IMAGES_LINK_NAME in elements, f"Missing Pictures link in navigation bar"

    def test_images_page_url(self):
        """ Checking Images page url """
        pytest.page.click_on_images_link()
        assert IMAGES_LINK_SAMPLE in pytest.page.get_current_url(), f"Wrong url"

    def test_open_first_category(self):
        """ Checking open first category Images"""
        first_cat_name = pytest.page.get_cat_alt()[0]
        pytest.page.go_to_cat(0)
        assert pytest.page.title_contains(first_cat_name)
        assert first_cat_name == pytest.page.get_search_text(), f"Invalid text in search field"

    def test_open_first_image(self):
        """ Checking open first image"""
        assert pytest.page.go_to_img(0), f"Can't open image"

    def test_go_to_next_image(self):
        """ Checking go to next image """
        pytest.first_img = pytest.page.get_open_img_src()
        pytest.page.click_on_forward_button()
        next_img = pytest.page.get_open_img_src()
        assert pytest.first_img != next_img, f"FORWARD: Picture has not changed"

    def test_back_to_first_image(self):
        """ Checking back to first image """
        pytest.page.click_on_back_button()
        img = pytest.page.get_open_img_src()
        assert img == pytest.first_img, f"BACK: The picture is not the same"
