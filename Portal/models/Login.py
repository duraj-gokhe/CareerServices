from django.db import models
from Portal.models.Staff import Person

class Login(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    CreateDateTime = models.DateTimeField(auto_now_add=True)
    LastUpdateDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Person