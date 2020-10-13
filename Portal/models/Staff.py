from django.db import models

# Create your models here.
class Person(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PasswordHash = models.CharField(max_length=500)
    Jwt = models.CharField(max_length=100)
    CreateDateTime = models.DateTimeField(auto_now_add=True)
    LastUpdateDateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Firstname
    
class Staff(models.Model):
    Staff = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.Staff 