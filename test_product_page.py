from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest

link_old = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_new = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

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
    # Ожидаемый результат:
    # Сообщение о том, что товар добавлен в корзину.
    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    # Сообщение со стоимостью корзины.
    # Стоимость корзины совпадает с ценой товара.
    page.should_be_correct_product_name_message()
    page.should_be_correct_product_price_message() 
