from django.urls import path
from .views import (
    QuestionDjangoListView,
    QuestionPythonListView,
    QuestionSQLListView,
    IndexTemplateView,
)

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="main"),
    path("question/python", QuestionPythonListView.as_view(), name="question_python"),
    path("question/django", QuestionDjangoListView.as_view(), name="question_django"),
    path("question/sql", QuestionSQLListView.as_view(), name="question_sql"),
]
