# coding:utf-8
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

    @Retry.retry()
    def test_01_jyxs_update(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(function.__name__))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.tq_menu()
            self.index.update_click()
            self.index.up_xxfb_number_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_xxfb_btime_input(param[i]["btime"])
            self.index.up_content_input(param[i]["problem"])
            self.index.up_range_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    @Retry.retry()
    def test_02_jyxs_select(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.tq_menu()
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["btime"])
            self.index.edate_input(param[i]["btime"])
            self.index.sleep(2)
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["number"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )

    @Retry.retry()
    def test_03_jyxs_update(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.tz_menu()
            self.index.update_click()
            self.index.up_xxfb_number_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_xxfb_btime_input(param[i]["btime"])
            self.index.up_content_input(param[i]["problem"])
            self.index.up_range_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    @Retry.retry()
    def test_04_jyxs_select(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.tz_menu()
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["btime"])
            self.index.edate_input(param[i]["etime"])
            self.index.sleep(2)
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["number"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )

    @Retry.retry()
    def test_05_jyxs_update(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.qt_menu()
            self.index.update_click()
            self.index.up_xxfb_number_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_xxfb_btime_input(param[i]["btime"])
            self.index.up_content_input(param[i]["problem"])
            self.index.up_range_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    @Retry.retry()
    def test_06_jyxs_select(self):
        """时间参数中开始时间必须大于结束时间"""
        i = 1
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 10):
            self.index.sleep(3)
            self.index.F5()
            self.menu.xxfb_menu()
            self.index.sleep(2)
            self.menu.qt_menu()
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["btime"])
            self.index.edate_input(param[i]["btime"])
            self.index.sleep(2)
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["number"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )
