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

# 赵庆利、刘玮、庞晓文、冯伟、呼吸内科门诊、柳小林、消化内科门诊
DOCTOR = '冯伟'
# 呼吸内科门诊、皮肤科门诊、中西医正骨科门诊、消化内科门诊
DEPARTMENT = '中西医正骨科门诊'
# 是否默认选中最新一天放号日期
SELECTEDDATE = True


class Test3(unittest.TestCase):

    def test1(self):

        desired_caps = {}
        desired_caps['noReset'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['udid'] = 'fe2addde'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.hundsun.hospitalcloud.hos.bj.airforceHospital'
        desired_caps['appActivity'] = 'com.hundsun.main.v1.activity.SplashActivity'
        desired_caps["nativeInstrumentsLib"] = False
        desired_caps["interKeyDelay"] = 0
        desired_caps['newCommandTimeout'] = 500

        driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        sleep(5)
        # finds(driver, By.XPATH,
        #       "//android.widget.TextView[contains(@text,'以后再说')]", True, 400).click();

        find(driver, By.XPATH,
             "//android.widget.TextView[@text = '我']", True, 400).click();
        sleep(2)
        finds(driver, By.XPATH,
              "//android.widget.TextView[contains(@text,'我的关注')]").click();
        # find(driver, By.XPATH,
        #      "//android.widget.TextView[contains(@text,'赵庆利')]").click();

        find(driver, By.XPATH,
             "//android.widget.TextView[contains(@text,'%s')]" % DOCTOR, True, 400).click();

        ishave = True
        while ishave:
            try:
                find(driver, By.XPATH,
                     "//android.widget.TextView[contains(@text,'医生介绍')]", True, 2)
                break
            except Exception as err:
                print('医生介绍')
                continue
            ishave = False

        sleep(1)

        # 点击出诊信息按钮
        find(driver, By.XPATH,
             "//android.widget.TextView[contains(@text,'出诊信息')]").click();
        find(driver, By.XPATH,
             "//android.widget.TextView[contains(@text,'出诊信息')]").click();

        sleep(2)

        # 判断是否有号
        DIDNOTHAVE = True
        if ishave:
            try:
                finds(driver, By.XPATH,
                      "//android.widget.TextView[@text = '有号']", True, 3).click()
                ishave = False
                DIDNOTHAVE = False
            except Exception as err:
                print('无号00')
                ishave = True
                DIDNOTHAVE = True

        if DIDNOTHAVE:
            # 滑动医生介绍至顶部
            w = driver.get_window_size()['width']
            h = driver.get_window_size()['height']
            driver.swipe(int(w * 0.5), int(h * 0.75), int(w * 0.5), int(h * 0.1), 100)

            sleep(2)

            if SELECTEDDATE:
                # 等待日期组件出现
                ishave = True
                while ishave:
                    try:
                        find(driver, By.XPATH,
                             "//android.widget.TextView[contains(@text,'全部日期')]", True, 2)
                        sleep(3)
                        break
                    except Exception as err:
                        print('等待日期组件出现')
                        continue
                    ishave = False
                # 点击日期组件
                ishave = True
                while ishave:
                    try:
                        try:
                            find(driver, By.XPATH,
                                 "//android.widget.TextView[contains(@text,'擅长')]", True, 3)
                        except Exception as err:
                            print('选择日期辅助')
                        find(driver, By.XPATH,
                             "//android.widget.TextView[contains(@text,'全部日期')]", True, 2).click()
                        break
                    except Exception as err:
                        print('选择日期')
                        continue
                    ishave = False
                sleep(2)
                # 滑动日期
                w = driver.get_window_size()['width']
                h = driver.get_window_size()['height']
                driver.swipe(int(w * 0.5), (852 if h >= 1600 else 652), int(w * 0.5), int(h * 0.01), 100)
                # 选择最后一个日期
                try:
                    find(driver, By.XPATH,
                         "//android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]", True,
                         2).click()
                except Exception as err:
                    print('选择日期辅助')
                    find(driver, By.XPATH,
                         "//android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]", True,
                         2).click()
                sleep(1)

            # 判断是否有号
            ishave = True
            if ishave:
                try:
                    finds(driver, By.XPATH,
                          "//android.widget.TextView[@text = '有号']", True, 3).click()
                    ishave = False
                except Exception as err:
                    print('无号01')
                    ishave = True

        # 不停刷新到有号出现
        if ishave:
            menzhen = True
            flag = True;
            while flag:
                try:

                    try:
                        while True:
                            try:
                                find(driver, By.XPATH,
                                     "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout//android.widget.ListView/..//android.widget.ImageView",
                                     True, 0.01)
                            except Exception as err:
                                print('############无刷新跳开')
                                break
                            try:
                                find(driver, By.XPATH,
                                     "//android.widget.TextView[contains(@text,'擅长')]", True, 0.01)
                            except Exception as err:
                                print('>>>>>>>>>>>>无刷新辅助')
                        finds(driver, By.XPATH,
                              "//android.widget.TextView[@text = '有号']", True, 0.01).click()
                        break
                    except Exception as err:
                        print('无号02')

                    # if menzhen:
                    #     menzhen = False
                    #     find(driver, By.XPATH,
                    #          "//android.widget.TextView[@text = '全部门诊']", True, 0.01).click();
                    #     find(driver, By.XPATH,
                    #          "//android.widget.ListView/android.widget.TextView[@text = '%s']" % DEPARTMENT, True,
                    #          0.01).click();
                    # else:
                    #     menzhen = True
                    #     find(driver, By.XPATH,
                    #          "//android.widget.TextView[@text = '%s']" % DEPARTMENT, True, 0.01).click();
                    #     find(driver, By.XPATH,
                    #          "//android.widget.ListView/android.widget.TextView[@text = '全部门诊']", True, 0.01).click();

                    # 滑动到提交按钮出现
                    w = driver.get_window_size()['width']

                    h = driver.get_window_size()['height']

                    driver.swipe(int(w * 0.5), int(h * 0.58), int(w * 0.5), int(h * 0.93), 100)

                    finds(driver, By.XPATH,
                          "//android.widget.TextView[@text = '有号']", True, 0.05).click()
                    break
                except Exception as err:
                    print('无号刷新')
                    try:
                        finds(driver, By.XPATH,
                              "//android.widget.TextView[@text = '有号']", True, 0.01).click()
                        break
                    except Exception as err:
                        print('无号03')
                    continue
                flag = False

        # find(driver, By.XPATH,
        #      "//android.widget.TextView[@text = '有号']", True, 0.5).click()

        # 等待请稍候弹窗取消
        ishave = True
        while ishave:
            try:
                find(driver, By.XPATH,
                     "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True, 0.02)
                continue
            except Exception as err:
                print('请稍侯01')
                break
            ishave = False

        # 等待剩余按钮出现，如果卡住了就循环点击有号
        ishave = True
        while ishave:
            try:
                find(driver, By.XPATH,
                      "//android.widget.TextView[contains(@text,'剩余')]", True, 2).click()
                break
            except Exception as err:
                print('剩余')
                try:
                    finds(driver, By.XPATH,
                          "//android.widget.TextView[@text = '有号']", True, 1).click()
                except Exception as err:
                    print('无号04')
                while True:
                    try:
                        find(driver, By.XPATH,
                             "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True,
                             0.02)
                        continue
                    except Exception as err:
                        print('请稍侯02')
                        break
                continue
            ishave = False

        # 等待请稍候弹窗取消
        ishave = True
        while ishave:
            try:
                find(driver, By.XPATH,
                     "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True, 0.02)
                # driver.press_keycode(AndroidKeyCode.BACK)
                continue
            except Exception as err:
                print('请稍侯03')
                break
            ishave = False

        # 等待选择就诊人消失
        ishave = True
        while ishave:
            try:
                try:
                    find(driver, By.XPATH,
                         "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True, 0.02)
                    driver.press_keycode(4)
                except Exception as err:
                    print('请稍侯04')

                try:
                    find(driver, By.XPATH,
                         "//android.widget.TextView[contains(@text,'确认放弃本次挂号')]", True, 0.02)
                    find(driver, By.XPATH,
                         "//android.widget.TextView[contains(@text,'取消')]", True, 0.02).click()
                except Exception as err:
                    print('继续挂号01')

                find(driver, By.XPATH,
                     "//android.widget.TextView[contains(@text,'选择就诊人')]", True, 0.05)
                continue
            except Exception as err:
                print('就诊人回显')
                break
            ishave = False

        # 等待平台服务费出现
        ishave = True
        while ishave:
            try:
                try:
                    find(driver, By.XPATH,
                         "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True, 0.02)
                    driver.press_keycode(4)
                except Exception as err:
                    print('请稍候05')

                try:
                    find(driver, By.XPATH,
                         "//android.widget.TextView[contains(@text,'确认放弃本次挂号')]", True, 0.02)
                    find(driver, By.XPATH,
                         "//android.widget.TextView[contains(@text,'取消')]", True, 0.02).click()
                except Exception as err:
                    print('继续挂号02')

                find(driver, By.XPATH,
                     "//android.widget.TextView[contains(@text,'平台服务费')]", True, 0.05)
                break
            except Exception as err:
                print('平台服务费回显')
                continue
            ishave = False

        # 滑动到提交按钮出现
        w = driver.get_window_size()['width']

        h = driver.get_window_size()['height']

        driver.swipe(int(w * 0.5), int(h * 0.75), int(w * 0.5), int(h * 0.1), 100)

        # find(driver, By.XPATH,
        #      "//android.widget.TextView[contains(@text,'挂号提醒')]", True, 300).click()

        while True:
            try:
                find(driver, By.XPATH,
                     "//android.widget.TextView[contains(@text,'立即提交')]", True, 0.02).click()
                break
            except Exception as err:
                print('没有滑动')
                # 滑动到提交按钮出现
                w = driver.get_window_size()['width']

                h = driver.get_window_size()['height']

                driver.swipe(int(w * 0.5), int(h * 0.75), int(w * 0.5), int(h * 0.1), 200)
                continue

        # # 点击提交按钮
        # find(driver, By.XPATH,
        #      "//android.widget.TextView[contains(@text,'立即提交')]", True, 400).click()

        # 等待请稍候弹窗取消
        ishave = True
        while ishave:
            try:
                find(driver, By.XPATH,
                     "//android.widget.RelativeLayout/android.widget.TextView[contains(@text,'请稍')]", True, 0.02)
                continue
            except Exception as err:
                print('请稍候06')
                break
            ishave = False

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        timeArray = time.strptime(today, "%Y-%m-%d")
        # 当天8点整时间戳
        todayMi = int(time.mktime(timeArray)) + 8 * 60 * 60 + 37.8

        timeOk = True;
        while timeOk:
            sleep(0.05)
            print('延迟')
            if (time.time() >= todayMi):
                timeOk = False;
                break;

        # 点击确定按钮
        find(driver, By.XPATH,
             "//android.widget.TextView[@text = '确定']", True, 400).click()

        sleep(500)

        driver.quit()


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
