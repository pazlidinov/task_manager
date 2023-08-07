from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Direction, Group, Task

# Create your models here.


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    is_moderator = models.BooleanField(default=False, blank=True, null=True)
    points = models.PositiveIntegerField(default=0, blank=True, null=True)
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    telegram_link = models.URLField()
    img = models.ImageField(upload_to='user_images/',
                            default='default.jpg',
                            blank=True, null=True)

    group = models.ForeignKey(
        Group, on_delete=models.PROTECT,
        blank=True, null=True, related_name='group_members')
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE,
        related_name='user_direction',
        blank=True, null=True)    

    def get_robo_coints(self):
        return int(self.points) / 10  # type: ignore

    def get_phone_number(self):
        return int(self.phone_number)  # type: ignore

    def get_development_level(self):  # type: ignore
        return round((100 / self.work_group.tasksp.count()) * (self.doned_tasks.count()))

    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')


class Project(models.Model):
    project_name = models.CharField(max_length=250)
    project_link = models.URLField()
    poster = models.ImageField(
        upload_to='images/project_posters/', blank=True, null=True)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_projects')

    def __str__(self):
        return str(self.project_name)
    
    
class Chat(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.PROTECT,
        blank=True, null=True)
    added = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return str(self.sender)

