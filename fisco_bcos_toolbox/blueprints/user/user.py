# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

user_bp = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@user_bp.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")
