from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    coffee_bar = models.BooleanField(default=False)
    coffee_station = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    kst_number = models.IntegerField(max_length=30)
    description = models.TextField(max_length=300, null=True, blank=True)
    random_code = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']



