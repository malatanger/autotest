# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Ganzhou_pages_01
import sys
import time
from config import datas_path
from common.get_parameter import Data
from common.basepage import Retry

data = Data(datas_path + "Ganzhou_datas.xlsx", "车辆基本信息统计")
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
        # cls.index.Ganzhou_open("http://10.50.10.117:8080/#/statistics/vehicle_real_situation")
        cls.index.max_window()
        cls.index.Ganzhou_open(param[1]["url"])
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.login_click()

    @classmethod
    def tearDownClass(cls):
        cls.index = Ganzhou_pages_01.Ganzhou_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    # @Retry.retry(2)
    def test_01_diquhuizong(self):
        # 0 地区 1 平台
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Ganzhou_pages_01.Ganzhou_pages_TJFX(driver)
        self.index.TJFX_click()
        self.index.iframe_in()
        # self.index.fristmenu_click(param[1]["firstmenu"])
        self.index.secondmenumenu_click(param[1]["secondmenu"])
        self.index.header_click(param[1]["thirdmenu"])
        self.index.sleep(3)
        self.index.zone_input(1, "赣州")
        self.index.sleep(2)
        #self.index.timeslot_input(3, "2019-07-04", "2019-07-04")
        self.index.sleep(3)
        self.index.platform_input(1,"GBOS")
        #self.index.company_input(3, "3")
        self.index.query_bts(1, "查询")
        self.index.sleep(3)
