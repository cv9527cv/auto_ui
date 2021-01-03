import pytest
from settings import Browser, Config
from selenium import webdriver

if __name__ == '__main__':
    Browser.dr = webdriver.Chrome('./driver/chrome/chromedriver.exe')
    Browser.dr.maximize_window()
    pytest.main(['-s', '-v', '--reruns=1', '--alluredir={}'.format(Config.report_dir), '--clean-alluredir', '--maxfail=2'])
    Browser.dr.quit()

    """
    """