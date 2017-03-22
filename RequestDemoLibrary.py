import requests
from requests.auth import HTTPBasicAuth
import json


class RequestDemoLibrary(object):
    """
    asd
    """

    def __init__(self):
        self.url = "http://httpbin.org{}"
        self.get = "/get"
        self.auth = "/basic-auth/{}/{}"
        self.stream = "/stream/{}"
        self.response = None

    def request_get(self):
        """
        Send request to httpbin.org/get
        :return: response to request
        """
        headers = {'test': 'my-app/0.0.1'}
        self.response = requests.get(self.url.format(self.get, headers=headers))
        return self

    def request_auth(self, user, passwd):
        """
        Send request to http://httpbin.org/basic-auth/:user/:passwd with auth params
        :param user: Username for Auth
        :param passwd: Password for Auth
        :return: response to request
        """
        base_auth = HTTPBasicAuth(user, passwd)
        self.response = requests.get(self.url.format(self.auth.format(user, passwd)), auth=base_auth)
        return self

    def request_stream(self, count):
        """
        Send request to http://httpbin.org//stream/:count with auth params
        :param count: number of streams
        :return: response to request
        """
        self.response = requests.get(self.url.format(self.stream.format(count)))
        return self

    def get_response_status_code(self):
        """
        Get response status code
        :return: status code
        """
        return str(self.response.status_code)

    def status_code_should_be(self, status_code):
        actual_status_code = self.get_response_status_code()
        if actual_status_code != int(status_code):
            raise AssertionError('Actual Status code != Expected: %s != %s' % (actual_status_code, status_code))
        return self

    def number_of_lines_should_be(self, number_of_lines):
        actual_number_of_lines = len(self.get_response_text().splitlines())
        if actual_number_of_lines != int(number_of_lines):
            raise AssertionError(
                'Actual Number of lines != Expected: %s != %s' % (actual_number_of_lines, number_of_lines))
        return self

    def authorization_status_should_be(self, auth_status):
        actual_auth_status = self.get_response_authorization_status()
        if actual_auth_status != bool(auth_status):
            raise AssertionError(
                'Actual Authorization status != Expected: %s != %s' % (actual_auth_status, auth_status))
        return self

    def get_response_text(self):
        """

        :param response:
        :return:
        """
        return self.response.text

    def get_response_authorization_status(self):
        if self.response.headers.get('content-type') == "application/json":
            return self.response.json()['authenticated']
        else:
            raise AssertionError(
                '%s != %s' % (self.response.headers.get('content-type'), str("application/json")))


r = RequestDemoLibrary()
r.request_auth("asd", "qwezsd")
print r.response.headers.get('content-type')
print type(r.response.status_code)
# print RequestDemoLibrary().request_auth("asd", "asd").response.text
# print RequestDemoLibrary().get_response_line_count(RequestDemoLibrary().request_stream(99))
