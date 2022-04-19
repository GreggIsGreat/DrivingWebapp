from django.db import models


# Create your models here.


# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


class Account(models.Model):
    account = models.CharField(max_length=100)
    title = models.ForeignKey(GeeksModel, on_delete=models.CASCADE)


from django.db import models
class Customer(models.Model ):
    GENDER_CHOICES = (('Male','Male'),('Female', 'Female') )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
            return self.gender
