from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import page_loaded
import time


@given(u'User has navigated to the home page website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://parabank.parasoft.com/parabank/index.htm")

@when(u'User has loaded home page')
def step_impl(context):
    assert page_loaded(context.driver, '//a[normalize-space()=\'Home\']', 15) is True

@then(u'User observes logo')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,"//img[@title='ParaBank']").is_displayed()
    assert status is True


@when(u'User clicks on products category button in the header')
def step_impl(context):
    assert page_loaded(context.driver, '//a[normalize-space()=\'Home\']', 15) is True
    context.driver.find_element(By.XPATH,"//ul[@class='leftmenu']//a[normalize-space()='Products']").click()
    

@then(u'User is redirected to the products page URL and observes products page content')
def step_impl(context):    
    status = context.driver.find_element(By.XPATH,"//p[@class='page-title']").is_displayed()
    assert status is True


@when(u'User clicks on "Parabank is now re-opened" button')
def step_impl(context):
    assert page_loaded(context.driver, '//a[normalize-space()=\'Home\']', 15) is True
    context.driver.find_element(By.XPATH,"//a[normalize-space()='ParaBank Is Now Re-Opened']").click()
    

@then(u'User is redirected to the "Parabank is now re-opened" and observes news content')
def step_impl(context):    
    status = context.driver.find_element(By.XPATH,"//h1[normalize-space()='ParaBank News']").is_displayed()
    assert status is True


@when(u'User enters login details')
def step_impl(context):
    assert page_loaded(context.driver, "//input[@name='username']", 15) is True

    context.driver.find_element(By.XPATH,"//input[@name='username']").click()
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys("an123")

    context.driver.find_element(By.XPATH,"//input[@name='password']").click()
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("an123")

    context.driver.find_element(By.XPATH,"//input[@value='Log In']").click()

    status = context.driver.find_element(By.XPATH,"//h1[normalize-space()='Accounts Overview']").is_displayed()
    assert status is True


@then(u'User is redirected to the Account overview page')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,"//h1[normalize-space()='Accounts Overview']").is_displayed()
    assert status is True