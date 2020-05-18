from selenium import webdriver
import time


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'q'
        self.btn_search = 'btnK'
        self.btn_lucky = 'btnI'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_name(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_name(
            self.search_bar).submit()


def main():
    firefox = webdriver.Firefox()
    g = Google(firefox)
    g.navigate()
    g.search('InspirAda na Computação')
    time.sleep(5)
    firefox.close()


if __name__ == '__main__':
    main()
