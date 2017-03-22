import requests
from requests.auth import HTTPBasicAuth


class RequestDemoLibrary(object):
    def __init__(self):
        self.url = "http://httpbin.org{}"
        self.get = "/get"
        self.auth = "/basic-auth/{}/{}"
        self.stream = "/stream/{}"
        self.response = None

    def request_get(self, headers=None):
        """
        Send request to http://httpbin.org/get with custom headers value
        :param headers: request headers
        :return: response to request
        """
        self.response = requests.get(self.url.format(self.get), headers=headers)
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

    def get_response_text(self):
        """
        Get response text
        :return: response text
        """
        return self.response.text

    def get_response_authorization_status(self):
        """
        Get response authorization status value from the text of response
        :return: response authorization status
        """
        if self.response.headers.get('content-type') == "application/json":
            return self.response.json()['authenticated']
        else:
            return False

    def get_response_header(self):
        """
        Get response header value from the text of response
        :return: response header value
        """
        if self.response.headers.get('content-type') == "application/json":
            return self.response.json()['headers']
        else:
            return False
