from behave import *
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from messages import verify_messages
from utils import constant


@given(u'the user is at "{home_page}"')
def step_impl(context, home_page):
    context.driver = webdriver.Chrome()
    HomePage.open_page(context.driver, home_page)


@when(u'user search a new "{product}"')
def step_impl(context, product):
    HomePage.search_product(context.driver, product)


@when(u'sort by "{index}" order the list')
def step_impl(context, index):
    ProductPage.sort_by(context.driver, index)


@when(u'add the product')
def step_impl(context):
    ProductPage.select_product(context.driver, constant.ten)
    ProductPage.add_to_cart(context.driver)
    ProductPage.go_to_cart_click_mouse(context.driver, constant.ten)
    CartPage.verify_add(context.driver, constant.ten)


@then(u'delete de product')
def step_impl(context):
    CartPage.delete_product(context.driver)
    CartPage.verify_delete(context.driver, verify_messages.deleteMessage)
