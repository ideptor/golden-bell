from werkzeug.utils import redirect

from flask import Blueprint, url_for, g

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello_pybo():
    return "Hello, Pybo!"


@bp.route("/")
def index():
    return redirect(url_for("quiz.show", quiz_idx=0))
