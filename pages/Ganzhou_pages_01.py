# coding:utf-8
from common.basepage import pyselenium


class Ganzhou_pages_login(pyselenium):

    # 登录页元素
    def Ganzhou_open(self, url):
        self.open(url)

    def username_input(self, username):
        self.input('css->#app > div > div.login-right > div > div:nth-child(1) > input', username)
        # self.input("css->#txtUser", username)

    def password_input(self, password):
        self.input(
            'css->#app > div > div.login-right > div > div.el-input.el-input--medium.el-input--prefix.el-input--suffix > input',
            password)
        # self.input("css->#txtPwd", password)

    def login_click(self):
        self.click('css->#app > div > div.login-right > div > div.btn-wrapper > button')
        # self.click("css->#button")


class Ganzhou_pages_TJFX(pyselenium):

    # 统计分析

    def TJFX_click(self):
        # self.click('css->[modular-name="统计分析"]')
        self.click('xpath->//div[@class="menu-wrapper"]/div/span[contains(text(),"{0}")]'.format("统计分析"))

    def iframe_in(self):
        self.switch_to_frame("css->#report_Vue")

    def fristmenu_click(self, menuname):
        # 车辆基本统计
        # self.js("document.querySelector('#app > div > section > aside > ul > li:nth-child(1) > ul').style.display='block'")
        self.click('xpath->//*[@class="el-menu-vertical-demo el-menu"]/li/div/span[contains(text(),"{0}")]'.format(
            menuname))

    def secondmenumenu_click(self, menuname):
        self.click('xpath->//*[@class="el-menu el-menu--inline"]/li/ul/li/span[contains(text(),"{0}")]'.format(
            menuname))

    def getthirdmenu_ele(self, num):
        """
        :param num: 第num个表格 0开始
        :return: 第num个表格的元素
        """
        se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
        ele_menu = self.get_element('css-> div > div.search-wrapper > form', ele=se_menu[num - 1], types="level")
        return ele_menu

    def query_bts(self, ele_menu, bt):
        self.click(
            'xpath->.//button[@class="el-button el-button--primary el-button--small"]/span[contains(text(),"{}")]'.format(
                bt), ele=ele_menu, types="level")

    def header_click(self, header):
        self.click(
            # 'xpath->//*[@id="app"]/div/section/main/div/div/div[1]/div/div/div/div[contains(text(),"{0}")]'.format(
            #     header))
            'xpath->//*[@class="el-tabs__nav is-top"]/div[contains(text(),"{0}")]'.format(
                header))

    def zone_input(self, ele_menu, zone):
        self.input('css->input[placeholder="地区为必填项"]', zone, ele=ele_menu, types="level")
        self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li[contains(text(),"{0}")]'.format(zone))

    def daysslot_input(self, ele_menu, btime, etime):
        self.click("css->i.el-input__icon.el-range__close-icon", ele=ele_menu, types="level")
        self.input('css->input[placeholder="开始日期"]', btime, ele=ele_menu, types="level")
        self.input('css->input[placeholder="结束日期"]', etime, ele=ele_menu, types="level")

    def day_input(self, ele_menu, time):
        day = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("选择日期"), ele=ele_menu,
                               types="level")

        # self.click("css->i.el-input__suffix", ele=ele_menu, types="level")
        self.clear_input_enter('xpath->.//following-sibling::*//div/input', time, ele=day, types="level")

    def month_input(self, ele_menu, time):
        month = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("选择月份"), ele=ele_menu,
                                 types="level")
        self.clear_input_enter('xpath->.//following-sibling::*//div/input', time, ele=month, types="level")

    def platform_input(self, ele_menu, platform):
        plat = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("接入平台"), ele=ele_menu,
                                types="level")
        if platform != "":
            self.input('xpath->.//following-sibling::*//div/div/input', platform, ele=plat, types="level")
            self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li[contains(text(),"{0}")]'.format(platform))

    def company_input(self, ele_menu, company):
        comp = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("运输企业"), ele=ele_menu,
                                types="level")
        if company != "":
            self.input('xpath->.//following-sibling::*//div/div/input', company, ele=comp, types="level")
            self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li[contains(text(),"{0}")]'.format(company))

    def cartype_click(self, ele_menu, cartype):
        types = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("车辆类型"), ele=ele_menu,
                                 types="level")
        if cartype != "":
            self.sleep(2)
            self.click('xpath->.//following-sibling::*//div/div/input', ele=types, types="level")
            self.sleep(2)
            self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(cartype))

    def GPS_click(self, ele_menu, GPS):
        G = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("GPS安装情况"), ele=ele_menu,
                             types="level")
        if GPS != "":
            self.click('xpath->.//following-sibling::*//div/div/input', ele=G, types="level")

            self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(GPS))

    def carnum_input(self, ele_menu, carnum):
        car = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("车牌号"), ele=ele_menu,
                               types="level")
        if carnum != "":
            self.input('xpath->.//following-sibling::*//div/div/input', carnum, ele=car, types="level")
            self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li[contains(text(),"{0}")]'.format(carnum))

    def plattype_click(self, ele_menu, palttype):
        types = self.get_element('xpath->.//div/label[contains(text(),"{0}")]'.format("平台类型"), ele=ele_menu,
                                 types="level")
        if palttype != "":
            self.sleep(2)
            self.click('xpath->.//following-sibling::*//div/div/input', ele=types, types="level")
            self.sleep(2)
            self.click(
                'xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(palttype))


class Ganzhou_pages_YHBH(pyselenium):

    # YHBH_tongbao_
    # 隐患闭环

    def YHBH_click(self):
        self.click('css->[modular-name="隐患闭环"]')

    def YHBH_menu_click(self, menu):
        self.click('xpath->//*[@id="app"]/div/section/aside/ul/li/span[contains(text(),"{0}")]'.format(menu))

    def YHBH_tongbao_select(self):
        self.click(
            'css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(2) > div > button')

    def YHBH_tongbao_select_title_input(self, title):
        self.input(
            'css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(1) > div > div > input',
            title)

    def YHBH_tongbao_add_click(self):
        self.click(
            'css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(3) > div > button')

    def YHBH_tongbao_add_title_input(self, title):
        self.input(
            'css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(1) > div > div > input',
            title)

    def YHBH_tongbao_add_time_input(self, btime, etime):
        self.input_and_enter(
            'css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(2) > div > div > input:nth-child(2)',
            btime)
        self.input_and_enter(
            'css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(2) > div > div > input:nth-child(4)',
            etime)

    def YHBH_tongbao_add_back_click(self):
        self.click(
            'css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(1) > button.el-button.el-button--default')

    def YHBH_tongbao_add_YES_click(self):
        self.click(
            'css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(1) > button.el-button.el-button--primary')
