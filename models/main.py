from django.db import models
from accounts import Profile

# Create your models here


class Direction(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    added_date = models.DateField(auto_now_add=True)
    direction = models.ForeignKey(Direction, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    link = models.URLField()
    img = models.ImageField(upload_to='task_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(default=False)
    point_task = models.PositiveIntegerField(default=0, blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='group_task')

    def __str__(self):
        return str(self.name)


class CompletedTasks(models.Model):
    task_file = models.FileField(upload_to='completed_tasks/%Y/%m/')
    points = models.PositiveIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='completed_task')
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='user_completed_task')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Completed Tasks'

    def __str__(self):
        return str(f'{self.author.first_name}___{self.task}')  # type: ignore


