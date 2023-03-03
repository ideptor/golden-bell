from datetime import datetime

from werkzeug.utils import redirect

from app import db
from app.forms import AnswerForm, QuestionForm
from app.models import Question
from app.views.auth_views import login_required
from flask import Blueprint, flash, g, render_template, request, url_for


bp = Blueprint("quiz", __name__, url_prefix="/quiz")


@bp.route("/<int:question_id>/")
def show(question_id: int = 1):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return question.content
    # return render_template(
    #     "question/question_detail.html", question=question, form=form
    # )
