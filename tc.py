from os import environ
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


INTERVAL = 0.04


def click_at_ratio(action, frame, x, y):
    height = frame.size['height']
    width = frame.size['width']
    action.move_to_element_with_offset(frame, width * x, height * y)
    action.click()
    action.pause(INTERVAL)


def loop(driver):
    frame = driver.find_element_by_id('unityFrame')

    while True:
        action = ActionChains(driver)

        click_at_ratio(action, frame, .5, .5)

        for i in range(200):
            action.click()
            action.pause(INTERVAL)

        # click all the upgrade buttons
        click_at_ratio(action, frame, 0.05, .3)
        click_at_ratio(action, frame, 0.05, .45)
        click_at_ratio(action, frame, 0.05, .6)
        click_at_ratio(action, frame, 0.05, .7)
        click_at_ratio(action, frame, 0.05, .85)

        # click 'activate all'
        click_at_ratio(action, frame, 0.95, .7)

        # click dimension shift
        click_at_ratio(action, frame, 0.83, .62)

        # click cooldown
        click_at_ratio(action, frame, 0.97, .62)

        action.perform()


def tc(username, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('http://www.timegamers.com/login/')
    form = driver.find_element_by_id('pageLogin')
    form.find_element_by_id('ctrl_pageLogin_login').send_keys(username)
    form.find_element_by_id('ctrl_pageLogin_password').send_keys(password)
    form.find_element_by_css_selector('[type=submit]').click()
    driver.find_element_by_css_selector('.navTab.account')
    driver.get('http://www.timegamers.com/TimeClickers/WebGL/#unityFrame')

    sleep(30)  # hopefully the game will load in this time

    frame = driver.find_element_by_id('unityFrame')
    action = ActionChains(driver)

    # click play
    click_at_ratio(action, frame, .5, .55)
    action.pause(20)  # another unchecked load wait

    # open settings, disable screen shake and post effects, and close settings
    click_at_ratio(action, frame, .25, .05)
    click_at_ratio(action, frame, .04, .23)
    click_at_ratio(action, frame, .04, .45)
    click_at_ratio(action, frame, .25, .05)

    # turn idle mode on for weapons
    click_at_ratio(action, frame, .29, .96)
    click_at_ratio(action, frame, .71, .96)
    # XXX idk where the button is for the third weapon

    # set upgrade mode to max
    for i in range(3):
        click_at_ratio(action, frame, .03, .95)

    action.perform()
    loop(driver)


if __name__ == '__main__':
    username = environ['TC_USERNAME']
    password = environ['TC_PASSWORD']
    tc(username, password)
