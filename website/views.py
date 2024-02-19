from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@views.route("/home/")
def redirect_lang():
    return render_template("landing_page.html")


@views.route("/en")
@views.route("/en/")
@views.route("/en/home")
@views.route("/en/home/")
def home_en():
    return render_template("home.html")


@views.route("/en/who_we_are")
@views.route("/en/who_we_are/")
def who_we_are_en():
    return render_template("who_we_are.html")


@views.route("/en/how_to_use")
@views.route("/en/how_to_use/")
def how_to_use_en():
    return render_template("how_to_use.html")


@views.route("/en/order_now")
@views.route("/en/order_now/")
def order_now_en():
    return render_template("order_now.html")


@views.route("/en/contact_us")
@views.route("/en/contact_us/")
def contact_us_en():
    return render_template("contact_us.html")


@views.route("/en/terms_and_conditions")
@views.route("/en/terms_and_conditions/")
def terms_and_conditions_en():
    return render_template("terms_and_conditions.html")
