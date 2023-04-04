from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class star(models.Model):
    stname = models.CharField(max_length=250)
    stimg = models.ImageField(upload_to='pics')
    stdesc = models.TextField()

    def __str__(self):
        return self.stname
