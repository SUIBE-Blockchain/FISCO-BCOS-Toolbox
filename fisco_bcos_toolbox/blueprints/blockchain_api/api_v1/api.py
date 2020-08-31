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
    send_from_directory,
    send_file,
    make_response,
    jsonify
)

from fisco_bcos_toolbox.extensions import csrf_protect
import json,os

from fisco_bcos_toolbox.blockchain import Ethereum
# from __future__ import print_function
import random
from fisco_bcos_toolbox.blockchain import Bitcoin

api_bp = Blueprint("blockchain_api", __name__, static_folder="../static")
now_path = 'fisco_bcos_toolbox\\blueprints\\blockchain_api\\api_v1'

@api_bp.route("/generate_addr", methods=["GET", "POST"])
@csrf_protect.exempt
def gen_addr():
    payload = trans(request.get_data(as_text=True))
    if (payload == ""):
        priv = request.args.get("priv")
        if priv == None:
            return json.dumps(Ethereum.generate_addr())
    else:
        priv = payload["priv"]
    
    return json.dumps(Ethereum.generate_addr(priv))


@api_bp.route("/generate_btcAddr", methods=["GET", "POST"])
@csrf_protect.exempt
def gen_btcAddr():
    payload = trans(request.get_data(as_text=True))
    if (payload == ""):
        priv = request.args.get("priv")
        if priv == None:
            return json.dumps(Bitcoin.generate_addr())
    else:
        priv = payload["priv"]

    return json.dumps(Bitcoin.generate_addr(priv))


@api_bp.route("/translate_sig", methods=["GET","POST"])
@csrf_protect.exempt
def translate_sig():
    if request.method == "GET":
        sig = request.args.get("sig")
    else:
        sig = trans(request.get_data(as_text=True))["sig"]
    
    return json.dumps(Ethereum.split_sig(sig))   

def trans(payload):
    try:
        return json.loads(payload)
        # return json.dumps(a_json, sort_keys=True, indent=4, separators=(',', ':'))
    except:
        return payload


@api_bp.route("/get_sdk_config", methods=["POST"])
@csrf_protect.exempt
def get_sdk_config():
    payload = trans(request.get_data(as_text=True))
    path=os.getcwd()
    if get_sdk_config_tool(payload):
        response=make_response(send_file("{}\\{}\\client_config.py".format(path,now_path)))
        response.headers["Content-Disposition"] = "attachment; filename=client_config.py"
    else:
        response='erro'
    return response


def get_sdk_config_tool(data):
    try:
        with open('{}\\client_config.py.template'.format(now_path),'r',encoding='utf8') as r:
            _t=r.read()
            _t=_t.format(**data)
            with open('{}\\client_config.py'.format(now_path),'w',encoding='utf8') as w:
                w.write(_t)
    except Exception:
        return False
    return True
        
@api_bp.route('/random_bytes32', methods=['GET'])
def random_bytes32():
    data = random.randint(10000000000000000000000000000000000000000000000000000000000000000000000000000, 99999999999999999999999999999999999999999999999999999999999999999999999999999)

    return jsonify({
        'code':'200',
        'message':hex(data)
    })
@api_bp.route('/random_bytes', methods=['GET'])
def random_bytes():
    data = random.randint(10, 99)

    return jsonify({
        'code':'200',
        'message':hex(data)
    })


@api_bp.route('/random_int', methods=['GET'])
def random_int():
    data = random.randint(1,1999989)
    return jsonify({
        'code':'200',
        'message':str(data),
    })

