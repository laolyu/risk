# $language = "Python3"
# $interface = "1.0"
import sys
import subprocess
import time

import pyperclip
from time import sleep
from loguru import logger
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


# sys.path.append("F:\\py")
# from demo.woods import dialogg


def driver():
    logger.info('ready for driver')
    service = 'http://localhost:4723/wd/hub'
    caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        # 'noSign': True,
        'autoGrantPermissions': True,
        'newCommandTimeout': '900',
        'automationName': 'UiAutomator2',
        # 'udid': 'PWH4C19613004851',
        'udid': '6HJDU19912010450',
        # 'unlockType': 'password',
        # 'unlockKey': '123456'
    }
    driver = webdriver.Remote(service, caps)
    logger.info('the driver is ready')
    return driver


def apkpath():
    # title = 'paste'
    # message = 'Please enter the apk path.                             '
    # path_input = dialogg.get_text_input(title, message)

    # path_input = crt.Dialog.Prompt(
    #     "Please enter the apk path.Thank you!",
    #     "paste",
    #     "",
    #     False)

    path_input = pyperclip.paste()
    logger.info(path_input)
    path_base = r'F:/apps/apk/new/'
    file = path_base + path_input + '.apk'
    return file


def AppInst(driver, apkpath):  # 安装pak
    udid = '6HJDU19912010450'
    cmd = f'adb -s {udid} install {apkpath}'
    cmd_password = f'adb -s  {udid} shell input text 123456'

    alertTitle = 'android:id/alertTitle'
    alert_continue = 'android:id/button1'

    continue_button = 'com.android.packageinstaller:id/continue_button'
    ok_button = 'com.android.packageinstaller:id/ok_button'
    done_button = 'com.android.packageinstaller:id/done_button'

    risk_icon = 'com.huawei.appmarket:id/tips_card_risk_icon'
    continue_hw = 'com.huawei.appmarket:id/hidden_card_install_button_continue'

    alert_installed = 'com.huawei.systemmanager:id/messagecontent'

    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if find_id(driver, alertTitle):
            logger.info('安装,提示风险')
            driver.find_element_by_id(alert_continue).click()

        if find_id(driver, risk_icon, 30):
            logger.info('安装来源,发现风险项')
            now = time.strftime("%Y-%m%d-%H%M_%S", time.localtime(time.time()))
            # driver.get_screenshot_as_file(f'F:\screenshot\risk_{now}.png')
            driver.save_screenshot('test_login_error_02.png')
            driver.find_element_by_id(continue_hw).click()
            subprocess.Popen(cmd_password, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if find_id(driver, continue_button):
            logger.info('click continue_button')
            driver.find_element_by_id(continue_button).click()

            if find_id(driver, ok_button, 20):
                logger.info('click ok_button')
                driver.find_element_by_id(ok_button).click()
            if find_id(driver, done_button, 20):
                logger.info('click done_button')
                driver.find_element_by_id(done_button).click()

        if find_id(driver, alert_installed):
            logger.info('风险软件')
            now = time.strftime("%Y-%m%d-%H%M_%S", time.localtime(time.time()))
            driver.get_screenshot_as_file(f'F:\screenshot\risk_{now}.png')

        out, err = p.communicate(timeout=60)
        out_info = out.decode('gbk')
        logger.info(out_info)

    except Exception as e:
        logger.info(e)


def find_id(driver, el, length=5):
    try:
        WebDriverWait(driver, length).until(lambda x: x.find_element_by_id(el))
        sleep(2)
        logger.info(f'found {el}')
        return True
    except Exception as e:
        # print(e)
        logger.info(e)
        return False


logger.add("F:/log/ins_log_{time}.log", rotation="500MB", encoding="utf-8", enqueue=True, compression="zip", retention="10 days")
try:
    file = apkpath()
    f = open(file)
    f.close()
    driver = driver()
    AppInst(driver, file)
    driver.quit()
except IOError as e:
    logger.info(e)
except Exception as e:
    logger.info(e)
