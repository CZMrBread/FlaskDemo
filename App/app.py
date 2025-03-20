from flask import render_template, Blueprint
my_app = Blueprint("my_app", __name__, template_folder='../templates')


@my_app.route('/')
def index():
    return render_template("index.html")