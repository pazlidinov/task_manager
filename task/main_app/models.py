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
    members = models.ManyToManyField(to='accounts.Profile', blank=True)

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



class CompletedTasks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True, related_name='task')
    task_file = models.FileField()
    author = models.ForeignKey(to='accounts.Profile', on_delete=models.CASCADE, related_name='completed_task')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True, default=0)
    comment = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Completed Tasks'
    
    def __str__(self):
        return str(f'{self.id} {self.author.first_name}') # type: ignore
    
    
class Chat(models.Model):
    sender = models.ForeignKey(to='accounts.Profile', on_delete=models.PROTECT, blank=True, null=True)
    added = models.TimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return str(self.sender)
    

class Project(models.Model):
    author = models.ForeignKey(to='accounts.Profile',
                               on_delete=models.CASCADE,
                               related_name='project_author')
    project_name = models.CharField(max_length=250)
    project_link = models.URLField()
    poster = models.ImageField(upload_to='images/project_posters/', blank=True, null=True)

    def __str__(self):
        return str(self.project_name)