from django.db import models

# Create your models here.


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
    members = models.ManyToManyField(to='account.Profile', blank=True)

    def __str__(self):
        return str(self.name)


class Task(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)    
    link = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='task_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='tasks')
    added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
