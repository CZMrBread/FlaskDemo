import flask
from flask import render_template, Blueprint,redirect, flash, url_for
from App import db
from faker import Faker
from Models.User import User
my_app = Blueprint("my_app", __name__, template_folder='../templates')


@my_app.route('/')
def show_users():
    return render_template("show.html")

@my_app.route('/create-user')
def create_user():
    return render_template("show.html")


@my_app.route('/modify-user')
def create_user():
    return render_template("show.html")



@my_app.route('/generate')
def generate_fake_users(n=20):
    fake = Faker('cs_CZ')
    for _ in range(n):
        user = User(
            username=fake.unique.user_name(),
            email=fake.unique.email()
        )
        db.session.add(user)
    db.session.commit()
    flash("Users generated", "success")
    return redirect(url_for('my_app.show_users'))