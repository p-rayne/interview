from django.urls import path
from .views import QuestionListView, IndexTemplateView

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="main"),
    path("question/", QuestionListView.as_view(), name="question_list"),
]
