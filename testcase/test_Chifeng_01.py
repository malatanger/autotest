# coding:utf-8
"""车辆抽验"""
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Chifeng_pages
import sys
import time
from config import datas_path
from common.get_parameter import Data

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

    @unittest.skip("页面变化")
    def test_01_ky_update(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.ky_menu()
            self.index.update_click()
            self.index.up_carnum_input(param[i]["carnum"])
            self.index.up_zone_click(param[i]["zone"])
            self.index.up_color_click(param[i]["color"])
            self.index.up_problem_click(param[i]["problem"])
            self.index.up_feedback_click(param[i]["feedback"])
            self.index.up_company_input(param[i]["company"])
            self.index.up_numeber_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_update_input(param[i]["bdate"])
            self.index.up_backdate_input(param[i]["edate"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.sleep(2)
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )
    @unittest.skip("页面变化")
    def test_02_ky_select(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 8):
            self.index.sleep(2)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.ky_menu()
            self.index.carnum_input(param[i]["carnum"])
            self.index.number_input(param[i]["number"])
            self.index.group_input(param[i]["group"])
            self.index.bdate_input(param[i]["bdate"])
            self.index.edate_input(param[i]["edate"])
            self.index.zone_click(param[i]["zone"])
            self.index.feedback_click(param[i]["feedback"])
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["carnum"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )
    @unittest.skip("页面变化")
    def test_03_wh_update(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(3)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.wh_menu()
            self.index.update_click()
            self.index.up_carnum_input(param[i]["carnum"])
            self.index.up_zone_click(param[i]["zone"])
            self.index.up_color_click(param[i]["color"])
            self.index.up_problem_click(param[i]["problem"])
            self.index.up_feedback_click(param[i]["feedback"])
            self.index.up_company_input(param[i]["company"])
            self.index.up_numeber_input(param[i]["number"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_update_input(param[i]["bdate"])
            self.index.up_backdate_input(param[i]["edate"])
            self.index.sleep(2)
            self.index.up_yes_click()
            self.index.sleep(2)
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )
    @unittest.skip("页面变化")
    def test_04_wh_select(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(2)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.wh_menu()

            self.index.carnum_input(param[i]["carnum"])
            self.index.number_input(param[i]["number"])
            self.index.group_input(param[i]["group"])
            self.index.bdate_input(param[i]["bdate"])
            self.index.edate_input(param[i]["edate"])
            self.index.zone_click(param[i]["zone"])
            self.index.feedback_click(param[i]["feedback"])
            self.index.select_click()
            self.index.assert_text(
                text=param[i]["carnum"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)'
            )

    def test_05_cz_update(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_update(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(2)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.cz_menu()
            self.index.update_click()
            self.index.up_carnum_input(param[i]["carnum"])
            self.index.up_cz_zone_click(param[i]["zone"])
            self.index.up_color_click(param[i]["color"])
            self.index.up_update_input(param[i]["bdate"])
            self.index.up_group_input(param[i]["group"])
            self.index.up_numeber_input(param[i]["number"])
            self.index.up_problem_input(param[i]["problem"])
            self.index.up_remarks_input(param[i]["remarks"])
            self.index.up_yes_click()
            self.index.sleep(2)
            self.index.assert_text(
                text="录入信息成功！",
                css='css->body > div.el-message.el-message--success > p',
            )

    def test_06_cz_select(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Chifeng_pages.Chifeng_select(driver)
        self.menu = Chifeng_pages.Chifeng_menu(driver)
        for i in range(1, 3):
            self.index.sleep(2)
            self.index.F5()
            # self.menu.kccy_menu()
            self.menu.cz_menu()
            self.index.carnum_input(param[i]["carnum"])
            self.index.number_input(param[i]["number"])
            self.index.bdate_input(param[i]["bdate"])
            self.index.edate_input(param[i]["edate"])
            self.index.sleep(2)
            self.index.select_click()
            self.index.sleep(4)
            self.index.assert_text(
                text=param[i]["carnum"],
                css='css->div.bus_content > div.el-table.el-table--fit.el-table--fluid-height.el-table--scrollable-x.el-table--enable-row-transition > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1)',
            )
