from data import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebPage:

    def __init__(self, driver, url=''):
        self.driver = driver
        if not url:
            url = BASE_URL
        self.url = url

    def find_element(self, locator, timeout=10):
        """ Find element on the page. """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        """ Find elements on the page. """

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def is_visible(self, locator, timeout=10):
        """ Checking the visibility of element on the page. """

        element = self.find_element(locator=locator)
        if element:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of(element),
                                                             message=f"Can't visible element by locator {locator}")
        return False

    def get_attr(self, locator, attr):
        """ Get text of element. """

        element = self.find_element(locator=locator)
        result = ''
        try:
            result = str(element.get_attribute(attr))
        except Exception as e:
            print(f'Error: {e}')
        return result

    def get_attrs(self, locator, attr):
        """ Get attributes of elements. """

        elements = self.find_elements(locator=locator)
        result = []
        for element in elements:
            value = ''
            try:
                value = str(element.get_attribute(attr))
            except Exception as e:
                print(f'Error: {e}')
            result.append(value)
        return result

    def get_current_url(self):
        """ Returns current browser URL. """
        self.switch_to()
        cur_url = self.driver.current_url
        return cur_url

    def get_text(self, locator):
        """ Get text of element. """

        element = self.find_element(locator=locator)
        result = ''
        try:
            result = str(element.text)
        except Exception as e:
            print(f'Error: {e}')
        return result

    def get_texts(self, locator):
        """ Get text of elements. """

        elements = self.find_elements(locator=locator)
        result = []
        for element in elements:
            value = ''
            try:
                value = str(element.text)
            except Exception as e:
                print(f'Error: {e}')
            result.append(value)
        return result

    def go_to_url(self):
        """ Go to a web page. """
        return self.driver.get(self.url)

    def switch_to(self):
        num = len(self.driver.window_handles)-1
        self.driver.switch_to.window(self.driver.window_handles[num])

    def title_contains(self, text):
        return WebDriverWait(self.driver, timeout=10).until(EC.title_contains(text),
                                                            message=f"title contains no text {text}")
