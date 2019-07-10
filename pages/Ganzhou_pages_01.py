# coding:utf-8
from common.basepage import pyselenium


class Ganzhou_pages_login(pyselenium):

    # 登录页元素
    def Ganzhou_open(self, url):
        self.open(url)

    def username_input(self, username):
        self.input("css->#txtUser", username)

    def password_input(self, password):
        self.input("css->#txtPwd", password)

    def login_click(self):
        self.click("css->#button")


class Ganzhou_pages_TJFX(pyselenium):

    # 统计分析

    def TJFX_click(self):
        self.click('css->[modular-name="统计分析"]')

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

    def query_bts(self, num, bt):
        se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
        querys = self.get_element('css-> div > div.search-wrapper > form', ele=se_menu[num], types="level")
        self.click(
            'xpath->//button[@class="el-button el-button--primary el-button--small"]/span[contains(text(),"{0}")]'.format(
                bt), ele=querys, types="level")

    def header_click(self, header):
        self.click(
            'xpath->//*[@id="app"]/div/section/main/div/div/div[1]/div/div/div/div[contains(text(),"{0}")]'.format(
                header))

    def zone_input(self, num, zone):
        se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
        querys = self.get_element('css-> div > div.search-wrapper > form', ele=se_menu[num], types="level")
        self.input('css->input[placeholder="地区为必填项"]', zone, ele=querys, types="level")
        self.click('xpath->/html/body/div[2]/div[1]/div[1]/ul/li[contains(text(),"{0}")]'.format(zone))

    # def plantform_input(self):
    #     se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
    #     querys = self.levels_get_element(se_menu[num], 'css-> div > div.search-wrapper > form')
    #     self.levels_input(querys, 'css->input[placeholder="地区为必填项"]', zone)

    def timeslot_input(self, num, btime, etime):
        se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
        querys = self.get_element('css-> div > div.search-wrapper > form', ele=se_menu[num], types="level")
        self.click("css->i.el-input__icon.el-range__close-icon", ele=querys, types="level")
        self.input('css->input[placeholder="开始日期"]', btime, ele=querys, types="level")
        self.input('css->input[placeholder="结束日期"]', etime, ele=querys, types="level")





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
