from django.views.generic import ListView, TemplateView

from .models import Question
from backend_interview.utils.functions import get_question

active_link = "disabled border rounded bg-light shadow-sm"


class QuestionPythonListView(ListView):
    model = Question
    template_name = "junior_question/python.html"
    extra_context = {
        "active_python": active_link,
        "category": "Python",
    }
    paginate_by = 10

    def get_queryset(self) -> list[any]:
        return get_question("Python")


class QuestionDjangoListView(ListView):
    model = Question
    template_name = "junior_question/django.html"
    extra_context = {
        "active_django": active_link,
        "category": "Django",
    }
    paginate_by = 10

    def get_queryset(self) -> list[any]:
        return get_question("Django")


class QuestionSQLListView(ListView):
    model = Question
    template_name = "junior_question/SQL.html"
    extra_context = {
        "active_sql": active_link,
        "category": "SQL",
    }
    paginate_by = 10

    def get_queryset(self) -> list[any]:
        return get_question("SQL")


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "active_main": active_link,
    }

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["amount"] = Question.objects.count()
        return context
