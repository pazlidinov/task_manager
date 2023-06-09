from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=250)
    birthday = models.DateField(auto_now_add=True)
    # direction=models.ForeignKey(Direction, on_delete=models.PROTECT, related_name='directions'),
    phone_number=models.PositiveIntegerField(max_length=20)
    