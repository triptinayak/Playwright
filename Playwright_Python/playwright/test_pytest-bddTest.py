import pytest

from pytest_bdd import given, when, then, parsers, scenarios

from Playwright_Python.playwright.conftest import user_credentials
from Playwright_Python.playwright.utils.apiBaseFramework import APIUtils
from pageObjects.login import LoginPage
from Playwright_Python.playwright.pageObjects.orderDetailsPage import OrderDetailsPage
from Playwright_Python.playwright.pageObjects.orderHistory import OrderHistoryPage


scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["password"] = password
    apiutils = APIUtils()
    orderId = apiutils.createOrder(playwright, user_credentials)
    shared_data['orderId'] = orderId

@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data): #browserInsatnce coming from pytest.fixture
    loginPage = LoginPage(browserInstance)
    loginPage.navigation()
    shared_data['login_page'] = loginPage #login page info is now written in the dictionary

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboardPage'] = dashboardPage

@when('navigate to orders page')
def navigate_to_order_page(shared_data):
     dashboardPage = shared_data['dashboardPage']
     orderHistoryPage = dashboardPage.selectOrdersNavLink()
     shared_data['orderHistoryPage'] = orderHistoryPage

@when('select the orderId')
def select_order_id(shared_data):
    orderId = shared_data['orderId']
    orderHistoryPage = shared_data['orderHistoryPage']
    orderDetailsPage = orderHistoryPage.orderDetails(orderId)
    shared_data['orderDetailPage']= orderDetailsPage

@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetailPage']
    orderDetailsPage.verifyOrderMessage()