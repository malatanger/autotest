# coding:utf-8
"""学时抽查"""
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Chifeng_pages
import sys
import time
from config import datas_path
from common.get_parameter import Data
from common.basepage import Retry

data = Data(datas_path + "Chifeng_datas.xlsx", "客车抽验")
param = data.get_data()


class Chifeng_ky_test(unittest.TestCase):
    """客运"""

    @classmethod
    def setUpClass(cls):
        global logger
        global driver

        logger = Log()
        # 实例化浏览器引擎
        logger.info('############################### START ###############################')
        driver = Browser_engine().get_browser()
        # driver = Browser_engine().get_browser()
        cls.index = Chifeng_pages.Chifeng_pages_login(driver)
        cls.index.max_window()
        cls.index.open_Chifeng(param[1]["url"])
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Chifeng_pages.Chifeng_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_01_jyxs_update(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xscy_menu()
            self.index.sleep(2)
            self.menu.jyxs_menu()
            self.index.update_click()
            self.index.up_numeber_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_problem_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.up_name_input(param[i]["username"])
            self.index.up_cardnum_input(param[i]["number"])
            self.index.up_jyxs_btime(param[i]["btime"])
            self.index.up_jyxs_etime(param[i]["etime"])
            self.index.up_jyxs_zone_click(param[i]["zone"])
            self.index.up_platform_input(param[i]["company"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    def test_02_jyxs_select(self):
        """时间参数中开始时间必须大于结束时间"""
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xscy_menu()
            self.index.sleep(2)
            self.menu.jyxs_menu()
            self.index.cardnum_input(param[i]["number"])
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["bdate"])
            self.index.edate_input(param[i]["edate"])
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["company"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )

    def test_03_jsyxs_update(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xscy_menu()
            self.index.sleep(2)
            self.menu.jsyxs_menu()
            self.index.update_click()
            self.index.up_numeber_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_problem_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.up_name_input(param[i]["username"])
            self.index.up_cardnum_input(param[i]["number"])
            self.index.up_jyxs_btime(param[i]["btime"])
            self.index.up_jyxs_etime(param[i]["etime"])
            self.index.up_jyxs_zone_click(param[i]["zone"])
            self.index.up_platform_input(param[i]["company"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    def test_04_jyxs_select(self):
        """时间参数中开始时间必须大于结束时间"""
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xscy_menu()
            self.index.sleep(2)
            self.menu.jsyxs_menu()
            self.index.cardnum_input(param[i]["number"])
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["bdate"])
            self.index.edate_input(param[i]["edate"])
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["company"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )
