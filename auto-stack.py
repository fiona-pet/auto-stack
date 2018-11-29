# coding=utf-8
import datetime
import unittest
import time

from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

PASSWORD = '850210'

HOME_TABS = {'交易':'com.lphtsccft:id/rb_trade'}

class Test3(unittest.TestCase):

    def test1(self):
        desired_caps = {}
        desired_caps['noReset'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['udid'] = 'fe2addde'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.lphtsccft'
        desired_caps['appActivity'] = 'com.lphtsccft.zhangle.startup.SplashScreenActivity'
        desired_caps["nativeInstrumentsLib"] = False
        desired_caps["interKeyDelay"] = 0
        desired_caps['newCommandTimeout'] = 500

        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        sleep(5)


        # 行情
        find(driver, By.ID, 'com.lphtsccft:id/rb_market', 3).click()

        # 自选股票
        find(driver, By.ID, 'com.lphtsccft:id/tv_title_bar_radio_right', 3).click()

        driver.find_element_by_id('com.lphtsccft:id/rb_market').click()

def buy(driver: WebDriver, trade_code):
    # 交易
    find(driver, By.ID, 'com.lphtsccft:id/rb_trade', 3).click()
    # 买入
    find(driver, By.ID, 'com.lphtsccft:id/trade_portal_normal_buy', 3).click()
    # 是否登陆检查 数据 交易密码
    find(driver, By.ID, 'com.lphtsccft:id/password_edit', 3).send_keys(PASSWORD)
    # 登陆
    find(driver, By.ID, 'com.lphtsccft:id/confirm_text_view', 3).click()
    # 股票号码
    find(driver, By.ID, 'com.lphtsccft:id/trade_editText', 3).send_keys(trade_code)
    # 一手
    find(driver, By.XPATH,
         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.TextView[2]',
         3).click()
    # 买入
    find(driver, By.ID, 'com.lphtsccft:id/tv_trade', 3).click()
    # 确认 订单
    find(driver, By.ID, 'com.lphtsccft:id/dialog_btn_right', 3).click()


def find(driver: WebDriver, by: str = By.ID, value=None, do_wait=True, timeout=20):
    """查找多元素，相同属性元素会返回一个元素合集
    :Args:
         - driver: WebDriver
         - by: 查找类型
         - value: 查找表达式
         - do_wait: 是否等待，默认开启等待
         - timeout: 等待时长，默认20秒内，如果未开启等待该值不生效
    """
    if do_wait:
        return wait(driver, lambda x: x.find_element(by, value), timeout)
    else:
        return driver.find_elements(by, value)


def finds(driver: WebDriver, by: str = By.ID, value=None, do_wait=True, timeout=20):
    """查找多元素，相同属性元素会返回一个元素合集
    :Args:
         - driver: WebDriver
         - by: 查找类型
         - value: 查找表达式
         - do_wait: 是否等待，默认开启等待
         - timeout: 等待时长，默认20秒内，如果未开启等待该值不生效
    """
    if do_wait:
        elements = wait(driver, lambda x: x.find_elements(by, value), timeout)
        elements.reverse()
        for i in elements:
            return i
    else:
        return driver.find_elements(by, value)


def wait(driver: WebDriver, method, timeout=20):
    return WebDriverWait(driver, timeout, 0.01).until(method)


if __name__ == "__main__":
    unittest.main()
