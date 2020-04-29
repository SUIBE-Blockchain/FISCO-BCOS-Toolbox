# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from fisco_bcos_toolbox.extensions import csrf_protect
import json

from fisco_bcos_toolbox.blockchain import Ethereum

api_bp = Blueprint("blockchain_api", __name__, static_folder="../static")

@api_bp.route("/generate_addr", methods=["GET", "POST"])
@csrf_protect.exempt
def gen_addr():
    payload = trans(request.get_data(as_text=True))
    if (payload == ""):
        return json.dumps(Ethereum.generate_addr())
    else:
        return json.dumps(Ethereum.generate_addr(payload["priv"]))
    
def trans(payload):
    try:
        return json.loads(payload)
        # return json.dumps(a_json, sort_keys=True, indent=4, separators=(',', ':'))
    except:
        return payload