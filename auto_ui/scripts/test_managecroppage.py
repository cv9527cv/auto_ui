from pageobj.page import ManageCropPage
from settings import Browser, DB
import time
import pytest
import allure
import logging

logger = logging.getLogger(__name__)

@allure.epic('用户管理')
@pytest.mark.run(order=4)
class TestManageCorpPage():

    def setup_class(self):
        self.base_url = 'http://10.1.25.147:9527/#/corpinfo/corp'
        self.page = ManageCropPage(Browser.dr)

    # @pytest.mark.skip(msg='跳过')
    @allure.story('新增单位')
    @allure.title('默认输入[ssmtest2, 1234507231, 市局, 西湖]')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001_add_corp(self):
        Browser.dr.get(self.base_url)
        self.page.search_addbut().click()
        time.sleep(2)
        # 输入单位名称
        self.page.search_addcropnameinput().send_keys('ssmtest2')
        # 输入单位编码
        self.page.search_addcropcodeinput().send_keys('1234507231')
        # 点击单位类型下拉框, 点击[0](市局类型)
        self.page.search_addcroptype().click()
        self.page.search_croptypes()[0].click()
        # 输入单位地址
        self.page.search_cropaddressinput().send_keys('西湖')
        # 点击确认按钮
        self.page.search_confirmbut().click()
        # pytest.assume(self.page.search_promptdiv().text == '添加成功')
        logger.info(pytest.assume(self.page.search_promptdiv().text == '添加成功'))

    @allure.story('编辑单位')
    @allure.title('默认输入[ssmtest3, 1234507231, 市局, 西湖]')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_002_edit_corp(self):
        Browser.dr.get(self.base_url)
        # 点击单位列表中杭州市局的下拉框
        self.page.search_dropdowni().click()
        # 点击编辑按钮
        self.page.search_editbtn().click()

        time.sleep(2)
        # 输入单位名称
        name = self.page.search_addcropnameinput()
        name.clear()
        name.send_keys('ssmtest3')
        # 输入单位编码
        code_ = self.page.search_addcropcodeinput()
        code_.clear()
        code_.send_keys('1234507231')
        # 点击单位类型下拉框, 点击[0](市局类型)
        self.page.search_addcroptype().click()
        self.page.search_croptypes()[0].click()
        # 输入单位地址
        address = self.page.search_cropaddressinput()
        address.clear()
        address.send_keys('西湖')
        # 点击确认按钮
        self.page.search_confirmbut().click()
        logger.info(pytest.assume(self.page.search_promptdiv().text == '修改成功'))

    @allure.story('查询单位')
    @allure.title('查询单位')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_query_corp(self):
        Browser.dr.get(self.base_url)
        self.page.search_querydropdownbtn().click()
        self.page.search_querycropcodeinp().send_keys('001')
        self.page.search_selectcropstatusinput().click()
        self.page.crop_status_options()[1].click()
        self.page.serach_querybtn().click()
        with DB() as dbcur:
            sql = "select * from corp where code = '001';"
            count = dbcur.execute(sql)
        li_tr = self.page.query_corptr()
        logger.info(pytest.assume(len(li_tr) == count))

    @allure.story('删除单位')
    @allure.title('删除单位')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_004_del_corp(self):
        Browser.dr.get(self.base_url)
        # 点击单位列表中杭州市局的下拉框
        self.page.search_dropdowni().click()
        # 点击最后一条数据的删除按钮
        self.page.search_deletebtn().click()
        time.sleep(2)
        self.page.confirm_delbtn().click()
        logger.info(pytest.assume(self.page.search_promptdiv().text == '删除成功'))



