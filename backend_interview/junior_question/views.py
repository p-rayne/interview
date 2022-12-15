from django.views.generic import ListView, TemplateView
from typing import Any, Dict
from .models import Question


class QuestionListView(ListView):
    model = Question
    template_name = "junior_question/question.html"
    queryset = (
        Question.objects.all()
        .select_related("category", "answer")
        .order_by("category__id")
    )


class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["amount"] = Question.objects.count()
        return context
