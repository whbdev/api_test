import requests


class RequestUtil:
    sess = requests.session()

    # 统一请求的方法
    def send_all_request(self, method, url, **kwargs):
        res = RequestUtil.sess.request(method, url, **kwargs)
        return res