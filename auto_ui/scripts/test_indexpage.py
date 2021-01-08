from pageobj.page import IndexPage
from settings import Browser
import pytest
import time
import logging

logger = logging.getLogger(__name__)

# @pytest.mark.skip(msg='nibudong')
@pytest.mark.index
@pytest.mark.run(order=2)
class TestIndexPage():

    def setup_class(self):
        self.base_url = 'http://10.1.25.147:9527/#/homepage/index'
        # Browser.dr.maximize_window()
        self.page = IndexPage(Browser.dr)

    # @pytest.mark.skip(msg='任性')
    def test_click_evidencea(self):
        Browser.dr.get(self.base_url)
        self.page.search_evidencea.click()
        logger.info(pytest.assume(Browser.dr.current_url == 'http://10.1.25.147:9527/#/evidence/evidence'))

    # @pytest.mark.skip(msg='任性')
    def test_click_warninga(self):
        Browser.dr.get(self.base_url)
        self.page.search_warninga.click()
        logger.info(pytest.assume(Browser.dr.current_url == 'http://10.1.25.147:9527/#/alarm/bind'))

    # @pytest.mark.skip(msg='任性')
    def test_click_basicinfoa(self):
        Browser.dr.get(self.base_url)
        self.page.search_basicinfoa.click()
        logger.info(pytest.assume(Browser.dr.current_url == 'http://10.1.25.147:9527/#/police/user'))

    # @pytest.mark.skip(msg='任性')
    def test_click_indexa(self):
        # Browser.dr.get(self.base_url)
        self.page.search_indexa.click()
        logger.info(pytest.assume(Browser.dr.current_url == 'http://10.1.25.147:9527/#/homepage/index'))

    # @pytest.mark.skip(msg='nibudong')
    # @pytest.mark.flaky(reruns=2)
    def test_page_full_screen(self):
        Browser.dr.get(self.base_url)
        size1 = Browser.dr.get_window_size()
        self.page.search_dropdownboxi.click()
        self.page.search_full_screendiv.click()
        time.sleep(2)
        size2 = Browser.dr.get_window_size()
        logger.info(pytest.assume(size1 != size2))

    @pytest.mark.repeat(2)
    # @pytest.mark.skip(msg='renxin')
    def test_logout(self):
        Browser.dr.get(self.base_url)
        self.page.search_dropdownboxi.click()
        self.page.search_logoutdiv.click()
        logger.info(pytest.assume(self.page.search_logoutalter.text == '退出登录？'))
        # Browser.dr.refresh()





