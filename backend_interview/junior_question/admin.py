from django.contrib import admin
from .models import Question, Answer, Category


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
        "category",
    )
    list_display_links = ("id", "question")
    search_fields = ("id", "question")
    list_filter = ("category",)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question_id", "answer")
    list_display_links = ("id", "question_id")
    search_fields = ("id", "question_id")


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("id", "name")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category, CategoryAdmin)
