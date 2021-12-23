from flask import Response
from datetime import datetime
import traceback
import json


def generateResponse(response):
    resp = Response(json.dumps({'msg': response["body"]}),
                    status=response["status_code"],
                    mimetype='application/json')
    return resp


def log(type, message, description):
    date = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
    if description is None:
        description = str(traceback.format_exc()).replace("\n", "")
    print(f"{'{'} {date}, {type}, {message}, {description} {'}'}")


def get_key_for_status_code(status_code):
    if status_code == 200:
        return "msg"
    else:
        return "message"
