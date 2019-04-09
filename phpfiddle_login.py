# Imports
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.phpfiddle.org"
username = "myusername"
password = "mypassword"
signin_button_xpath = "//*[@id=\"signin_button\"]"
username_xpath = "//*[@id=\"sign_email\"]"
password_xpath = "//*[@id=\"sign_pword\"]"
login_button_xpath = "/html/body/div[1]/div/form/input[4]"
mylinks_button_xpath = "/html/body/div[1]/div[1]/div/ul/li[7]/a"
go_button_xpath = "//*[@id=\"mylinks_search\"]"
option_chain_link_xpath = "/html/body/div[1]/div[1]/div/div[5]/div[2]/div/strong[5]/a"
pass_url_link_xpath = "/html/body/div[1]/div[1]/div/div[5]/div[2]/div/strong[6]/a"
saveas_button_xpath = "//*[@id=\"link_button\"]"
filename_textbox_xpath = "//*[@id=\"fname\"]"
submit_button_xpath = "/html/body/div[1]/div/form/input[5]"
signout_button_xpath = "//*[@id=\"signout_button\"]"
browser = object()


# Launch browser
def launch_browser():
    global browser
    options = Options()
    options.headless = True
    print("Launching firefox in headless mode")
    browser = webdriver.Firefox(options=options)
    print("Opening", url)
    browser.get(url)


# Check if element exists, max default wait of 10s
def element_exists(element_xpath, wait_time=5):
    element = False
    for counter in range(0, wait_time):
        try:
            element = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
            print("Found", element_xpath, "after", counter * 2, "s")
            break
        except:
            browser.find_element_by_xpath(element_xpath).send_keys(username)
            print("Couldn't find", element_xpath, "Retry after 1s")
            time.sleep(1)
    return element


# Login
def login():
    print("Clicking Sign In button")
    element_exists(signin_button_xpath).click()
    print("Switching to iframe_1")
    browser.switch_to.frame(browser.find_element_by_id('iframe_1'))
    print("Entering username")
    element_exists(username_xpath).send_keys(username)
    print("Entering password")
    element_exists(password_xpath).send_keys(password)
    print("Clicking login button")
    element_exists(login_button_xpath).click()
    print("Switching to default window from iframe_1")
    browser.switch_to.default_content()


def savefiles():
    print("Clicking My Links menu item")
    element_exists(mylinks_button_xpath).click()
    print("Clicking Go button")
    element_exists(go_button_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Clicking nnq2-06mf")
    element_exists(option_chain_link_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Clicking Save As button")
    element_exists(saveas_button_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Switching to iframe")
    browser.switch_to.frame(browser.find_element_by_id('iframe_1'))
    print("Inputting file name: OptionChain")
    element_exists(filename_textbox_xpath).send_keys("OptionChain")
    print("Clicking Submit button")
    element_exists(submit_button_xpath).click()
    print("Switching to default window from iframe_1")
    browser.switch_to.default_content()

    print("Clicking My Links menu item")
    element_exists(mylinks_button_xpath).click()
    print("Clicking Go button")
    element_exists(go_button_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Clicking 2pis-ri8v")
    element_exists(pass_url_link_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Clicking Save As button")
    element_exists(saveas_button_xpath).click()
    print("Waiting for 2s")
    time.sleep(2)
    print("Switching to iframe")
    browser.switch_to.frame(browser.find_element_by_id('iframe_1'))
    print("Inputting file name: passurl")
    element_exists(filename_textbox_xpath).send_keys("passurl")
    print("Clicking Submit button")
    element_exists(submit_button_xpath).click()
    print("Switching to default window from iframe_1")
    browser.switch_to.default_content()


# #Logout
def logout():
    print("Clicking Sign Out button")
    element_exists(signout_button_xpath).click()


# #Close browser
def close_browser():
    print("Closing Firefox")
    browser.close()


launch_browser()
login()
savefiles()
logout()
close_browser()
