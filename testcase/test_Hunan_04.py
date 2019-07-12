# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Hunan_pages
import sys
import time
from config import datas_path
from common.get_parameter import Data
from common.basepage import Retry

data = Data(datas_path + "1.xlsx", "Sheet1")
param = data.get_data()


class Hunan_Assessment_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        # driver = Browser_engine().get_browser()
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.wait(30)
        cls.index.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    @Retry.retry()
    def test_01_studyusers(self):
        for i in range(1, 36):
            self.index.F5()
            self.index.open_Hunan("http://study.hunanlwlk.com/")
            self.index.input(
                "css->#app > div > div:nth-child(1) > div > div > form > div:nth-child(1) > div > div > input",
                param[i]["负责人手机"])
            self.index.input(
                "css->#app > div > div:nth-child(1) > div > div > form > div:nth-child(2) > div > div > input",
                param[i]["初始密码"])
            self.index.click("css->#app > div > div:nth-child(1) > div > div > button")
            self.index.sleep(4)
            self.index.assert_text(
                text="修改密码",
                css='xpath->//*[@id="app"]/div/div[2]/div/div[1]/span'
            )
            self.index.deleteall_cookies()
