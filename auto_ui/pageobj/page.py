from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.dr = driver

    def by_id(self, id_):
        return self.dr.find_element_by_id(id_)

    def by_name(self, name_):
        return self.dr.find_element_by_name(name_)

    def by_class_name(self, cname_):
        return self.dr.find_element_by_class_name(cname_)

    def by_tag_name(self, tname_):
        return self.dr.find_element_by_tag_name(tname_)

    def by_link_text(self, text_):
        return self.dr.find_element_by_link_text(text_)

    def by_partial_linktext(self, text_):
        return self.dr.find_element_by_partial_link_text(text_)

    def by_xpath(self, xpath_):
        return self.dr.find_element_by_xpath(xpath_)

    def by_css_selector(self, any_):
        return self.dr.find_element_by_css_selector(any_)

    def visibility_of_element_located(self, args):
        """
        :param args:  tuple 比如 (By.XPATH, '//*[@id="app"]/div/input')
        :return: element
        """
        element = WebDriverWait(self.dr, 10, 0.5).until(
            # 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
            # 和presence_of_element_located有点像，但后者只强调元素存在于DOM树中，可见不可见无所谓，
            # 而visibility要求必须高和宽必须都大于0，因此后者在性能上会稍微快一点点
            EC.visibility_of_element_located(args)
        )
        return element

    def element_to_be_clickable(self, args):
        """
            同 explicit_wait_search
        """
        element = WebDriverWait(self.dr, 5, 0.5).until(
            # 判断元素是否可见并且能被单击，条件满足返回页面元素对象，否则返回Flase
            EC.element_to_be_clickable(args)
        )
        return element

    def presence_of_element_located(self, args):
        """
            同 explicit_wait_search
        """
        element = WebDriverWait(self.dr, 5, 0.5).until(
            # 判断一个元素存在于页面DOM树中，存在则返回元素本身，不存在则报错
            EC.presence_of_element_located(args)
        )
        return element

    def visibility_of_all_elements_located(self, args):
        """
            同 explicit_wait_search
        """
        element = WebDriverWait(self.dr, 5, 0.5).until(
            EC.visibility_of_all_elements_located(args)
        )
        return element


class LoginPage(BasePage):

    def by_xpath(self, xpath_):
        element = WebDriverWait(self.dr, 5, 0.5).until(
            lambda x: x.find_element_by_xpath(xpath_)
        )
        return element


    @property
    def search_nameinput(self):
        return self.by_xpath('//*[@id="app"]/div/form/div/div[2]/div/div/input')

    @property
    def search_pwdinput(self):
        return self.by_xpath('//*[@id="app"]/div/form/div/div[3]/div/div/input')

    @property
    def search_button(self):
        return self.by_tag_name('button')


class IndexPage(BasePage):

    @property
    def search_indexa(self):
        return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/a[1]'))


    @property
    def search_evidencea(self):
        return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/a[2]'))

    @property
    def search_basicinfoa(self):
        return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/a[4]'))

    @property
    def search_warninga(self):
        return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/a[3]'))

    @property
    def search_dropdownboxi(self):
        """
        找下拉框元素
        :return: element
        """
        return self.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section/header/div/span/div/i'))

    @property
    def search_full_screendiv(self):
        """
        找下拉框中的全屏按钮
        :return:
        """
        ele = self.presence_of_element_located((By.XPATH, "//div[contains(@id,'el-popover')]"))
        if ele.get_attribute('aria-hidden') == 'false':
            return self.element_to_be_clickable((By.XPATH, '//*[@id="screenfull"]'))

    @property
    def search_logoutdiv(self):
        """
        找下拉框中的退出按钮
        :return:
        """
        ele = self.presence_of_element_located((By.XPATH, "//div[contains(@id,'el-popover')]"))
        if ele.get_attribute('aria-hidden') == 'false':
            return self.element_to_be_clickable((By.XPATH, "//div[contains(@id,'el-popover')]/div/div[3]"))

    @property
    def search_logoutalter(self):
        """
        找退出提示框
        :return:
        """
        return self.visibility_of_element_located((By.XPATH, "//div[contains(@tabindex,'-1')]/div/div[2]/div[1]/div[2]/p"))


class BaseInfoPage(BasePage):

    def search_userinfoli(self):
        return self.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/li[1]'))

    def search_usermagmtli(self):
        li = self.search_userinfoli()
        if li.get_attribute('aria-expanded') == 'true':
            return self.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/li[1]/ul/a/li')
            )

    def search_cropinfoli(self):
        return self.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/li[2]'))

    def search_cropmagmtli(self):
        li = self.search_cropinfoli()
        if li.get_attribute('aria-expanded') == 'true':
            return self.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/li[2]/ul/a[1]/li')
            )

    def search_roommagmtli(self):
        li = self.search_cropinfoli()
        if li.get_attribute('aria-expanded') == 'true':
            return self.visibility_of_element_located(
                (By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/li[2]/ul/a[2]/li')
            )


class ManageUserPage(BasePage):
    pass


class ManageCropPage(BasePage):

    def search_textdiv(self):
        """
        单位管理 text的div
        :return:
        """
        return self.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[1]'))

    def search_addbut(self):
        return self.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/section/main/div/div/form/div[1]/div[2]/div/div[2]/button')
        )

    def search_addcropnameinput(self):
        """
        找到新增单位表单中的名称输入框
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[1]/div/div[1]/input'))

    def search_addcropcodeinput(self):
        """
        找到新增单位表单中的单位编号输入框
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[2]/div/div/input'))

    def search_addcroptype(self):
        """
        找到新增单位表单中的单位类型下拉框
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[3]/div/div/div'))

    def search_croptypes(self):
        """
        找到类型选择栏
        :return: 一组元素列表 span   [市局, 市局部门, 分局, 分局部门, 派出所]
        """
        if self.presence_of_element_located((By.XPATH, '/html/body/div[@class="el-select-dropdown el-popper"]')).is_displayed():
            return self.visibility_of_all_elements_located((By.XPATH, '//div[@class="el-select-dropdown '
                                                                      'el-popper"]/div[1]/div[1]/ul/ul//span'))

    def search_cropaddressinput(self):
        """
        找到地址输入栏
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[5]/div/div/input'))

    def search_disableinput(self):
        """
        找到禁用栏
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[6]/div/label[2]/span['
                                                                 '1]/input'))

    def search_promptdiv(self):
        """
        找到提示框， 一般只有新增/修改/删除才会出现提示框
        :return:
        """
        return self.presence_of_element_located((By.XPATH, '//h2[@class="el-notification__title"]'))

    def search_confirmbut(self):
        """
        确认按钮
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-card dialog-card is-always-shadow"]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                                 '3]/div/div[2]/div/form/div[7]/button[2]'))

    def search_queryinp(self):
        """
        关键字输入框
        :return:
        """
        return self.presence_of_element_located((By.CLASS_NAME, 'el-input__inner'))

    def serach_querybtn(self):
        """
        查询按钮
        :return:
        """
        return self.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/section/main/div/div/form/div[1]/div[2]/div/div[1]/button[1]')
        )

    def search_querydropdownbtn(self):
        """
        查询下拉框
        :return:
        """
        return self.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/section/main/div/div/form/div[1]/div[2]/div/div[1]/button[2]')
        )

    def search_querycropcodeinp(self):
        """
        判断是否存在向上收缩的下拉框按钮， 存在则返回查询栏单位编码输入框
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//i[@class="el-icon-caret-top"]')):
            return self.visibility_of_element_located((By.XPATH, '//input[@placeholder="请输入单位编号进行查询"]'))

    def search_selectcropstatusinput(self):
        """
        单位状态选择框
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//i[@class="el-icon-caret-top"]')):
            return self.visibility_of_element_located((By.XPATH, '//input[@placeholder="请选择单位状态"]'))

    def crop_status_options(self):
        """
        单位类型选项
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '/html/body/div[@class="el-select-dropdown el-popper"]')).is_displayed():
            return self.visibility_of_all_elements_located((By.XPATH, '//div[@class="el-select-dropdown '
                                                                      'el-popper"]/div/div/ul/li/span'))


    def search_dropdowni(self):
        """
        市局下拉框
        """
        return self.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div['
                                                           '2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/div/i'))

    def search_editbtn(self):
        """
        思路：先判断市局的下拉框是否被按下， 如果是，则找到编辑按钮，xpath用到了last（）
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-table__expand-icon '
                                                       'el-table__expand-icon--expanded"]')):
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div'
                                                                      '/div[2]/div/div/div[3]/table/tbody/tr[last('
                                                                      ')]/td[last()]/div/button'))

    def search_deletebtn(self):
        """
        同 edit button
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '//div[@class="el-table__expand-icon '
                                                       'el-table__expand-icon--expanded"]')):
            return self.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div'
                                                                      '/div[2]/div/div/div[3]/table/tbody/tr[last('
                                                                      ')]/td[last()]/div/span/button'))
    def query_corptr(self):
        """
        获取查询出来的tr 的[]
        //tbody/tr
        :return:
        """
        return self.visibility_of_all_elements_located((By.XPATH, '//tbody/tr[not(contains(@style, "display: none;"))]'))

    def confirm_delbtn(self):
        """
        获取确认删除的按钮
        :return:
        """
        if self.presence_of_element_located((By.XPATH, '/html/body/div[contains(@id,"el-popover-")]')).is_displayed():
            return self.visibility_of_element_located((By.XPATH, '/html/body/div[contains(@id,'
                                                                 '"el-popover-")]/div/button[2]'))


if __name__ == '__main__':
    # import os, sys
    # BASEDIR = os.path.dirname(os.path.dirname(__file__))
    # sys.path.append(BASEDIR)
    from selenium import webdriver
    import json
    import time

    dr = webdriver.Chrome(r'C:\Users\ssm\PycharmProjects\auto_ui\driver\chrome\chromedriver.exe')

    # with open('my_cookies') as f:
    #     my_cookies = json.loads(f.read())
    #     p = {}
    #     p.setdefault('name', my_cookies.get('name'))
    #     p.setdefault('value', my_cookies.get('value'))

    dr.get('http://192.168.18.149:9527/#/homepage/index')
    # a = EC.presence_of_element_located((By.XPATH, '//*[@id="el-popover-9034"]'))
    # print(a.locator)
    # print(a(dr))
    a = dr.get_window_size()
    print(a)
    dr.maximize_window()
    a = dr.get_window_size()
    print(a)
    dr.fullscreen_window()
    dr.maximize_window()
    a = dr.get_window_size()
    print(a)


    # print(p)
    # try:
        # dr.add_cookie(p)
        # dr.get('http://192.168.18.149:9527/#/homepage/index')
        # a = EC.visibility_of_element_located((By.XPATH, '//*[@id="el-popover-9034"]'))
        # print(a.locator)
        # print(a(dr))
    #     element = WebDriverWait(dr, 5, 0.5).until(
    #         # 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="el-popover-9034"]'))
    #     )
    #     print(element)
    #     # time.sleep(4)
    #     # b = IndexPage(dr)
    #     # print(b.search_full_screendiv)
    # except Exception as e:
    #     print(e)


    # dr.get('http://192.168.18.149:9527')
    # b = LoginPage(dr)
    # b.search_nameinput.clear()
    # b.search_nameinput.send_keys('admin')
    # b.search_pwdinput.clear()
    # b.search_pwdinput.send_keys('123456')
    # b.search_button.click()
    #
    #
    # time.sleep(3)
    #
    # my_cookie = json.dumps(dr.get_cookies()[0])
    # # print(type(my_cookie), my_cookie)
    # # dr.add_cookie()
    # with open('my_cookies', 'w') as f:
    #     f.write(my_cookie)

    dr.quit()







