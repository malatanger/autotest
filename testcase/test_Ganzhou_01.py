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

    @Retry.retry(2)
    def test_01_YHBH(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Ganzhou_pages_01.Ganzhou_pages_YHBH(driver)
        self.index.YHBH_click()
        self.index.switch_to_frame('css->#govern-index > iframe')
        self.index.YHBH_menu_click("通报管理")
        self.index.YHBH_tongbao_select_title_input("关于6月1日监测数据的通报")
        self.index.YHBH_tongbao_select()
        self.index.assert_text(
            text="关于6月1日监测数据的通报",
            css='css->#app > div > section > main > div > div:nth-child(2) > div > div.el-table.el-table--fit.el-table--border.el-table--enable-row-transition.el-table--mini'
        )

    @Retry.retry(2)
    def test_02_TJFX(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Ganzhou_pages_01.Ganzhou_pages_YHBH(driver)
        self.index.YHBH_click()
        self.index.switch_to_frame('css->#govern-index > iframe')
        self.index.YHBH_menu_click("通报管理")




