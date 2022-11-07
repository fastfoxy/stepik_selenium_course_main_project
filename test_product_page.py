from .pages.product_page import ProductPage
import pytest
import time
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_promo_2019 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # Открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    # Нажимаем на кнопку "Добавить в корзину".
    page.add_to_basket_click()
    # Посчитать результат математического выражения и ввести ответ.
    page.solve_quiz_and_get_code()
    #time.sleep(3600)
    # Ожидаемый результат:
    # Сообщение о том, что товар добавлен в корзину.
    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    # Сообщение со стоимостью корзины.
    # Стоимость корзины совпадает с ценой товара.
    page.should_be_correct_product_name_message()
    page.should_be_correct_product_price_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, link, 0)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    page = ProductPage(browser, link, 0)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    page = ProductPage(browser, link, 0)
    page.open()
    # Добавляем товар в корзину
    page.add_to_basket_click()
    page.solve_quiz_and_get_code()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_dissapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    # Проверяем, что перешли на страницу корзины
    page.should_be_basket_page()
    # Ожидаем, что в корзине нет товаров
    page.should_not_be_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    page.should_be_basket_empty_text()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        # зарегистрировать нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        login_page.should_be_authorized_user()
        # teardown
        # yield
        # не нужно — пользователей удалять мы не умеем

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, link, 0)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Открываем страницу товара
        page = ProductPage(browser, link)
        page.open()
        # Нажимаем на кнопку "Добавить в корзину".
        page.add_to_basket_click()
        # Посчитать результат математического выражения и ввести ответ.
        page.solve_quiz_and_get_code()
        #time.sleep(3600)
        # Ожидаемый результат:
        # Сообщение о том, что товар добавлен в корзину.
        # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        # Сообщение со стоимостью корзины.
        # Стоимость корзины совпадает с ценой товара.
        page.should_be_correct_product_name_message()
        page.should_be_correct_product_price_message()