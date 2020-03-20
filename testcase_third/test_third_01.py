# coding:utf-8
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Third_pages_01
import sys
import time
from config import *
from common.get_parameter import Data
from common.basepage import Retry

data = Data(datas_path + "Third_datas.xls", "山西")
param = data.get_data()

class Third_01_clazs_test(unittest.TestCase):
    """车辆安装数"""

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        logger.info('############################### START ###############################')
        driver = Browser_engine.get_browser()
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.max_window()
        cls.index.Third_open(param[1]["url"])
        cls.index.js(login_js)
        cls.index.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    # @Retry.retry(2)
    def test_01_zone(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(1, 3):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            # self.index.fristmenu_click(param[1]["firstmenu"])
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.sleep(3)
            # self.index.day_input(ele_menu,"2019-07-04")
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            # self.index.sleep(3)
            # self.index.platform_input(ele_menu,"GBOS")
            # self.index.company_input(ele_menu, "3")
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-RegionalSummary"]/div/div[2]/div[1]/div[3]/table/tbody',
            )

    # @Retry.retry(2)
    def test_02_platform(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(3, 5):
            self.index.F5()
            self.index.TJFX_click()
            # self.index.fristmenu_click(param[1]["firstmenu"])
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(2)  # 接入平台汇总
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.sleep(3)
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.sleep(5)
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-AccessPlatformSummary"]/div/div[2]/div[1]/div[3]/table/tbody'
            )

    def test_03_company(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(5, 7):
            self.index.F5()
            self.index.TJFX_click()
            # self.index.fristmenu_click(param[1]["firstmenu"])
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(3)  # 企业汇总
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.sleep(3)
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.sleep(5)
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-EnterpriseSummary"]/div/div[2]/div[1]/div[3]/table/tbody'
            )

    def test_04_cars(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(7, 8):
            self.index.F5()
            self.index.TJFX_click()
            # self.index.fristmenu_click(param[1]["firstmenu"])
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(4)  # 车辆安装明细
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.sleep(3)
            self.index.carnum_input(ele_menu, param[i]["carnum"])
            self.index.day_input(ele_menu, param[i]["btime"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.GPS_click(ele_menu, param[i]["GPS"])
            self.index.query_bts(ele_menu, "查询")
            self.index.sleep(5)
            self.index.assert_text(
                text=param[i]["carnum"],
                css='xpath->//*[@id="pane-DetailsOfVehicleInstallation"]/div/div[2]/div[1]/div[3]/table/tbody'
            )

    def test_05_newcars(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(7, 13):
            self.index.F5()
            self.index.TJFX_click()
            # self.index.fristmenu_click(param[1]["firstmenu"])
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(5)  # 企业汇总
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.sleep(3)
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.carnum_input(ele_menu, param[i]["carnum"])
            self.index.query_bts(ele_menu, "查询")
            self.index.sleep(5)
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-InstallationOfNewVehicles"]/div/div[2]/div[1]/div[3]/table/tbody'
            )


class Third_02_clzxl_test(unittest.TestCase):
    """车辆在线率"""

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        logger.info('############################### START ###############################')
        driver = Browser_engine.get_browser()
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.max_window()
        cls.index.Third_open(param[1]["url"])
        cls.index.js(login_js)
        cls.index.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    @Retry.retry(2)
    def test_01_zone(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(13, 15):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.month_input(ele_menu, param[i]["month"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-first"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )

    def test_02_platform(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(15, 17):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(2)  # 平台汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.month_input(ele_menu, param[i]["month"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.plattype_click(ele_menu, param[i]["plattype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-second"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )

    def test_03_company(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(17, 19):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(3)  # 企业汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.month_input(ele_menu, param[i]["month"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-third"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )

    def test_04_car(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(19, 21):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(4)  # 车辆汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.month_input(ele_menu, param[i]["month"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.carnum_input(ele_menu, param[i]["carnum"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="",
                css='xpath->//*[@id="pane-fourth"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )


class Third_03_clsxtj_test(unittest.TestCase):
    """车辆上线统计"""

    @classmethod
    def setUpClass(cls):
        global logger
        global driver
        logger = Log()
        logger.info('############################### START ###############################')
        driver = Browser_engine.get_browser()
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.max_window()
        cls.index.Third_open(param[1]["url"])
        cls.index.js(login_js)
        cls.index.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.index = Third_pages_01.Third_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    def test_01_zone(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(21, 23):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.daysslot_input(ele_menu, param[i]["btime"],param[i]["etime"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-first"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )
    def test_02_platform(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(21, 23):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-second"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )
    def test_03_company(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(21, 23):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-third"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )
    def test_04_car(self):
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Third_pages_01.Third_pages_TJFX(driver)
        for i in range(21, 23):  # 文档中参数序号
            self.index.F5()
            self.index.TJFX_click()
            self.index.secondmenumenu_click(param[i]["secondmenu"])
            self.index.header_click(param[i]["thirdmenu"])
            ele_menu = self.index.getthirdmenu_ele(1)  # 地区汇总
            self.index.sleep(2)
            self.index.zone_input(ele_menu, param[i]["zone"])
            self.index.platform_input(ele_menu, param[i]["platform"])
            self.index.daysslot_input(ele_menu, param[i]["btime"], param[i]["etime"])
            self.index.company_input(ele_menu, param[i]["company"])
            self.index.cartype_click(ele_menu, param[i]["cartype"])
            self.index.query_bts(ele_menu, "查询")
            self.index.assert_text(
                text="合计",
                css='xpath->//*[@id="pane-forth"]/div/div[2]/div[1]/div[3]/table/tbody/tr[last()]',
            )
