# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required
from fb_python_sdk.client_config import client_config

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")

@blueprint.route("/sdk_config")
@login_required
def sdk_config():
    """List members."""
    # TODO handle url and posts
    return render_template("users/sdk_config.html", client_config=client_config)