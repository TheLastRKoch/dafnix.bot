from os import environ as env
import requests
from requests import api
import utils
import json
import re


class URLService ():
    def get_url(self, text):
        try:
            commands = text.split(" ")
            url = commands[1]
            pattern = env["CHECK_URL_PATTERN"]
            match_count = len(re.findall(pattern, url))
            if (match_count > 0):
                return url
            raise Exception("There's no valid URL in the message")

        except IndexError:
            utils.log(
                "Error", "Probably there's no valid url or command", None)
            return "Error: There's missing the URL from the command"

        except Exception as ex:
            utils.log(
                "Error", "Somthing went wrong trying validating the URL", ex)
            return "Error: " + str(ex)


class DafnixAPIService ():

    headers = {
        'Content-Type': 'application/json'
    }

    def __perform_request(self, HTML_Verb, url, headers, body):
        request = requests.request(HTML_Verb, url, headers=headers, data=body)
        if request.status_code == 200:
            dic_key = "msg"
        else:
            dic_key = "message"
        return utils.generateResponse({
            "body": json.loads(request.text)[dic_key],
            "status_code": request.status_code
        })

    def get_URL(self):
        response = self.__perform_request(
            "GET", env["DAFNIX_API_URL"], self.headers, None)

        if response.status_code == 200:
            return str(json.loads(response.data)["msg"])
        utils.log("Error", "Something went wrong with the request",
                  json.loads(response.data)["msg"])
        return "It was not possible to get the URL"

    def update_url(self, url):

        body = json.dumps({
            "url": url
        })

        response = self.__perform_request("PATCH", env["DAFNIX_API_URL"],
                                          self.headers, body)

        if response.status_code == 200:
            return json.loads(response.data)["msg"]
        return "It was not possible to update the URL"
