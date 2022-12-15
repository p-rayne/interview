from django.db import models


class Question(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Вопрос №{self.pk}"


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name="Ответ")
    code = models.TextField(null=True, verbose_name="Пример кода")
    url = models.URLField()

    def __str__(self) -> str:
        return f"Ответ на вопрос №{self.question.id}"


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name="Категория")

    def __str__(self) -> str:
        return self.name
