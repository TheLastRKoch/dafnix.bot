from os import environ as env
import os
import requests
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
        response = requests.request(HTML_Verb, url, headers=headers, data=body)
        dic_key = utils.get_key_for_status_code(response.status_code)
        return utils.generateResponse({
            "body": json.loads(response.text)[dic_key],
            "status_code": response.status_code
        })

    def get_URL(self):
        response = self.__perform_request(
            "GET", env["DAFNIX_API_URL"], self.headers, None)

        if response.status_code == 200:
            return str(json.loads(response.data)["msg"])
        message = "It was not possible to get the URL"
        utils.log("Error", message,
                  response.data)
        return message

    def update_url(self, url):

        body = json.dumps({
            "url": url
        })

        response = self.__perform_request("PATCH", env["DAFNIX_API_URL"],
                                          self.headers, body)

        if response.status_code == 200:
            return json.loads(response.data)["msg"]
        message = "It was not possible to update the URL"
        utils.log("Error", message,
                  response.data)
        return message


class TemplateManagerService ():
    def read_template(self, template_name):
        basedir = os.path.abspath(os.path.dirname(__file__))
        templates_path = os.path.join(
            basedir, env["TEMPLATE_PATH"], template_name+".md")
        with open(templates_path) as f:
            print(f.read())


if __name__ == '__main__':

    tms = TemplateManagerService()
    tms.read_template("welcome")
