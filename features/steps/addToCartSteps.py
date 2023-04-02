from behave import *
from selenium import webdriver
from features.pages.homePage import HomePage
from features.pages.productPage import ProductPage
from features.pages.cartPage import CartPage

url = "https://www.amazon.com/-/es/"
productOne = "iphone 14 pro"
productTwo = "washing machine"
descendingIndex = 1
time = 10
deleteMessageExpected = "se ha eliminado del Carrito."
deleteMessageExpected2 = "loca"
driver = ""


@given(u'the user is at home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    HomePage.open_page(context.driver, url)


@when(u'user search a new product')
def step_impl(context):
    HomePage.search_product(context.driver, productOne)


@when(u'sort by decent order the list')
def step_impl(context):
    ProductPage.sort_by(context.driver, descendingIndex)


@when(u'add the product')
def step_impl(context):
    ProductPage.select_product(context.driver, time)
    ProductPage.add_to_cart(context.driver)
    CartPage.verify_add(context.driver, time)


@then(u'delete de product')
def step_impl(context):
    ProductPage.go_to_cart_click_mouse(context.driver, time)
    CartPage.delete_product(context.driver)
    CartPage.verify_delete(context.driver,deleteMessageExpected)
