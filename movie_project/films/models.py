from django.db import models

class Comment(models.Model):
    film_title = models.CharField(max_length=200)
    description = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.title