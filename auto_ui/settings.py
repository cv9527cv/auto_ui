import os
import time
import pymysql

BASE_DIR = os.path.dirname(__file__)


class Browser:
    dr = None

class Config:
    """
        运行测试配置
    """
    now_time = time.strftime("%Y_%m_%d_%H_%M")

    # allure 报告的地址
    report_dir = os.path.join(BASE_DIR, 'report', now_time)

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    # driver_type = "chrome"

    # 存放 cookies的文件
    cookies_file = os.path.join(BASE_DIR, 'static', 'mycookies')

    # 存放日志的路径
    logger_file = os.path.join(BASE_DIR, 'log.txt')


class DB(object):
    dic = {
            'NAME': 'evidencetrack',
            'HOST': '10.1.25.147',
            'PORT': 3306,
            'USER': 'root',
            'PASSWORD': '12345'
        }

    def __init__(self, host=dic['HOST'], port=dic['PORT'], db=dic['NAME'], user=dic['USER'], passwd=dic['PASSWORD'], charset="utf8"):
        # 创建数据库连接
        self.dbconn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

        # 创建字典型游标(返回的数据是字典类型)
        self.dbcur = self.dbconn.cursor(cursor=pymysql.cursors.DictCursor)

    # __enter__() 和 __exit__() 是with关键字调用的必须方法
    # with本质上就是调用对象的enter和exit方法
    def __enter__(self):
        # 返回游标
        return self.dbcur

    def __exit__(self, exc_type, exc_value, exc_trace):
        # 提交事务
        self.dbconn.commit()

        # 关闭游标
        self.dbcur.close()

        # 关闭数据库连接
        self.dbconn.close()


if __name__ == '__main__':
    pass