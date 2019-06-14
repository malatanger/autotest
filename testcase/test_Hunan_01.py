# coding:utf-8
"""
基本信息-车辆信息
"""
import unittest
from common.basepage import Browser_engine
from common.log import Log
from pages import Hunan_pages
import sys
import time
from config import datas_path
from common.get_parameter import Data
from common.basepage import Retry

data = Data(datas_path + "Hunan_datas.xlsx", "CarInfo")
param = data.get_data()


class Hunan_CarInfo_test(unittest.TestCase):

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
        cls.index.max_window()
        cls.index.open_Hunan(param[1]["url"])
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    @Retry.retry()
    def test_001_SelectTheCar_area(self):
        """
        查询指定地区车辆基本信息
        :return:
        """
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_BaseInfo(driver)
        self.index.F5()
        self.index.move_settings()
        self.index.baseinfo_click()
        try:
            self.index.carinfo_zone_input(param[1]["zone1"])  # 地区
            self.index.carinfo_platform_input(param[1]["platform"])  # 接入平台
            self.index.carinfo_company_input(param[1]["company"])  # 企业
            self.index.carinfo_cartype_click()
            # self.index.carinfo_cartype_choose(param[1]["cartype1"])  # 类型1
            if param[1]["deletecheck"] == "YES":
                self.index.carinfo_deletcheck_click()
            self.index.carinfo_carstate_click()
            self.index.carinfo_carstate_choose(param[1]["carstate"])
            self.index.carinfo_select_bt_click()
        except KeyError as e:
            logger.error("参数错误:{0}".format(e))
            raise
        self.index.assert_text(
            text=param[1]["zone"],
            css="css->#vehicleManage_tables_table > tbody > tr:nth-child(1)"
        )

    @Retry.retry()
    def test_002_SelectTheCar_platform(self):
        """
        查询指定平台车辆基本信息
        :return:
        """
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_BaseInfo(driver)
        self.index.F5()
        self.index.move_settings()
        self.index.baseinfo_click()
        self.index.carinfo_zone_input(param[2]["zone"])  # 地区
        self.index.carinfo_platform_input(param[2]["platform"])  # 接入平台
        self.index.carinfo_company_input(param[2]["company"])  # 企业
        self.index.carinfo_cartype_click()
        # self.index.carinfo_cartype_choose(param[1]["cartype1"])  # 类型1
        if param[1]["deletecheck"] == "YES":
            self.index.carinfo_deletcheck_click()
        self.index.carinfo_carstate_click()
        self.index.carinfo_carstate_choose(param[2]["carstate"])
        self.index.carinfo_select_bt_click()
        self.index.assert_text(
            text=param[2]["platform"],
            css="css->#vehicleManage_tables_table > tbody > tr:nth-child(1)"
        )

    @Retry.retry()
    def test_003_SelectTheCar_company(self):
        """
        查询指定企业车辆基本信息
        :return:
        """
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_BaseInfo(driver)
        self.index.F5()
        self.index.move_settings()
        self.index.baseinfo_click()
        self.index.carinfo_zone_input(param[3]["zone"])  # 地区
        self.index.carinfo_platform_input(param[3]["platform"])  # 接入平台
        self.index.carinfo_company_input(param[3]["company"])  # 企业
        self.index.carinfo_cartype_click()
        # self.index.carinfo_cartype_choose(param[1]["cartype1"])  # 类型1
        if param[1]["deletecheck"] == "YES":
            self.index.carinfo_deletcheck_click()
        self.index.carinfo_carstate_click()
        self.index.carinfo_carstate_choose(param[3]["carstate"])
        self.index.carinfo_select_bt_click()
        self.index.assert_text(
            text=param[3]["company"],
            css="css->#vehicleManage_tables_table > tbody > tr:nth-child(1)"
        )

    @Retry.retry()
    def test_004_SelectTheCar_Synch(self):
        """
        根据车牌号查询并同步车辆信息
        :return:
        """
        logger.info("开始用例: {0}".format(sys._getframe().f_code.co_name))
        self.index = Hunan_pages.Hunan_pages_BaseInfo(driver)
        self.index.F5()
        self.index.move_settings()
        self.index.baseinfo_click()
        self.index.carinfo_carnum_input(param[1]["carnumber"])
        self.index.carinfo_select_bt_click()
        self.index.assert_text(
            text=param[1]["carnumber"],
            css="css->#vehicleManage_tables_table > tbody > tr:nth-child(1)"
        )
        self.index.carinfo_chooseinfo_click()
        self.index.carinfo_synch_bt_click_()
        self.index.carinfo_synch_YES_click()
        self.index.assert_text(
            text="同步成功",
            css="css->.layui-layer-content.layui-layer-padding"
        )
    # @Retry.retry()
    # def test_005(self):
    #     self.index.assert_text(
    #         text="同步成功",
    #         css="css->.layui-layer-content.layui-layer-padding"
    #     )