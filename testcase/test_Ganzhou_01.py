# coding:utf-8
import unittest
from common.basepage import Browser_engine
from pages import Ganzhou_pages_01
from common.log import Log
from common.get_parameter import Data
from config import datas_path
import sys


data =  Data(datas_path + "Ganzhou_datas.xlsx", "统计分析")
param = data.get_data()



class Ganzhou_TJFX_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        logger.info('############################### START ###############################')
        driver = Browser_engine.get_browser()
        cls.index = Ganzhou_pages_01.Ganzhou_pages_login(driver)
        cls.index.Ganzhou_open(param[1]["url"])
        cls.index.max_window()
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.login_click()

    @classmethod
    def tearDownClass(cls):
        cls.index = Ganzhou_pages_01.Ganzhou_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def setUp(self):

        self.index.F5()


    def test_01_TJFX(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Ganzhou_pages_01.Ganzhou_pages_TJFX(driver)
        self.index.TJFX_click()

    def test_02_TJFX(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Ganzhou_pages_01.Ganzhou_pages_TJFX(driver)
        self.index.TJFX_click()




