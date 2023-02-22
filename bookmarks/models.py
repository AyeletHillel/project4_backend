from django.db import models

################## Create your models here.
# By default all fields are required
class Bookmark(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    img = models.CharField(max_length=400, blank=True, default="https://blog.tapptic.com/wp-content/uploads/2020/02/what-can-AI-generate-today-scaled.jpg")
    