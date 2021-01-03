from pageobj.page import BaseInfoPage
from settings import Browser
import pytest


@pytest.mark.skip(msg='re')
@pytest.mark.index
@pytest.mark.run(order=3)
class TestBaseInfoPage():

    def setup_class(self):
        self.base_url = 'http://192.168.18.149:9527/#/police/user'
        # Browser.dr.maximize_window()
        self.page = BaseInfoPage(Browser.dr)

    def test_userinfoli(self):
        Browser.dr.get(self.base_url)
        self.page.search_userinfoli()
        self.page.search_usermagmtli().click()
        pytest.assume(Browser.dr.current_url == 'http://192.168.18.149:9527/#/police/user')

    def test_cropinfoli(self):
        Browser.dr.get(self.base_url)
        self.page.search_cropinfoli().click()
        self.page.search_cropmagmtli().click()
        pytest.assume(Browser.dr.current_url == 'http://192.168.18.149:9527/#/corpinfo/corp')
        self.page.search_roommagmtli().click()
        pytest.assume(Browser.dr.current_url == 'http://192.168.18.149:9527/#/corpinfo/room')
