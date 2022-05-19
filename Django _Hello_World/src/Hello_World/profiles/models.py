from django.db import models

FNAME_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
}
class Profiles(models.Model):
    fname = models.CharField(max_length=50, default="", blank=True, choices=FNAME_CHOICES)
    lname = models.CharField(max_length=50, default="", blank=True, null=False)
    email = models.CharField(max_length=50, default="", blank=True)
    username = models.CharField(max_length=50, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.lname