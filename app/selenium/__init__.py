from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

def repeatableAction(browserObj):
    browserObj.find_element_by_id("search").send_keys(
        "dwight howard, zion williamson, Giannis Antetokounmpo, lebron james, chris paul, carmelo anthony, kemba walker, james harden")
    sleep(2)

    browserObj.find_element_by_id("search").send_keys(Keys.ENTER)
    sleep(3)

    saveToCSVButton = browserObj.find_element_by_id("saveToCSV")
    action = ActionChains(browserObj)
    action.click(saveToCSVButton)
    action.perform()
    sleep(10)

def execute():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")

    browser = webdriver.Chrome(executable_path='./app/selenium/chromedriver', chrome_options=chrome_options)
    browser.maximize_window()
    sleep(3)

    browser.get("localhost:5000/")
    sleep(3)

    for i in range(20):
        repeatableAction(browser)