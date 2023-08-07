from django.db import models
from accounts import Profile

# Create your models here


class LeadUser(models.Model):
    firs_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return str(f'{firs_name}  {last_name}')


class Direction_for_quiz(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    quiz = models.TextField()

    direction = models.ForeignKey(
        Direction_for_quiz, on_delete=models.CASCADE, related_name="direction_for_questions")

    def __str__(self):
        return str(self.title)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, blank=True, null=True, related_name='false_answers')
    false_answer = models.CharField(max_length=250)

    def __str__(self):
        return str(self.false_answer)


class CountTrueAnswer(models.Model):
    count_true_answers = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="user_answers")
    direction = models.ForeignKey(
        Direction_for_quiz, on_delete=models.PROTECT, related_name="direction_for_count")
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT, related_name="questions_for_count")
