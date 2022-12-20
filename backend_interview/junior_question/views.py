from django.views.generic import ListView, TemplateView
from typing import Any, Dict
from .models import Question

active_link = "disabled border rounded bg-light shadow-sm"


class QuestionPythonListView(ListView):
    model = Question
    template_name = "junior_question/python.html"
    extra_context = {
        "active_python": active_link,
        "category": "Python",
    }
    queryset = Question.objects.filter(category__name="Python").select_related(
        "category", "answer"
    )
    paginate_by = 20


class QuestionDjangoListView(ListView):
    model = Question
    template_name = "junior_question/django.html"
    extra_context = {
        "active_django": active_link,
        "category": "Django",
    }
    queryset = Question.objects.filter(category__name="Django").select_related(
        "category", "answer"
    )
    paginate_by = 20


class QuestionSQLListView(ListView):
    model = Question
    template_name = "junior_question/SQL.html"
    extra_context = {
        "active_sql": active_link,
        "category": "SQL",
    }
    queryset = Question.objects.filter(category__name="SQL").select_related(
        "category", "answer"
    )
    paginate_by = 20


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "active_main": active_link,
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["amount"] = Question.objects.count()
        return context
