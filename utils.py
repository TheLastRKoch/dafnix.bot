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
