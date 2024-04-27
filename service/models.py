from typing import Any
from django.db import models
from django.contrib.auth.models import User
class interest(models.Model):
    checking=models.BooleanField(default=False)
    science=models.BooleanField(default=False)
    technology=models.BooleanField(default=False)
    sports=models.BooleanField(default=False)
    finance=models.BooleanField(default=False)
    education=models.BooleanField(default=False)
    entertainment=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


