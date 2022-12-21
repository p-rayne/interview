from backend_interview.junior_question.models import Question
from random import shuffle, sample


def get_question(cat: str, sample_count: int = 0) -> list:
    """
    By default, the QuerySet is returned in random order as a list.
    Otherwise, it will return a list of randomly selected objects
    in the amount equal to sample_count.
    """
    result = list(
        Question.objects.filter(category__name=cat).select_related("category", "answer")
    )
    if sample_count:
        return sample(result, sample_count)
    shuffle(result)
    return result
