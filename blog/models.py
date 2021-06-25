from django.db import models

# Create your models here.
class Topic(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title