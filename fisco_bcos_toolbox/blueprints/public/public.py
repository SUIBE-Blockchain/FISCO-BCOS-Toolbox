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
from flask_login import login_required, login_user, logout_user, current_user

from fisco_bcos_toolbox.extensions import login_manager
from fisco_bcos_toolbox.forms import RegisterForm, LoginForm
from fisco_bcos_toolbox.models import User
from fisco_bcos_toolbox.utils import flash_errors, redirect_back
from fisco_bcos_toolbox.extensions import db

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
    # TODO
    mock_data_type = ["byte32", "int", "bytes"]
    trans_type = ["signature"]
    return render_template("public/home.html",
     form=form,
     mock_data_type=mock_data_type,
     trans_type=trans_type,
     )


@public_bp.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))



@public_bp.route('/login', methods=['GET', 'POST'])
def login():
    # login in func
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))

    form = LoginForm()
    if form.validate_on_submit():
        username_or_email = form.username.data
        password = form.password.data
        # remember = form.remember.data
        user = [User.query.filter(User.username==username_or_email).first(), User.query.filter(User.email==username_or_email).first()]
        if user[0]:
            if user[0].check_password(password):
                # login_user(user[0], remember)
                login_user(user[0])
                flash('Welcome back.', 'info')
                return redirect_back()
            else:
                flash('账号或者密码错误，请重新输入！', 'warning')
        elif user[1]:
            if user[1].check_password(password):
                login_user(user[1])
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
        
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password1 = form.confirm.data
        if not all([username, email, password, password1]):
            flash('请把信息填写完整', "warning")
        elif password != password1:
            flash('两次密码不一致，请重新输入！', "warning")
        elif User.query.filter(User.username==username).first():
            flash('这个用户名已经被注册过了！', "warning")
        elif User.query.filter(User.email==email).first():
            flash('这个邮箱已经被注册过了！', "warning")
        else:
            new_user = User(username=username, email=email, active=False, id=None)
            # add a User(active = False)
            new_user.set_password(password)
            db.session.add(new_user)
            # try:
            #     db.session.commit()
                
            #     return redirect(url_for('public.home'))
            # except:
            #     flash("注册失败，请重试！")
            #     db.session.rollback()
            db.session.commit()
            flash("感谢注册，请联系管理员激活账号！", "success")
            return redirect(url_for('public.login'))
    return render_template('public/register.html', form=form)



@public_bp.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)

@public_bp.route("/sdk_config/")
def sdk_config():
    """About page."""
    form = LoginForm(request.form)
    crypto_type = ['ECDSA','GM']
    return render_template("public/sdk_config.html", 
    form=form,
    crypto_type=crypto_type,
    )