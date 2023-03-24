from behave import *
from selenium import webdriver


@given('Launch chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome(
        "C:\\Users\\CCI\\PycharmProjects\\behaveProject\\Features\\steps\\chromedriver.exe")




@when("The user opens portal link")
def open_portal(context):
    context.driver.get("https://aologin.azurewebsites.net/Account/Signin")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@then("The user get title")
def verify_text(context):
    get_title = context.driver.title
    print(get_title)
    assert get_title == "Universal Login"


@then("Close browser")
def close_browser(context):
    context.driver.quit()
