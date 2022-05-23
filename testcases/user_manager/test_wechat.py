import re
import random

import allure
import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_testcase_yaml


@allure.epic("中国移动SAAS管理系统")
@allure.feature("用户管理")
class TestApi:

    csrf_token = ""

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/get_token.yaml"))
    def test_get_token(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["params"]
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, params=datas)
        result = res.json()
        data = {"access_token": result["access_token"]}
        print(data)
        write_yaml("extract.yaml", data)
        # TestApi.access_token = result["access_token"]

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/select_flag.yaml"))
    def test_select_flag(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        datas = caseinfo["request"]["params"]
        datas["access_token"] = read_yaml("extract.yaml", "access_token")
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, data=datas)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/edit_flag.yaml"))
    def test_edit_flag(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["json"]
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, params=params, json=datas)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/delete_flag.yaml"))
    def test_delete_flag(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["json"]
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, params=params, json=datas)
        result = res.json()
        print(result, type(result))

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("testcases/user_manager/file_upload.yaml"))
    def test_file_upload(self, caseinfo):
        name = caseinfo["name"]
        method = caseinfo["request"]["method"]
        urls = caseinfo["request"]["url"]
        headers = caseinfo["request"]["headers"]
        params = caseinfo["request"]["params"]
        params["access_token"] = read_yaml("extract.yaml", "access_token")
        datas = caseinfo["request"]["files"]
        for key, value in datas.items():
            datas[key] = open(value, 'rb')
        validates = caseinfo["validate"]

        res = RequestUtil().send_all_request(method=method, url=urls, params=params, files=datas)
        result = res.json()
        print(result, type(result))
    #
    # def test_index(self):
    #     url = "http://47.107.116.139/phpwind/"
    #     res = RequestUtil().send_all_request(method="get", url=url)
    #     # res = request.get(url=url)
    #     result = res.text
    #     data = {"csrf_token": re.search('name="csrf_token" value="(.*?)"', result).group(1)}
    #     write_yaml("extract.yaml", data)
    #
    # def test_login(self):
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     datas = {
    #         "username": "admin",
    #         "password": "msjy123",
    #         "csrf_token": read_yaml("extract.yaml", "csrf_token"),
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     headers = {
    #         "Accept": "application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     res = RequestUtil().send_all_request(method="post", url=url, data=datas, headers=headers)
    #     result = res.text
    #     print(result, type(result))

    #
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