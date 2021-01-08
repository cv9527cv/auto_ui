from pageobj.page import LoginPage
from settings import Browser
import time
import pytest
import allure
import logging


"""
blocker：阻塞缺陷（功能未实现，无法下一步）
critical：严重缺陷（功能点缺失）
normal： 一般缺陷（边界情况，格式错误）
minor：次要缺陷（界面错误与ui需求不符）
trivial： 轻微缺陷（必须项无提示，或者提示不规范）
"""
logger = logging.getLogger(__name__)


@allure.epic('登录')
@allure.feature('登录模块')
@pytest.mark.login
@pytest.mark.run(order=1)
class TestLoginPage():

    def setup_class(self):
        self.base_url = 'http://10.1.25.147:9527/'
        self.page = LoginPage(Browser.dr)

    @allure.story('页面标题测试')
    # @pytest.mark.skip(msg='任性')
    @allure.severity(allure.severity_level.MINOR)
    def test_title(self):
        Browser.dr.get(self.base_url)
        title = Browser.dr.title
        logger.info(pytest.assume(title == '现场物证溯源智能管控平台'))

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('登录测试')
    @allure.title("测试数据是用户名:{title_}")
    @pytest.mark.parametrize('name_, pwd_, title_',
        [
            pytest.param('admin', '', '预期失败', marks=pytest.mark.xfail),
            pytest.param('', '1234', '跳过', marks=pytest.mark.skip),
            ('admin', '123456', '登录成功')
        ]
    )
    def test_login(self, name_, pwd_, title_):
        Browser.dr.get(self.base_url)
        self.page.search_nameinput.clear()
        self.page.search_nameinput.send_keys(name_)
        self.page.search_pwdinput.clear()
        self.page.search_pwdinput.send_keys(pwd_)
        self.page.search_button.click()
        time.sleep(5)
        logger.info(pytest.assume(Browser.dr.current_url == 'http://10.1.25.147:9527/#/homepage/index'))


