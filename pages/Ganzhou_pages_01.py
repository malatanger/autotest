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
