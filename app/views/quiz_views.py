from datetime import datetime
from random import shuffle
from werkzeug.utils import redirect

from app import db
from app.forms import AnswerForm, QuestionForm
from app.models import Question
from app.views.auth_views import login_required
from flask import Blueprint, flash, g, render_template, request, url_for
import sys

bp = Blueprint("quiz", __name__, url_prefix="/quiz")

# questions = list(Question.query.order_by(Question.create_date.desc()))
# shuffle(questions)
# quiz_idx = 0
# print(quiz_num, question_list)

@bp.route("/<int:quiz_idx>/")
def show(quiz_idx: int = 0):
    # form = AnswerForm()
    # question = Question.query.get_or_404(question_id)
    # return question.content
    print(f"quiz.show(): {quiz_idx}", file=sys.stdout)

    quiz_dict = dict()
    question_list = Question.query.order_by(Question.create_date.desc())
    for question in question_list:
        quiz_dict[question.id] = question

    quiz_ids = sorted(list(quiz_dict.keys()))
    print(f"quiz.show() quiz_ids: {quiz_ids}", file=sys.stdout)

    if quiz_idx >= len(quiz_ids):
        return "<h1>퀴즈가 종료되었습니다</h1>"
    
    return render_template(
        "quiz/quiz.html", 
        quiz_num=(quiz_idx+1), 
        question=question_list.get(quiz_ids[quiz_idx])
    )

