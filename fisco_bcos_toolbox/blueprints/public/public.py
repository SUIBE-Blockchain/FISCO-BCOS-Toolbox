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
from flask_login import login_required, login_user, logout_user

from fisco_bcos_toolbox.extensions import login_manager
from fisco_bcos_toolbox.forms import RegisterForm, LoginForm
from fisco_bcos_toolbox.models import User
from fisco_bcos_toolbox.utils import flash_errors

public_bp = Blueprint("public", __name__, static_folder="../static")


@public_bp.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@public_bp.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))

@public_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login user."""
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter(User.username==username).first()
        if user:
            if user.check_password(password):
                login_user(user)
                flash('Welcome back.', 'info')
                return redirect_back()
            else:
                flash('账号或者密码错误，请重新输入！', 'warning') 
        else:
            flash('No account.', 'warning')
    return render_template('public/login.html', form=form)


@public_bp.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))
        
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=False,
        )
        flash("感谢注册，请联系管理员激活账号！", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@public_bp.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
