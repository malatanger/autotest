# coding:utf-8
from common.basepage import pyselenium


class Chifeng_pages_login(pyselenium):

    def open_Chifeng(self, url):
        self.open(url)

    def username_input(self, username):
        self.input("css->#app > div > div > div > div:nth-child(4) > form > div:nth-child(1) > input", username)

    def password_input(self, password):
        self.input("css->#app > div > div > div > div:nth-child(4) > form > div:nth-child(3) > input", password)

    def click_login(self):
        self.click("css->#app > div > div > div > div:nth-child(4) > form > div.el-form-item > div > button")


class Chifeng_menu(pyselenium):

    def kccy_menu(self):
        """客车抽验"""
        self.click('css->#app > div > section > aside > ul > li.el-submenu.is-active.is-opened > div')

    def ky_menu(self):
        self.click(
            'css->#app > div > section > aside > ul > li.el-submenu.is-active.is-opened > ul > li > ul > li:nth-child(1)')

    def wh_menu(self):
        self.click(
            'css->#app > div > section > aside > ul > li.el-submenu.is-active.is-opened > ul > li > ul > li:nth-child(2)')

    def cz_menu(self):
        self.click(
            'css->#app > div > section > aside > ul > li.el-submenu.is-active.is-opened > ul > li > ul > li:nth-child(3)')

    def qycy_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(2)')

    def kyqy_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(2) > ul > li > ul > li:nth-child(1)')

    def whqy_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(2) > ul > li > ul > li:nth-child(2)')

    def xscy_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(3) > div')

    def jyxs_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(3) > ul > li > ul > li:nth-child(1)')

    def jsyxs_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(3) > ul > li > ul > li:nth-child(2)')

    def xxfb_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(4) > div')

    def tq_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(4) > ul > li > ul > li:nth-child(1)')

    def tz_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(4) > ul > li > ul > li:nth-child(2)')

    def qt_menu(self):
        self.click('css->#app > div > section > aside > ul > li:nth-child(4) > ul > li > ul > li:nth-child(3)')


class Chifeng_select(pyselenium):

    def select_click(self):
        self.click(
            "css->#app > div > section > section > main > div > div.bus_body > div.bus_event > button:nth-child(1)")

    def carnum_input(self, carnum):
        self.input('css->[placeholder="车牌号"]', carnum)

    def number_input(self, number):
        self.input('css->[placeholder="编号"]', number)

    def group_input(self, group):
        self.input('css->[placeholder="组别"]', group)

    def bdate_input(self, bdate):
        self.input_and_enter('css->[placeholder="开始日期"]', bdate)

    def edate_input(self, edate):
        self.input_and_enter('css->[placeholder="结束日期"]', edate)

    def zone_click(self, zone):
        # self.js("document.querySelector('body > div.el-select-dropdown.el-popper').style.display='block'")
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div.bus_header > div > div.el-col.el-col-4 > div > div > div > input')
        self.sleep(2)
        self.click(
            'xpath->//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"{0}")]'.format(
                zone))
        self.sleep(2)

    def feedback_click(self, feedback):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div.bus_header > div > div:nth-child(6) > div > div > div.el-input.el-input--suffix > input')
        self.sleep(2)
        self.click('xpath->//li[@class="el-select-dropdown__item"]/span[contains(text(),"{0}")]'.format(
            feedback))
        self.sleep(2)

    def company_input(self, company):
        self.input('css->[placeholder="请输入企业名称"]', company)

    def cardnum_input(self, number):
        self.input('css->[placeholder="请输入证件号码"]', number)


class Chifeng_update(pyselenium):

    def update_click(self):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div.bus_event > button:nth-child(4)')

    def up_carnum_input(self, carnum):
        self.input('css->[placeholder="请输入车牌号"]', carnum)

    def up_color_click(self, color):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(2) > div > div > div > input')
        self.sleep(2)
        self.click(
            'xpath->//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span[contains(text(),"{0}")]'.format(
                color))
        self.sleep(2)

    def up_update_input(self, bdate):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > input',
            bdate)

    def up_backdate_input(self, edate):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(10) > div > div > input',
            edate)

    def up_numeber_input(self, number):
        self.input('css->[placeholder="请输入编号"]', number)

    def up_group_input(self, group):
        self.input('css->[placeholder="请输入组别"]', group)

    def up_company_input(self, company):
        self.input('css->[placeholder="请输入企业名称"]', company)

    def up_zone_click(self, zone):
        """适用于车辆抽验-客运危货/企业抽验"""
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(7) > div > div > div > input')
        self.sleep(2)
        self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(zone))
        self.sleep(2)

    def up_problem_click(self, problem):
        self.click(
            'css->.el-dialog__body > form > div:nth-child(8) > div > div > div > input ')
        self.sleep(2)
        self.click('xpath->/html/body/div/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(problem))
        self.sleep(2)

    def up_feedback_click(self, feedback):
        self.get_elements()

    def up_yes_click(self):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__footer > div > button.el-button.el-button--primary')

    def up_cz_zone_click(self, zone):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div > input')
        self.sleep(2)
        self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(zone))
        self.sleep(2)

    def up_problem_input(self, problem):
        self.input('css->[placeholder="请输入问题"]', problem)

    def up_remarks_input(self, remarks):
        self.input('css->[placeholder="请输入备注"]', remarks)

    def up_checktime_input(self, btime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(4) > div > div > input',
            btime)

    def up_cc_company_input(self, company):
        self.input(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input',
            company)

    def up_chagangtime_input(self, btime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > input',
            btime)

    def up_btime_input(self, btime):
        # self.click('css->[placeholder="开始日期"]')
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > input:nth-child(2)',
            btime, sec=2)

    def up_etime_input(self, etime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > input:nth-child(4)',
            etime, sec=2)

    def up_qy_feedback_click(self, feedback):
        self.click(
            'css->div.el-dialog__body > form > div:nth-child(10) > div > div > div.el-input.el-input--suffix > input')
        self.sleep(2)
        self.click('xpath->/html/body/div/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(feedback))
        self.sleep(2)

    def up_jyxs_btime(self, btime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input:nth-child(2)',
            btime)

    def up_jyxs_etime(self, etime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input:nth-child(4)',
            etime)

    def up_name_input(self, username):
        self.input('css->[placeholder="请输入人员姓名"]', username)

    def up_cardnum_input(self, number):
        self.input(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(5) > div > div > input',
            number)

    def up_jyxs_zone_click(self, zone):
        self.click(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(6) > div > div > div.el-input.el-input--suffix > input')
        self.sleep(2)
        self.click('xpath->/html/body/div[last()]/div[1]/div[1]/ul/li/span[contains(text(),"{0}")]'.format(zone))
        self.sleep(2)

    def up_platform_input(self, platform):
        self.input('css->[placeholder="请输入所用平台"]', platform)

    def up_xxfb_number_input(self, number):
        self.input(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(1) > div > div > input',
            number)

    def up_xxfb_btime_input(self, btime):
        self.input_and_enter(
            'css->#app > div > section > section > main > div > div.bus_body > div:nth-child(3) > div > div.el-dialog__body > form > div:nth-child(3) > div > div > input',
            btime)

    def up_content_input(self, problem):
        self.input('css->[placeholder="请输入发布内容"]', problem)

    def up_range_input(self, problem):
        self.input('css->[placeholder="请输入发布范围"]', problem)
