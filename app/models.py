from django.db import models

# Create your models here.
class Voter_model(models.Model):
    gender_choise = [
        ("Male",'Male'),
        ("Female","Female"),
        ('others','others')
    ]
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=gender_choise)
    address = models.TextField()
    Photo = models.ImageField(upload_to='Voter_photos/')
    Voter_id = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name
