from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings
from main_app.models import Direction, Group, Task

# Create your models here.


class Profile(User):
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name='user_direction', blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to='user_images/', default='default.jpg', blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    telegram_link = models.CharField(max_length=200, blank=True, null=True)
    work_group = models.ForeignKey(
        Group, on_delete=models.PROTECT, blank=True, null=True)
    is_moderator = models.BooleanField(default=False, blank=True, null=True)
    points = models.PositiveIntegerField(default=0, blank=True, null=True)
    doned_tasks = models.ManyToManyField(
        Task, related_name='doned_tasks', blank=True)

    def get_robo_coints(self):
        return int(self.points) / 10  # type: ignore

    def get_phone_number(self):
        return int(self.phone_number)  # type: ignore

    def get_development_level(self):  # type: ignore
        return round((100 / self.work_group.tasksp.count()) * (self.doned_tasks.count()))

    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')



class Uchat(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.sender)
