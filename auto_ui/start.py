import pytest
import logging
from settings import Browser, Config
from selenium import webdriver


# my_format = '%(asctime)s:%(levelname)s:%(message)s'
# logging.basicConfig(filename=Config.logger_file, format=my_format, filemode='w', level=logging.DEBUG)
logging.basicConfig(filemode='w', filename='log.txt')
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('--loging information--')

    # linux 无头浏览器运行
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--disable-gpu')
    chromeOptions.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片
    chrome_options = chromeOptions
    executable_path = "/usr/bin/chromedriver"
    Browser.dr = webdriver.Remote(
        command_executor='http://10.1.25.247:4444/wd/hub',
        options=chromeOptions
    )

    # 正常windows运行
    # Browser.dr = webdriver.Chrome('./driver/chrome/chromedriver.exe')

    Browser.dr.maximize_window()
    pytest.main(['-s', '-v', '--reruns=1', '--alluredir={}'.format(Config.report_dir), '--clean-alluredir', '--maxfail=2'])
    Browser.dr.quit()
    logger.info('-- exit --')




    """
    """