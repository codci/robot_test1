import requests
from requests.auth import HTTPBasicAuth


class RequestDemoLibrary(object):
    """
    asd
    """

    def __init__(self):
        self.url = "http://httpbin.org{}"
        self.get = "/get"
        self.auth = "/basic-auth/{}/{}"
        self.stream = "/stream/{}"

    def request_get(self):
        """

        :return:
        """
        response = requests.get(self.url.format(self.get))
        return response

    def request_auth(self, user, passwd):
        """

        :param user:
        :param passwd:
        :return:
        """
        base_auth = HTTPBasicAuth(user, passwd)
        response = requests.get(self.url.format(self.auth.format(user, passwd)), auth=base_auth)
        return response.status_code

    def request_stream(self, count):
        """

        :param count:
        :return:
        """
        response = requests.get(self.url.format(self.stream.format(count)))
        return response

print RequestDemoLibrary().request_auth("sd", "sd")
