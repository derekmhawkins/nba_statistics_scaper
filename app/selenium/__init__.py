from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

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

    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    browser.maximize_window()
    sleep(3)

    browser.get("localhost:5000/")
    sleep(3)

    for i in range(10):
        repeatableAction(browser)

    # videoSelection = browser.find_element_by_link_text("Sexy White Toenails Footjob with Happy Ending on Toes")
    # action = ActionChains(browser)
    # action.click(videoSelection)
    # action.perform()
    # sleep(3)
    #
    # elementToClick = browser.find_element_by_class_name("mhp1138_fullscreen")
    # actions = ActionChains(browser)
    # actions.click(elementToClick)
    # actions.perform()
    # sleep(5)
    #
    # exitFullScreen = browser.find_elements_by_class_name("mhp1138_fullscreen")[1]
    # actions = ActionChains(browser)
    # actions.click(exitFullScreen)
    # actions.perform()
    # sleep(5)
    #
    # browser.quit()
