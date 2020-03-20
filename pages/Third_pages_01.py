# coding:utf-8
from common.basepage import pyselenium


class Third_homepages_login(pyselenium):

    # 登录页元素
    def Third_open(self, url):
        self.open(url)

    def homepagemenu_click(self, homepagemenu):
        # self.click('css->[modular-name="统计分析"]')
        # self.click('xpath->//div[@class="menu-wrapper"]/div/span[contains(text(),"{0}")]'.format("统计分析"))
        self.click('xpath->//div[@class="menu-wrapper"]/div/span[contains(text(),"{0}")]'.format(homepagemenu))


class Third_pages_TJFX(Third_homepages_login):
    """
    统计分析
    """

    def iframe_in(self):
        self.switch_to_frame("css->#report_Vue")

    def fristmenu_click(self, menuname, second=True):
        """
        点击一级菜单
        :param menuname:
        :param second: True 或者 False 布尔值判断是否有二级菜单
        :return:
        """
        try:
            if second is True:
                self.click(
                    'xpath->//*[@class="el-menu-vertical-demo el-menu"]//div/span[contains(text(),"{0}")]'.format(
                        menuname))
            elif second is False:
                self.click(
                    'xpath->//*[@class="el-menu-vertical-demo el-menu"]//div/li/span[contains(text(),"{0}")]'.format(
                        menuname))
        except:
            raise
        # self.js("document.querySelector('#app > div > section > aside > ul > li:nth-child(1) > ul').style.display='block'")

    def secondmenu_click(self, menuname):
        """
        点击二级菜单
        :param menuname:
        :return:
        """
        self.click('xpath->//*[@class="el-menu el-menu--inline"]/li/ul/li/span[contains(text(),"{0}")]'.format(
            menuname))

    def getheader_ele(self, num=1, third=True):
        """
        获取查询条件元素组
        :param num: 第num个表格 从1开始
        :param third: 判断是否有有第三级菜单选项 如:地区汇总,企业汇总等
        :return: 第num个表格的元素
        """
        try:
            if third is True:
                se_menu = self.get_elements('xpath->//*[@class="el-tab-pane"]')
                ele_menu = self.get_element('css-> div > div.search-wrapper > form', ele=se_menu[num - 1],
                                            types="level")
                return ele_menu
            elif third is False:
                ele_menu = self.get_element('css-> div > div.search-wrapper > form')
                return ele_menu
        except:
            raise

    def query_bts(self, ele_menu, bt):
        """
        按钮定位
        :param ele_menu:
        :param bt:
        :return:
        """
        self.click(
            'xpath->.//button[@class="el-button el-button--primary el-button--small"]/span[contains(text(),"{}")]'.format(
                bt), ele=ele_menu, types="level")

    def thirdmenu_click(self, header):
        """
        点击三级菜单
        :param header:
        :return:
        """
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
