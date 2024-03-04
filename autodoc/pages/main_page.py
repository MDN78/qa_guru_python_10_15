from selene import browser, have, be
# # from selene.core import command
# # from utils.logger import step
# # # from demoqa_tests import resource
#
#
class MainPage:

    def open(self):
        browser.open("/")

    def search_item_by_tool_number(self, value):
        browser.element('#partNumberSearch').should(be.blank).send_keys(value)
        browser.element('.search-button').click()
        browser.element('.breadcrumbs-header').should(have.text(value))

    def main_page_should_have_visible_text(self):
        browser.element('.homepage-content__title').should(have.exact_text('Запчасти в интернет-магазине Автодок'))