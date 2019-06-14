# coding:utf-8
"""
考核通报
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

data = Data(datas_path + "Hunan_datas.xlsx", "Assessment")
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
        cls.index.open_Hunan(param[1]["url"])
        cls.index.username_input(param[1]["username"])
        cls.index.password_input(param[1]["password"])
        cls.index.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.index = Hunan_pages.Hunan_pages_login(driver)
        cls.index.quit()
        logger.info('################################ End ################################')

    # @unittest.skip("调试")
    @Retry.retry()
    def test_001_zoneassessment_month(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[1]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.sleep(3)
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zoneassessment_type_choose(param[1]["assessmenttype"])
        self.index.zoneassessment_zone_input(param[1]["zone"])
        self.index.zoneassessment_month_time_input(param[1]["btime"])
        self.index.zoneassessment_cartype_click()
        self.index.zoneassessment_cartype_check(param[1]["cartype"])
        self.index.zoneassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_002_zoneassessment_year(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[2]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.sleep(3)
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zoneassessment_type_choose(param[2]["assessmenttype"])
        self.index.sleep(3)
        self.index.zoneassessment_zone_input(param[2]["zone"])
        self.index.zoneassessment_year_time_input(param[2]["btime"])
        self.index.zoneassessment_cartype_click()
        self.index.zoneassessment_cartype_check(param[2]["cartype"])
        self.index.zoneassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
            sec=50
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_003_zoneassessment_day(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[3]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.sleep(3)
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zoneassessment_type_choose(param[3]["assessmenttype"])
        self.index.sleep(3)
        self.index.zoneassessment_zone_input(param[3]["zone"])
        self.index.zoneassessment_btime_input(param[3]["btime"])
        self.index.zoneassessment_etime_input(param[3]["etime"])
        self.index.zoneassessment_cartype_click()
        self.index.zoneassessment_cartype_check(param[3]["cartype"])
        self.index.zoneassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    #@unittest.skip("调试")
    @Retry.retry()
    def test_004_Companyassessment_month(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[4]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.companyassessment_click()
        self.index.companyassessment_company_input(param[4]["company"])
        self.index.companyassessment_type_choose(param[4]["assessmenttype"])
        self.index.companyassessment_zone_input(param[4]["zone"])
        self.index.companyassessment_month_time_input(param[4]["btime"])
        self.index.companyassessment_cartype_click()
        self.index.companyassessment_cartype_check(param[4]["cartype"])
        self.index.companyassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_005_Companyassessment_year(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[5]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.companyassessment_click()
        self.index.companyassessment_company_input(param[5]["company"])
        self.index.companyassessment_type_choose(param[5]["assessmenttype"])
        self.index.companyassessment_zone_input(param[5]["zone"])
        self.index.companyassessment_year_time_input(param[5]["btime"])
        self.index.companyassessment_cartype_click()
        self.index.companyassessment_cartype_check(param[5]["cartype"])
        self.index.companyassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
            sec=50
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_006_Companyassessment_day(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[6]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.companyassessment_click()
        self.index.companyassessment_company_input(param[6]["company"])
        self.index.companyassessment_type_choose(param[6]["assessmenttype"])
        self.index.companyassessment_zone_input(param[6]["zone"])
        self.index.companyassessment_btime_input(param[6]["btime"])
        self.index.companyassessment_etime_input(param[6]["etime"])
        self.index.companyassessment_cartype_click()
        self.index.companyassessment_cartype_check(param[6]["cartype"])
        self.index.companyassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_007_Platformassessment_month(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[7]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.platformassessment_click()
        self.index.platformassessment_platform_input(param[7]["platform"])
        self.index.platformassessment_type_choose(param[7]["assessmenttype"])
        self.index.platformassessment_zone_input(param[7]["zone"])
        self.index.platformassessment_month_time_input(param[7]["btime"])
        self.index.platformassessment_cartype_click()
        self.index.platformassessment_cartype_check(param[7]["cartype"])
        self.index.platformassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_008_Platformassessment_year(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[8]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.platformassessment_click()
        self.index.platformassessment_platform_input(param[8]["platform"])
        self.index.platformassessment_type_choose(param[8]["assessmenttype"])
        self.index.platformassessment_zone_input(param[8]["zone"])
        self.index.platformassessment_year_time_input(param[8]["btime"])
        self.index.platformassessment_cartype_click()
        self.index.platformassessment_cartype_check(param[8]["cartype"])
        self.index.platformassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
            sec=50
        )

    # @unittest.skip("调试")
    @Retry.retry()
    def test_009_Platformassessment_day(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[9]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.platformassessment_click()
        self.index.platformassessment_platform_input(param[9]["platform"])
        self.index.platformassessment_type_choose(param[9]["assessmenttype"])
        self.index.platformassessment_zone_input(param[9]["zone"])
        self.index.platformassessment_btime_input(param[9]["btime"])
        self.index.platformassessment_etime_input(param[9]["etime"])
        self.index.platformassessment_cartype_click()
        self.index.platformassessment_cartype_check(param[9]["cartype"])
        self.index.platformassessment_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
        )

    @Retry.retry()
    def test_010_Details_Install(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[10]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsinstall_carnum_input(param[10]["carnumber"])
        self.index.detailsinstall_zone_input(param[10]["zone"])
        self.index.detailsinstall_platform_input(param[10]["platform"])
        self.index.detailsinstall_company_input(param[10]["company"])
        self.index.detailsinstall_time_input(param[10]["btime"])
        self.index.detailsinstall_cartype_choose(param[10]["cartype"])
        self.index.detailsinstall_carstate_choose(param[10]["carstate"])
        self.index.detailsinstall_installtype_click(param[10]["installtype"])
        self.index.detailsinstall_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicleinstall_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_011_Details_Online(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[11]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsonline_click()
        self.index.detailsonline_carnum_input(param[11]["carnumber"])
        self.index.detailsonline_zone_input(param[11]["zone"])
        self.index.detailsonline_platform_input(param[11]["platform"])
        self.index.detailsonline_company_input(param[11]["company"])
        self.index.detailsonline_btime_input(param[11]["btime"])
        self.index.detailsonline_etime_input(param[11]["etime"])
        self.index.detailsonline_cartype_choose(param[11]["cartype"])
        self.index.detailsonline_onlinetype_click(param[11]["onlinetype"])
        self.index.detailsonline_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicleuplinerate_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_012_Details_Patform(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[12]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailspatform_click()
        self.index.detailspatform_zone_input(param[12]["zone"])
        self.index.detailspatform_platform_input(param[12]["platform"])
        self.index.detailspatform_btime_input(param[12]["btime"])
        self.index.detailspatform_etime_input(param[12]["etime"])
        self.index.detailspatform_cartype_choose(param[12]["cartype"])
        self.index.detailspatform_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicleconnectrate_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_013_Details_Trail(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[13]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailstrail_click()
        self.index.detailstrail_zone_input(param[13]["zone"])
        self.index.detailstrail_company_input(param[13]["company"])
        self.index.detailstrail_platform_input(param[13]["platform"])
        self.index.detailstrail_btime_input(param[13]["btime"])
        self.index.detailstrail_etime_input(param[13]["etime"])
        self.index.detailstrail_cartype_choose(param[13]["cartype"])
        self.index.detailstrail_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicletrail_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_014_Details_Data(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[14]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsdata_click()
        self.index.detailsdata_zone_input(param[14]["zone"])
        self.index.detailsdata_company_input(param[14]["company"])
        self.index.detailsdata_platform_input(param[14]["platform"])
        self.index.detailsdata_btime_input(param[14]["btime"])
        self.index.detailsdata_etime_input(param[14]["etime"])
        self.index.detailsdata_cartype_choose(param[14]["cartype"])
        self.index.detailsdata_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehiclestandard_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_015_Details_Speeding(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[15]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsspeeding_click()
        self.index.detailsspeeding_zone_input(param[15]["zone"])
        self.index.detailsspeeding_company_input(param[15]["company"])
        self.index.detailsspeeding_platform_input(param[15]["platform"])
        self.index.detailsspeeding_btime_input(param[15]["btime"])
        self.index.detailsspeeding_etime_input(param[15]["etime"])
        self.index.detailsspeeding_cartype_choose(param[15]["cartype"])
        self.index.detailsspeeding_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicleoverspeed_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_016_Details_Tired(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[16]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailstired_click()
        self.index.detailstired_zone_input(param[16]["zone"])
        self.index.detailstired_company_input(param[16]["company"])
        self.index.detailstired_platform_input(param[16]["platform"])
        self.index.detailstired_btime_input(param[16]["btime"])
        self.index.detailstired_etime_input(param[16]["etime"])
        self.index.detailstired_cartype_choose(param[16]["cartype"])
        self.index.detailstired_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicletired_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_017_Details_Drift(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[17]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsdrift_click()
        self.index.detailsdrift_zone_input(param[17]["zone"])
        self.index.detailsdrift_company_input(param[17]["company"])
        self.index.detailsdrift_platform_input(param[17]["platform"])
        self.index.detailsdrift_btime_input(param[17]["btime"])
        self.index.detailsdrift_etime_input(param[17]["etime"])
        self.index.detailsdrift_cartype_choose(param[17]["cartype"])
        self.index.detailsdrift_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicledrift_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_018_Details_Response(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[18]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.details_click()
        self.index.detailsresponse_click()
        self.index.detailsresponse_zone_input(param[18]["zone"])
        self.index.detailsresponse_company_input(param[18]["company"])
        self.index.detailsresponse_btime_input(param[18]["btime"])
        self.index.detailsresponse_etime_input(param[18]["etime"])
        self.index.detailsresponse_atwork_choose(param[18]["atwork"])
        self.index.detailsresponse_responsetype_choose(param[18]["responsetype"])
        self.index.detailsresponse_select_click()
        self.index.assert_text(
            text='没有相关数据',
            css='css->#check_report_vehicleresponse_detail_table_table > tbody > tr',
            asserttype='not in'
        )

    @Retry.retry()
    def test_019_Zero_Zone_month(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[19]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerozone_type_choose(param[19]["assessmenttype"])
        self.index.zerozone_zone_input(param[19]["zone"])
        self.index.zerozone_month_time_input(param[19]["btime"])
        self.index.zerozone_cartype_click()
        self.index.zerozone_cartype_check(param[19]["cartype"])
        self.index.zerozone_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    @Retry.retry()
    def test_020_Zero_Zone_year(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[20]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerozone_type_choose(param[20]["assessmenttype"])
        self.index.zerozone_zone_input(param[20]["zone"])
        self.index.zerozone_year_time_input(param[20]["btime"])
        self.index.zerozone_cartype_click()
        self.index.zerozone_cartype_check(param[20]["cartype"])
        self.index.zerozone_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    @Retry.retry()
    def test_021_Zero_Zone_day(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[21]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerozone_type_choose(param[21]["assessmenttype"])
        self.index.zerozone_zone_input(param[21]["zone"])
        self.index.zerozone_btime_input(param[21]["btime"])
        self.index.zerozone_etime_input(param[21]["etime"])
        self.index.zerozone_cartype_click()
        self.index.zerozone_cartype_check(param[21]["cartype"])
        self.index.zerozone_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    @Retry.retry()
    def test_022_Zero_Company_month(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[22]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerocompany_click()
        self.index.zerocompany_type_choose(param[22]["assessmenttype"])
        self.index.zerocompany_zone_input(param[22]["zone"])
        self.index.zerocompany_month_time_input(param[22]["btime"])
        self.index.zerocompany_cartype_click()
        self.index.zerocompany_cartype_check(param[22]["cartype"])
        self.index.zerocompany_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )

    @Retry.retry()
    def test_023_Zero_Company_year(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[23]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerocompany_click()
        self.index.zerocompany_type_choose(param[23]["assessmenttype"])
        self.index.zerocompany_zone_input(param[23]["zone"])
        self.index.zerocompany_year_time_input(param[23]["btime"])
        self.index.zerocompany_cartype_click()
        self.index.zerocompany_cartype_check(param[23]["cartype"])
        self.index.zerocompany_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr",
            sec=30
        )

    @Retry.retry()
    def test_024_Zero_Company_day(self):
        logger.info("开始用例： {0} , 参数选择： {1}".format(
            sys._getframe().f_code.co_name,
            param[24]["testname"]))
        self.index = Hunan_pages.Hunan_pages_Assessment(driver)
        self.index.F5()
        self.index.assessment_bt_click()
        self.index.sleep(3)
        self.index.zero_click()
        self.index.zerocompany_click()
        self.index.zerocompany_type_choose(param[24]["assessmenttype"])
        self.index.zerocompany_zone_input(param[24]["zone"])
        self.index.zerocompany_btime_input(param[24]["btime"])
        self.index.zerocompany_etime_input(param[24]["etime"])
        self.index.zerocompany_cartype_click()
        self.index.zerocompany_cartype_check(param[24]["cartype"])
        self.index.zerocompany_select_bt_click()
        self.index.assert_text(
            text="合计",
            css="css->tfoot > tr"
        )
