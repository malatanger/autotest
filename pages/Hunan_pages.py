# coding:utf-8
from common.basepage import pyselenium


class Hunan_pages_login(pyselenium):
    """登录"""

    def open_Hunan(self, URL):
        self.open(URL)

    def username_input(self, username):
        self.input("css->#txtUser", username)

    def password_input(self, password):
        self.input("css->#txtPwd", password)

    def click_login(self):
        self.click("css->.login-btn")


class Hunan_pages_BaseInfo(pyselenium):
    """
    基本信息车辆管理
    carinfo* -- 车辆基本信息
    """

    def move_settings(self):
        """移动到设置图标"""
        self.move_to_element("css->#home-down-icon-level")

    def baseinfo_click(self):
        """点击基本信息"""
        self.click("css->#base_info_level")

    def carinfo_carnum_input(self, car_numeber):
        """输入车牌号"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text0_show", car_numeber)

    def carinfo_select_bt_click(self):
        """查询"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button0_btn")

    def carinfo_chooseinfo_click(self):
        """选择第一条车辆信息"""
        self.click("css->#vehicleManage_tables_table > tbody > tr:nth-child(1)")

    def carinfo_synch_bt_click_(self):
        """点击同步按钮"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form1_button1_btn")

    def carinfo_synch_YES_click(self):
        """"确认同步"""
        self.click("css->#layui-layer5 > div.layui-layer-btn > a.layui-layer-btn0")

    def carinfo_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->input#vehicleManage_tables_div_queyFrom0_form0_text1_show", zone)
        # self.wait(5)
        self.click("xpath->//li[contains(text(),'{0}')]".format(zone))

    def carinfo_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text3_show", platform)
        self.click("xpath->//li[contains(text(),'{0}')]".format(platform))

    def carinfo_company_input(self, company):
        """输入企业"""
        self.input("css->#vehicleManage_tables_div_queyFrom0_form0_text2_show", company)
        self.click("xpath->//li[contains(text(),'{0}')]".format(company))

    def carinfo_cartype_click(self):
        """点击车辆类型选择框"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_select0 > input")

    def carinfo_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))

    def carinfo_deletcheck_click(self):
        """删除条件选择"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_checkBox0_check")

    def carinfo_carstate_click(self):
        """点击状态选择框"""
        self.click("css->#vehicleManage_tables_div_queyFrom0_form0_select2 > input")

    def carinfo_carstate_choose(self, carstate):
        # self.get_text("xpath->//div/ul/li[contains(text(),'{0}')]".format(carstate))
        """选择状态"""
        self.click(
            "xpath->//*[@id='vehicleManage_tables_div_queyFrom0_form0_select2']/ul/li[contains(text(),'{0}')]".format(
                carstate))


class Hunan_pages_Statistic(pyselenium):
    """
    统计分析
    installzonedata* - 地区汇总
    """

    def statistic_bt_click(self):
        # self.click("css->ul.left-ico-list > li[data-control='home_tjfx'] > a.page-load[modular-name='统计分析']")
        self.click("xpath->//*[@id='home-main']/div[1]/ul[2]/li[4]/a")

    def installzonedata_select_bt_click(self):
        """点击查询"""
        self.click("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_button1_btn")

    def installzonedata_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_text0_show", zone)
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def installzonedata_btime_input(self, btime):
        """开始时间和结束时间"""
        self.clear_input_enter("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
                               btime)

    def installzonedata_etime_input(self, etime):
        """结束时间"""
        self.clear_input_enter("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
                               etime)

    def installzonedata_cartype_click(self):
        self.click("css->#report_vehicleinstall_table_div_tabs0_content_panel0_form0_vehicleTypeTree0 > input")

    def installzonedata_cartype_check(self, cartype):
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))


class Hunan_pages_Assessment(pyselenium):
    """
    考核通报
    zoneassessment_* - 地区考核查询
    companyassessment_* - 企业考核查询
    platformassessment_* - 服务商考核查询
    detailsinstall_* - 考核明细-入网统计
    detailsonline_* - 考核明细-在线统计
    detailstrail_* - 轨迹完整率
    detailsdata_* - 数据合格率
    detailsspeeding_* - 超速
    detailstired_* - 疲驾
    detailstdrift_* - 漂移
    detailstresponse_* - 查岗
    """

    def assessment_bt_click(self):
        """点击考核通报"""
        self.click("xpath->//*[@id='home-main']/div[1]/ul[2]/li[1]/a")

    # --------------------------------------------------------- 地区考核 ------------------------------------------------------------------

    def zoneassessment_select_bt_click(self):
        """地区考核查询按钮"""
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_button1_btn")

    def zoneassessment_type_choose(self, assessmenttype):
        """选择考核类型"""
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click("xpath->//li[contains(text(),'{0}')]".format(assessmenttype))

    def zoneassessment_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_text0_show", zone)
        # report_zoneCheckRank_table_div_tabs0_content_panel0_form0_text0_show
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def zoneassessment_month_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def zoneassessment_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_date1_txt", time)

    def zoneassessment_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_select1 > input")

    def zoneassessment_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click("xpath->//li[contains(text(),'{0}')]".format(cartype))

    def zoneassessment_btime_input(self, btime):
        """地区考核开始时间"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
                               btime)

    def zoneassessment_etime_input(self, etime):
        """地区考核结束时间"""
        self.clear_input_enter("css->#report_zoneCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
                               etime)

    # --------------------------------------------------------- 企业考核 ------------------------------------------------------------------

    def companyassessment_click(self):
        """选择企业考核排名"""
        self.js(
            "document.querySelector('#checkmanage-index > div > div.check-manage-title > ul > li:nth-child(2) > ul').style.display='block'")
        self.sleep(1)
        self.click("xpath->//li[@data-control='checkManage_companyRank']/a/span[contains(text(),'企业考核排名')]")

    def companyassessment_company_input(self, company):
        """输入企业名称"""
        self.input("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_text0_show", company)
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                company))

    def companyassessment_type_choose(self, assessmenttype):
        """选择考核类型"""
        self.click("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click(
            "xpath->//*[@id='report_companyCheckRank_table_div_tabs0_content_panel0_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                assessmenttype))

    def companyassessment_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_text1_show", zone)
        if zone != '':
            self.click(
                "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    zone))

    def companyassessment_month_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def companyassessment_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_date1_txt", time)

    def companyassessment_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_select1 > input")

    def companyassessment_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click(
            "xpath->//*[@id='report_companyCheckRank_table_div_tabs0_content_panel0_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def companyassessment_btime_input(self, btime):
        """企业考核开始时间"""
        self.clear_input_enter(
            "css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
            btime)

    def companyassessment_etime_input(self, etime):
        """企业考核结束时间"""
        self.clear_input_enter(
            "css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
            etime)

    def companyassessment_select_bt_click(self):
        """企业考核查询按钮"""
        self.click("css->#report_companyCheckRank_table_div_tabs0_content_panel0_form0_button1_btn")

    # --------------------------------------------------------- 服务商考核 ------------------------------------------------------------------

    def platformassessment_click(self):
        """选择服务商考核"""
        self.js(
            "document.querySelector('#checkmanage-index > div > div.check-manage-title > ul > li:nth-child(3) > ul').style.display='block'")
        self.sleep(1)
        self.click("xpath->//li[@data-control='checkManage_providerRank']/a/span[contains(text(),'服务商考核排名')]")

    def platformassessment_platform_input(self, platform):
        """输入平台"""
        self.input("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_text1_show", platform)
        if platform != '':
            self.click(
                "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def platformassessment_type_choose(self, assessmenttype):
        """选择考核类型"""
        self.click("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click(
            "xpath->//*[@id='report_providerCheckRank_table_div_tabs0_content_panel0_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                assessmenttype))

    def platformassessment_zone_input(self, zone):
        """选择地区"""
        self.clear_input("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_text0_show", zone)
        self.click(
            "xpath->//*[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def platformassessment_month_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def platformassessment_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_date1_txt", time)

    def platformassessment_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_select1 > input")

    def platformassessment_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click(
            "xpath->//*[@id='report_providerCheckRank_table_div_tabs0_content_panel0_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def platformassessment_btime_input(self, btime):
        """服务商考核开始时间"""
        self.clear_input_enter(
            "css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
            btime)

    def platformassessment_etime_input(self, etime):
        """服务商考核结束时间"""
        self.clear_input_enter(
            "css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
            etime)

    def platformassessment_select_bt_click(self):
        """服务商考核查询"""
        self.click("css->#report_providerCheckRank_table_div_tabs0_content_panel0_form0_button0_btn")

    # --------------------------------------------------------- 入网明细 ------------------------------------------------------------------

    def details_click(self):
        """点击考核明细"""
        self.js(
            "document.querySelector('#checkmanage-index > div > div.check-manage-title > ul > li:nth-child(4) > ul').style.display='block'")
        self.sleep(1)
        self.click("xpath->//*[@data-control='checkManage_detail']/ul/li/a/span[contains(text(),'考核明细')]")

    def detailsinstall_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailsinstall_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsinstall_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_text2_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailsinstall_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsinstall_time_input(self, time):
        """输入时间"""
        self.clear_input_enter("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def detailsinstall_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailsinstall_carstate_choose(self, carstate):
        """选择车辆状态"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select1 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                carstate))

    def detailsinstall_installtype_click(self, installtype):
        """选择入网状态"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select2 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_select2']/ul/li[contains(text(),'{0}')]".format(
                installtype))

    def detailsinstall_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel0_form0_button1_btn")

    # --------------------------------------------------------- 上线明细 ------------------------------------------------------------------

    def detailsonline_click(self):
        """点击在线统计"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav1")

    def detailsonline_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailsonline_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_text1_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailsonline_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_text2_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsonline_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsonline_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_datePeriod0_date0_txt", btime)

    def detailsonline_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_datePeriod0_date1_txt", etime)

    def detailsonline_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailsonline_onlinetype_click(self, installtype):
        """选择入网状态"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_select1 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                installtype))

    def detailsonline_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel1_form0_button1_btn")

    # --------------------------------------------------------- 平台连通率 ------------------------------------------------------------------

    def detailspatform_click(self):
        """点击平台连通率统计"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav2")

    def detailspatform_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_text0_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailspatform_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailspatform_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_datePeriod0_date0_txt", btime)

    def detailspatform_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_datePeriod0_date1_txt", etime)

    def detailspatform_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailspatform_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel2_form0_button1_btn")

    # --------------------------------------------------------- 轨迹完整率 ------------------------------------------------------------------

    def detailstrail_click(self):
        """点击轨迹完整率"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav3")

    def detailstrail_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailstrail_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_text1_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailstrail_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_text2_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailstrail_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailstrail_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_datePeriod0_date0_txt", btime)

    def detailstrail_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_datePeriod0_date1_txt", etime)

    def detailstrail_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailstrail_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel3_form0_button1_btn")

    # --------------------------------------------------------- 数据合格率 ------------------------------------------------------------------
    def detailsdata_click(self):
        """点击数据合格率"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav4")

    def detailsdata_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailsdata_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_text1_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailsdata_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_text2_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsdata_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsdata_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_datePeriod0_date0_txt", btime)

    def detailsdata_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_datePeriod0_date1_txt", etime)

    def detailsdata_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailsdata_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel4_form0_button1_btn")

    # --------------------------------------------------------- 平均超速明细 ----------------------------------------------------------------

    def detailsspeeding_click(self):
        """点击数据合格率"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav5")

    def detailsspeeding_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailsspeeding_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_text2_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailsspeeding_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsspeeding_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsspeeding_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_datePeriod0_date0_txt", btime)

    def detailsspeeding_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_datePeriod0_date1_txt", etime)

    def detailsspeeding_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailsspeeding_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel5_form0_button1_btn")

    # --------------------------------------------------------- 平均疲架明细 ----------------------------------------------------------------

    def detailstired_click(self):
        """点击数据合格率"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav6")

    def detailstired_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailstired_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_text2_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailstired_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailstired_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailstired_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_datePeriod0_date0_txt", btime)

    def detailstired_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_datePeriod0_date1_txt", etime)

    def detailstired_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailstired_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel6_form0_button1_btn")

    # --------------------------------------------------------- 车辆飘移明细 ----------------------------------------------------------------

    def detailsdrift_click(self):
        """点击数据合格率"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav7")

    def detailsdrift_carnum_input(self, carnum):
        """输入车牌号"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_text0_show", carnum)
        if carnum != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    carnum))

    def detailsdrift_platform_input(self, platform):
        """输入接入平台"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_text2_show", platform)
        if platform != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    platform))

    def detailsdrift_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsdrift_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_text3_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsdrift_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_datePeriod0_date0_txt", btime)

    def detailsdrift_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_datePeriod0_date1_txt", etime)

    def detailsdrift_cartype_choose(self, cartype):
        """选择车辆类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def detailsdrift_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel7_form0_button1_btn")

    # --------------------------------------------------------- 查岗响应明细 ----------------------------------------------------------------

    def detailsresponse_click(self):
        """点击查岗响应"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_ul_nav8")

    def detailsresponse_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def detailsresponse_company_input(self, company):
        """输入企业"""
        self.input("css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_text0_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def detailsresponse_btime_input(self, btime):
        """输入开始时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_datePeriod0_date0_txt", btime)

    def detailsresponse_etime_input(self, etime):
        """输入结束时间"""
        self.clear_input_enter(
            "css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_datePeriod0_date1_txt", etime)

    def detailsresponse_atwork_choose(self, atwork):
        """是否在岗"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_select1 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                atwork))

    def detailsresponse_responsetype_choose(self, responsetype):
        """查询类型"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_select0 > input")
        self.click(
            "xpath->//div[@id='check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                responsetype
            ))

    def detailsresponse_select_click(self):
        """点击查询"""
        self.click("css->#check_report_vehicleinstall_table_div_tabs0_content_panel8_form0_button1_btn")

    # --------------------------------------------------------- 交通隐患清零地区 ----------------------------------------------------------------

    def zero_click(self):
        """点击考核明细"""
        self.js(
            """document.querySelector("li[data-control='checkManage_transport'] > ul").style.display='block'""")
        self.sleep(1)
        self.click("xpath->//li[@data-control='checkManage_transport']/ul/li/a/span[contains(text(),'交通厅隐患清零')]")

    def zerozone_zone_input(self, zone):
        self.clear_input("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_text0_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def zerozone_type_choose(self, assessmenttype):
        """选择考核类型"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_select0 > input")
        self.click(
            "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel0_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                assessmenttype))

    def zerozone_month_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_date0_txt", time)

    def zerozone_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_date1_txt", time)

    def zerozone_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_select1 > input")

    def zerozone_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click(
            "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel0_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def zerozone_btime_input(self, btime):
        """地区考核开始时间"""
        self.clear_input_enter(
            "css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date0_txt",
            btime)

    def zerozone_etime_input(self, etime):
        """地区考核结束时间"""
        self.clear_input_enter(
            "css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_datePeriod0_date1_txt",
            etime)

    def zerozone_carstate_choose(self, carstate):
        """选择车辆状态"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_select2 > input")
        self.click(
            "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel0_form0_select2']/ul/li[contains(text(),'{0}')]".format(
                carstate))

    def zerozone_select_bt_click(self):
        """点击查询"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel0_form0_button1_btn")

    # --------------------------------------------------------- 交通隐患清零企业 ----------------------------------------------------------------

    def zerocompany_click(self):
        self.click("css->#report_transportCheckRank_table_div_tabs0_ul_nav1")

    def zerocompany_company_input(self, company):
        self.input("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_text0_show", company)
        if company != '':
            self.click(
                "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                    company))

    def zerocompany_zone_input(self, zone):
        """输入地区"""
        self.clear_input("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_text1_show", zone)
        self.click(
            "xpath->//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content']/li[contains(text(),'{0}')]".format(
                zone))

    def zerocompany_type_choose(self, assessmenttype):
        """选择考核类型"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_select0 > input")
        # self.click(
        #     "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel1_form0_select0']/ul/li[contains(text(),'{0}')]".format(
        #         assessmenttype))
        self.click(
            "xpath->//*[@id='report_transportCheckRank_table_div_tabs0_content_panel1_form0_select0']/ul/li[contains(text(),'{0}')]".format(
                assessmenttype))

    def zerocompany_month_time_input(self, time):
        """输入时间（月）"""
        self.clear_input_enter("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_date0_txt", time)

    def zerocompany_year_time_input(self, time):
        """输入时间（年）"""
        self.clear_input_enter("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_date1_txt", time)

    def zerocompany_cartype_click(self):
        """点击车辆类型"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_select1 > input")

    def zerocompany_cartype_check(self, cartype):
        """选择车辆类型"""
        self.click(
            "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel1_form0_select1']/ul/li[contains(text(),'{0}')]".format(
                cartype))

    def zerocompany_btime_input(self, btime):
        """地区考核开始时间"""
        self.clear_input_enter(
            "css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_datePeriod0_date0_txt",
            btime)

    def zerocompany_etime_input(self, etime):
        """地区考核结束时间"""
        self.clear_input_enter(
            "css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_datePeriod0_date1_txt",
            etime)

    def zerocompany_carstate_choose(self, carstate):
        """选择车辆状态"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_select2 > input")
        self.click(
            "xpath->//div[@id='report_transportCheckRank_table_div_tabs0_content_panel0_form0_select2']/ul/li/span[contains(text(),'{0}')]".format(
                carstate))

    def zerocompany_select_bt_click(self):
        """点击查询"""
        self.click("css->#report_transportCheckRank_table_div_tabs0_content_panel1_form0_button1_btn")
