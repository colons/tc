from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


INTERVAL = 0.05


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

        for i in range(100):
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


def interactive():
    driver = webdriver.Chrome()
    driver.get('http://www.timegamers.com/login/')
    input("hit enter when you've logged in")
    driver.get('http://www.timegamers.com/TimeClickers/WebGL/')
    input(
        "hit enter when you've clicked 'play', dismissed the update, "
        "enabled idle mode for your click weapons, and set the buy mode to "
        "'max'"
    )
    loop(driver)


if __name__ == '__main__':
    interactive()
