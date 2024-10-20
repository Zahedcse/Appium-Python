import unittest
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict
import time

cap: Dict[str, Any] = {
    'platformName': 'iOS',
    'automationName': 'XCUITest',
    'deviceName': 'iPhone 16 Pro',
    'platformVersion': '18.0',
    'bundleId':'com.stucommunify.app',
    'appActivity':'.Settings',
    'language':'en',
    'locale':'US'
}

url = 'http://127.0.0.1:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_element(self) -> None:
        #YourElementAccessibilityID = "/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]"
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Student You're enrolled in an University seeking to access resources, and explore opportunities.")
        el.click()
        email = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Email* you@olivia.com")
        email.send_keys("nsharli8256+200@gmail.com")

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password* Enter password ").click()
        password = (self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Password* Enter password "))
        password.send_keys("Sitakund1#")
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Log in").click()
        time.sleep(5)

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="create-post, tab, 5 of 6").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Social post").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Write something").send_keys("Hello there, creating post using automation")
        # self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="").click()

if __name__ == '__main__':
    unittest.main()