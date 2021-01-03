import pytest
from selenium import webdriver


l = [1, 3, 2]

@pytest.mark.parametrize('id_', l)
def a_test_case(id_):
    """

    des
    :return:
    """
    # print(b)
    assert 1==2


import os, sys
BASEDIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASEDIR)
from pageobj.page import LoginPage
from settings import Browser
import time
# from selenium import webdriver

class TestLoginPage():


    def setup_class(self):
        self.base_url = 'http://10.1.25.147:9527/'
        self.page = LoginPage(Browser.dr)


    def test_title(self):
        Browser.dr.get(self.base_url)
        self.title = Browser.dr.title
        assert self.title == '现场物证溯源智能管控平台23232'

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)

logging.debug('debug ssm')
logging.info('info ssm')
logging.warning('waring ssm')
logging.error('error ssm')
logging.critical('critical ssm')
print('-----'*10)
logging.log(logging.DEBUG, 'ssm')
logging.log(logging.INFO, 'ssm')
logging.log(logging.WARNING, 'ssm')
logging.log(logging.ERROR, 'ssm')
logging.log(logging.CRITICAL, 'ssm')


