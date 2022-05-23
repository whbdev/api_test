import re
import random

import allure
import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_testcase_yaml


@allure.epic("中国移动SAAS管理系统")
@allure.feature("商品管理")
class TestApi:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_index.yaml"))
    def test_index(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        res = RequestUtil().send_all_request(method=method, url=urls)
        # res = request.get(url=url)
        result = res.text
        data = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result).group(1)}
        write_yaml("extract.yaml", data)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/product_manager/phpwind_login.yaml"))
    def test_login(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["data"]
        datas["csrf_token"] = read_yaml("extract.yaml", "csrf_token")
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, data=datas, headers=headers)
        result = res.text
        print(result, type(result))


    # @allure.story("码上教育接口")
    # # @allure.title("码上教育正例1")
    # @allure.severity(allure.severity_level.BLOCKER)
    # # @allure.description("用例的描述")
    # @allure.link("接口访问的链接")
    # @allure.issue("Bug链接")
    # @allure.testcase("测试用例的链接")
    # def test_mashang(self, base_url):
    #     allure.dynamic.title("码上教育正例2")
    #     allure.dynamic.description("用例的描述2")
    #     print(base_url + '码上教育')
    #     for i in range(1, 11):
    #         with allure.step("测试用例的第"+str(i)+"步"):
    #             pass
    #     with open("D:\\test.png", mode='rb') as f:
    #         allure.attach(body=f.read(), name="登录错误截图", attachment_type=allure.attachment_type.JPG)
    #         pass
    #     assert 'a' in 'abc'