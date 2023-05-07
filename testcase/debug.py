# coding:utf-8
from time import sleep

from loguru import logger
from selenium import webdriver
from appium import webdriver
import datetime
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


def find_element(*loc):
    try:
        # self.take_screenshot()
        logger.info(f'going to find{loc}')
        return driver.find_element(*loc)
    except:
        #     self.handle_exception()
        return driver.find_element(*loc)


caps = {'platformName': 'android',
        'deviceName': 'hw',
        'automationName': 'UiAutomator2',
        # 'appPackage': 'com.xueqiu.android',
        # 'appActivity': '.view.WelcomeActivityAlias',
        # 'autoGrantPermissions': 'true',  #自动同意权限申请
        # 'udid': 'emulator-5556',
        # 'chromedriverExecutable': '/Users/seveniruby/projects/chromedriver/2.20/chromedriver',
        'showChromedriverLog': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
driver.implicitly_wait(10)
print('resdy--------')

if __name__ == '__main__':
    ele = driver.find_element(By.XPATH, "//*[contains(@text,'风险详情')]")
    print('已找到ele,现在去click')
    ele.click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    sleep(2)
    driver.quit()
