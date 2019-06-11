# coding:utf-8
from common.basepage import pyselenium

class Ganzhou_pages_login(pyselenium):

    # 登录页元素
    def Ganzhou_open(self,url):
        self.open(url)

    def username_input(self,username):
        self.input("css->#txtUser",username)

    def password_input(self,password):
        self.input("css->#txtPwd",password)

    def login_click(self):
        self.click("css->#button")

class Ganzhou_pages_TJFX(pyselenium):

    # 统计分析

    def TJFX_click(self):
        self.click('css->[modular-name="统计分析"]')


class Ganzhou_pages_YHBH(pyselenium):

    # YHBH_tongbao_
    # 隐患闭环

    def YHBH_click(self):
        self.click('css->[modular-name="隐患闭环"]')

    def YHBH_menu_click(self,menu):
        self.click('xpath->//*[@id="app"]/div/section/aside/ul/li/span[contains(text(),"{0}")]'.format(menu))

    def YHBH_tongbao_select(self):
        self.click('css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(2) > div > button')

    def YHBH_tongbao_select_title_input(self,title):
        self.input('css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(1) > div > div > input',title)

    def YHBH_tongbao_add_click(self):
        self.click('css->#app > div > section > main > div > div.search-wrapper > form > div:nth-child(3) > div > button')

    def YHBH_tongbao_add_title_input(self,title):
        self.input('css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(1) > div > div > input',title)

    def YHBH_tongbao_add_time_input(self,btime,etime):
        self.input_and_enter('css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(2) > div > div > input:nth-child(2)',btime)
        self.input_and_enter('css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(2) > form > div:nth-child(2) > div > div > input:nth-child(4)',etime)

    def YHBH_tongbao_add_back_click(self):
        self.click('css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(1) > button.el-button.el-button--default')

    def YHBH_tongbao_add_YES_click(self):
        self.click('css->#app > div > section > main > div > div:nth-child(2) > div > div:nth-child(1) > button.el-button.el-button--primary')

