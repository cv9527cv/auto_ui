import pytest
import os
import allure
from settings import Browser


_driver = Browser.dr


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    # 获取钩子方法的调用结果
    out = yield
    # 3. 从钩子方法的调用结果中获取测试报告
    rep = out.get_result()
    #     print('测试报告：%s' % rep)
    #     print('步骤：%s' % rep.when)
    #     print('nodeid：%s' % rep.nodeid) ---> scripts/mytest.py::TestLoginPage::test_title
    #     print('description:%s' % str(item.function.__doc__)) --> testcase的描述
    #     print(('运行结果: %s' % rep.outcome))
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        # item.fixturenames---->  testcase 传入的参数名列表 ['id_']  实验得出  不保证正确
        # item.funcargs-------->  testcase 传入的参数名：值 字典 {'id_':2}  实验得出  不保证正确
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
