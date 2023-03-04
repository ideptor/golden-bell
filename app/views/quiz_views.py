from datetime import datetime
from werkzeug.utils import redirect

from app import db
from app.forms import EvaluationForm
from app.models import Question
from flask import Blueprint, render_template, url_for
import sys
from collections import defaultdict
from typing import Tuple

bp = Blueprint("quiz", __name__, url_prefix="/quiz")

scores = dict(
    kpg=defaultdict(bool),
    koy=defaultdict(bool),
    kme=defaultdict(bool),
)


def get_quiz_ids() -> Tuple[list, list]:
    quiz_set = set()
    question_list = Question.query.order_by(Question.create_date.desc())

    for question in question_list:
        quiz_set.add(question.id)

    quiz_ids = sorted(list(quiz_set))
    print(f"quiz.show() quiz_ids: {quiz_ids}", file=sys.stdout)

    return quiz_ids, question_list


@bp.route("/<int:quiz_idx>/")
def show(quiz_idx: int = 0):
    print(f"quiz.show(): {quiz_idx}", file=sys.stdout)

    quiz_ids, question_list = get_quiz_ids()

    if len(quiz_ids) <= 0:
        return redirect(url_for("question._list"))

    if quiz_idx >= len(quiz_ids):
        return "<h1>퀴즈가 종료되었습니다</h1>"

    return render_template(
        "quiz/quiz.html",
        quiz_idx=quiz_idx,
        question=question_list.get(quiz_ids[quiz_idx]),
    )


@bp.route("/answer/<int:quiz_idx>/")
def answer(quiz_idx: int):
    print(f"quiz.answr.show(): {quiz_idx}", file=sys.stdout)

    quiz_ids, question_list = get_quiz_ids()

    return render_template(
        "quiz/quiz_answer.html",
        quiz_idx=quiz_idx,
        question=question_list.get(quiz_ids[quiz_idx]),
    )
