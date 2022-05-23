from django.db import models

# Create your models here.

#This is my class djangoClasses
class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    course_number = models.IntegerField()
    instructor_name = models.CharField(max_length=50)
    duration = models.FloatField()
    #This is the object manager
    djangoClasses = models.Manager()
    #This makes the instances of the class have the title appear on the django admin page
    def __str__(self):
        return self.title

    #I used the shell to create the class objects
