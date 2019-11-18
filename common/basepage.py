# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from common.log import Log
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import report_path
import os

success = "SUCCESS   "
fail = "FAIL      "
warning = "WARNING   "
error = "ERROR     "
logger = Log()


class Browser_engine(object):
    """浏览器引擎"""

    @staticmethod
    def my_print(msg, level=1):

        if level == 1:
            logger.info(msg)
        elif level == 2:
            logger.debug(msg)
        elif level == 3:
            logger.warning(msg)
        elif level == 4:
            logger.error(msg)


    @staticmethod
    def get_browser(browsertype="chrome"):
        t1 = time.time()
        try:
            if browsertype == "ie":
                driver = webdriver.Ie()
            elif browsertype == "firefox":
                driver = webdriver.Firefox()
            else:
                driver = webdriver.Chrome()

            logger.info(
                "{0} 新建浏览器: {1}, 用时 {2} 秒.".format(success, browsertype, time.time() - t1)
            )
        except Exception:
            raise NameError(
                "未发现 {0} 浏览器,你可以输入 'ie','chrome','firefox'.".format(browsertype)
            )

        return driver


class pyselenium(Browser_engine):

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()  # 调试模式

    def open(self, url):
        """打开网址"""
        t1 = time.time()
        try:
            self.driver.get(url)
            self.my_print(
                "{0} 成功打开链接：{1}，用时 {2} 秒.".format(success, url, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 打开链接失败.".format(fail)
            )
            raise

    def element_wait(self, css, sec=5):
        if "->" not in css:
            raise NameError("请在定位方法以及路径之间输入“->”")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = '{0}秒内，未能找到元素：{1} '.format(sec, css)
        if by == "id":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_all_elements_located((By.ID, value)),
                messages
            )
        elif by == "name":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.NAME, value)),
                messages
            )
        elif by == "class":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)),
                messages
            )
        elif by == "link_text":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.LINK_TEXT, value)),
                messages
            )
        elif by == "xpath":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.XPATH, value)),
                messages
            )
        elif by == "css":
            WebDriverWait(self.driver, sec, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)),
                messages
            )
        else:
            raise NameError(
                "输入获取元素方法'id','name','class','link_text','xpath','css'."
            )

    # global element

    def get_element(self, css, ele=None, types="ordinary"):
        """获取元素"""

        if "->" not in css:
            raise NameError("请在定位方法以及路径之间输入“->”")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        # if css == "id":
        #     WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_id(value))
        if types == "ordinary":
            if by == "id":
                element = self.driver.find_element_by_id(value)
            elif by == "name":
                element = self.driver.find_element_by_name(value)
            elif by == "class":
                element = self.driver.find_element_by_class_name(value)
            elif by == "link_text":
                element = self.driver.find_element_by_link_text(value)
            elif by == "xpath":
                element = self.driver.find_element_by_xpath(value)
            elif by == "css":
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError(
                    "输入获取元素方法'id','name','class','link_text','xpath','css'."
                )
            return element
        else:
            if by == "id":
                element = ele.find_element_by_id(value)
            elif by == "name":
                element = ele.find_element_by_name(value)
            elif by == "class":
                element = ele.find_element_by_class_name(value)
            elif by == "link_text":
                element = ele.find_element_by_link_text(value)
            elif by == "xpath":
                element = ele.find_element_by_xpath(value)
            elif by == "css":
                element = ele.find_element_by_css_selector(value)
            else:
                raise NameError(
                    "输入获取元素方法'id','name','class','link_text','xpath','css'."
                )
            return element

    def get_elements(self, css, ele=None, types="ordinary"):
        """
        Judge element positioning way, and returns the element.
        批量获取元素。
        Usage:
        driver.get_elements('id->kw')
        """
        if "->" not in css:
            raise NameError("请在定位方法以及路径之间输入“->”")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        if types == "ordinary":
            if by == "id":
                elements = self.driver.find_elements_by_id(value)
            elif by == "name":
                elements = self.driver.find_elements_by_name(value)
            elif by == "class":
                elements = self.driver.find_elements_by_class_name(value)
            elif by == "link_text":
                elements = self.driver.find_elements_by_link_text(value)
            elif by == "xpath":
                elements = self.driver.find_elements_by_xpath(value)
            elif by == "css":
                elements = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError(
                    "输入获取元素方法'id','name','class','link_text','xpath','css'."
                )
            return elements

        else:

            if by == "id":
                elements = ele.find_elements_by_id(value)
            elif by == "name":
                elements = ele.find_elements_by_name(value)
            elif by == "class":
                elements = ele.find_elements_by_class_name(value)
            elif by == "link_text":
                elements = ele.find_elements_by_link_text(value)
            elif by == "xpath":
                elements = ele.find_elements_by_xpath(value)
            elif by == "css":
                elements = ele.find_elements_by_css_selector(value)
            else:
                raise NameError(
                    "输入获取元素方法'id','name','class','link_text','xpath','css'."
                )
            return elements

    def input_and_enter(self, css, text, sec=1, ele=None, types="ordinary"):
        """输入并敲击回车"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                el = self.get_element(css)
            else:
                el = self.get_element(ele, css, types="level")
            el.send_keys(text)
            time.sleep(sec)
            el.send_keys(Keys.ENTER)
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入成功， 用时 {3} 秒.".format(success, css, text, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入失败， 用时 {3} 秒.".format(fail, css, text, time.time() - t1)
            )
            raise

    def clear_input_enter(self, css, text, ele=None, sec=1, types="ordinary"):

        """清除默认内容，并输入新内容"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                el = self.get_element(css)
                el.clear()
            else:
                el = self.get_element(css, ele, types="level")
                el.clear()
            el.send_keys(text)
            self.sleep(sec)
            el.send_keys(Keys.ENTER)
            self.my_print("{0} 清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(success, css, text, time.time() - t1))
        except Exception:
            self.my_print("{0} 无法清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(fail, css, text, time.time() - t1))
            raise

    # def Enter(self,css):
    #
    #     """清除默认内容，并输入新内容"""
    #     t1 = time.time()
    #     try:
    #         self.element_wait(css)
    #         el = self.get_element(css)
    #         el.send_keys(Keys.ENTER)
    #         self.my_print("{0} 清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(success, css, time.time() - t1))
    #     except Exception:
    #         self.my_print("{0} 无法清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(fail, css, time.time() - t1))
    #         raise

    def input(self, css, text, ele=None, types="ordinary"):
        """输入"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                el = self.get_element(css)
                el.send_keys(text)
                self.my_print(
                    "{0} 元素：{1}，内容：‘{2}’输入成功， 用时 {3} 秒.".format(success, css, text, time.time() - t1)
                )
            else:
                el = self.get_element(css, ele, types="level")
                el.send_keys(text)
                self.my_print(
                    "{0} 元素：{1}，内容：‘{2}’输入成功， 用时 {3} 秒.".format(success, css, text, time.time() - t1)
                )
        except Exception:
            self.my_print(
                "{0} 元素：{1}，内容：‘{2}’输入失败， 用时 {3} 秒.".format(fail, css, text, time.time() - t1)
            )
            raise

    def quit(self):
        """关闭浏览器"""
        t1 = time.time()
        self.driver.quit()
        self.my_print(
            "{0} 退出浏览器并清除临时文件， 用时 {1} 秒.".format(success, time.time() - t1)
        )

    def F5(self):
        """刷新"""
        t1 = time.time()
        self.driver.refresh()
        self.my_print(
            "{0} 刷新页面，用时{1}".format(success, time.time() - t1)
        )

    def take_screenshot(self):
        """截图"""
        t1 = time.time()
        date = time.strftime('%Y-%m-%d')
        file_path = report_path + date
        image_path = file_path + "/image/"
        isExists = os.path.exists(file_path)
        isExists2 = os.path.exists(image_path)
        if not isExists:
            os.mkdir(file_path)
        if not isExists2:
            os.mkdir(image_path)
        date = time.strftime('%Y%m%d%H%M%S', time.localtime())
        screenname = image_path + date + ".png"
        try:
            picture_url = self.driver.get_screenshot_as_file(screenname)
            if picture_url is True:
                print('screenshot:  {0}.png'.format(date))
                self.my_print(
                    "{0} 截图保存成功，地址为{1}， 用时 {2} 秒.".format(success, image_path, time.time() - t1)
                )
            else:
                self.my_print("{0} 截图保存失败.".format(warning))
        except Exception:
            raise AttributeError(
                "截图失败"
            )

    def click(self, css, ele=None, types="ordinary"):
        """点击"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                self.get_element(css).click()
            else:
                el = self.get_element(css, ele, types="level")
                el.click()
            self.my_print(
                "{0} 点击元素：{1}， 用时 {2} 秒.".format(success, css, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 未能点击元素{1}.".format(fail, css)
            )
            raise

    def clicks(self, css, num, ele=None, types="ordinary"):
        """
        点击元素组中的元素
        :param css:
        :param num:
        :param ele:
        :param types:
        :return:
        """
        global el
        t1 = time.time()
        try:
            if types == "ordinary":
                el = self.get_elements(css)
                el[num].click()
            else:
                el = self.get_elements(css, ele, types="level")
                el[num].click()
            self.my_print(
                "{0} 点击第{1}元素：{2}， 用时 {3} 秒.".format(success, num + 1, css, time.time() - t1)
            )
        except Exception:
            self.my_print(
                "{0} 未能点击元素{1}.".format(fail, css)
            )
            raise

    def movetoelement(self, css, ele=None, types="ordinary"):
        """悬停元素"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                el = self.get_element(css)
                ActionChains(self.driver).move_to_element(el).perform()
                self.my_print(
                    "{0} 移动到元素: <{1}>, 用时 {2} 秒.".format(success, css, time.time() - t1)
                )
            else:
                el = self.get_element(css, ele, types="level")
                ActionChains(self.driver).move_to_element(el).perform()
                self.my_print(
                    "{0} 移动到元素: <{1}>, 用时 {2} 秒.".format(success, css, time.time() - t1)
                )
        except Exception:
            self.my_print(
                "{0} 无法移动到元素: <{1}>, 用时 {2} 秒.".format(fail, css, time.time() - t1)
            )
            raise

    def wait(self, secs=5):
        """隐性等待"""
        self.driver.implicitly_wait(secs)
        self.my_print(
            "{0} 等待 {1} 秒钟".format(success, secs)
        )

    def sleep(self, secs=5):
        """强制等待"""
        time.sleep(secs)
        self.my_print(
            "{0} 等待 {1} 秒钟".format(success, secs)
        )

    def max_window(self):
        """最大化浏览器"""
        t1 = time.time()
        self.driver.maximize_window()
        self.my_print(
            "{0} 浏览器窗口最大化, 用时 {1} 秒.".format(success, time.time() - t1)
        )

    def get_text(self, css):
        """获取元素的文本值"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)

            text = self.get_element(css).text
            self.my_print(
                "{0} 获取元素文本 元素: <{1}> 文本内容：<{2}>, 用时 {3} 秒.".format(success, css, text, time.time() - t1)
            )
            return text
        except Exception:
            self.my_print(
                "{0} 无法获取元素文本 元素: <{1}>, 用时 {2} 秒.".format(fail, css, time.time() - t1)
            )
            raise

    def assert_text(self, text, css, sec=15, asserttype="in"):
        """文本断言"""
        t1 = time.time()
        try:
            self.element_wait(css, sec)
            page_text = self.get_text(css)
            if asserttype == 'in':
                assert text in page_text
                self.my_print(
                    "{0} 断言类型：{1}  通过  元素: <{2}> , 用时 {3} 秒.".format(success, asserttype, css,
                                                                     time.time() - t1)
                )
            elif asserttype == "not in":
                if page_text != '':
                    assert text not in page_text
                    self.my_print(
                        "{0} 断言类型：{1}  通过  元素: <{2}> , 用时 {3} 秒.".format(success, asserttype, css,
                                                                         time.time() - t1)
                    )
                else:
                    self.my_print("{0} 断言元素文本内容为空， 用时 {1} 秒.".format(error, time.time() - t1))
            else:
                self.my_print(
                    "断言类型错误，请输入'in'或者'not in'."
                )
        except AssertionError:
            self.my_print(
                "{0} 断言类型：{1}  未通过  元素: <{2}> 断言文本：<{3}>, 用时 {4} 秒.".format(fail, asserttype, css, text,
                                                                            time.time() - t1)
            )
            self.take_screenshot()
            raise

    def js(self, script):
        """导入js"""
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.my_print("{0} 执行 javascript 脚本: {1}, 用时 {2} 秒.".format(success, script, time.time() - t1))
        except Exception:
            self.my_print("{0} 无法执行 javascript 脚本: {1}, 用时 {2} 秒.".format(fail, script, time.time() - t1))
            raise

    def clear(self, css):
        """清除默认内容"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.clear()
            self.my_print("{0} 清除元素: <{1}> , 用时 {2} 秒.".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} 无法清除元素: <{1}> , 用时 {2} 秒.".format(fail, css, time.time() - t1))
            raise

    def clear_input(self, css, text, ele=None, types="ordinary"):
        """清除默认内容，并输入新内容"""
        global el
        t1 = time.time()
        try:
            self.element_wait(css)
            if types == "ordinary":
                el = self.get_element(css)
                el.clear()
                el.send_keys(text)
            else:
                el = self.get_element(css, ele, types="level")
                el.clear()
                el.send_keys(text)
            self.my_print("{0} 清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(success, css, text, time.time() - t1))
        except Exception:
            self.my_print("{0} 无法清除元素: <{1}> 输入: {2}, 用时 {3} 秒.".format(fail, css, text, time.time() - t1))
            raise

    def switch_to_frame(self, css):
        """frame切换"""
        t1 = time.time()
        try:
            self.element_wait(css)
            iframe_el = self.get_element(css)
            self.driver.switch_to.frame(iframe_el)
            self.my_print("{0} 切换至iframe: <{1}>, 用时 {2} 秒".format(success, css, time.time() - t1))
        except Exception:
            self.my_print("{0} 未能切换至iframe: <{1}>, 用时 {2} 秒".format(fail, css, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        """
        frame退出
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.my_print("{0} 退出iframe, 用时 {1} 秒".format(success, time.time() - t1))

    def add_cookies(self, cookie):
        """

        :param cookie:  cookie dict
        :return:
        """
        t1 = time.time()
        self.driver.add_cookie(cookie)
        self.my_print("{0} 添加cookies, 用时 {1} 秒".format(success, time.time() - t1))

    def deleteall_cookies(self):
        t1 = time.time()
        self.driver.delete_all_cookies()
        self.my_print("{0} 清除cookies, 用时 {1} 秒".format(success, time.time() - t1))


class Retry(object):
    """
    重新执行
    """

    @staticmethod
    def retry(times=3, wait_time=5):
        def _warpper(func):
            def warpper(*args, **kwargs):
                raise_info = None
                rnum = 0
                for i in range(times):
                    rnum += 1
                    try:
                        ret = func(*args, **kwargs)
                        if rnum > 1:
                            logger.info('{0} 执行次数: {1}次, 成功'.format(success, rnum))
                        return ret
                    except Exception as ex:
                        time.sleep(wait_time)
                        raise_info = ex
                logger.info('{0} 执行次数: {1}次, 全部失败'.format(fail, rnum))
                raise raise_info

            return warpper

        return _warpper

# if __name__ == "__main__":
