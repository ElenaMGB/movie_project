from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    description = models.TextField()
    comment = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'Comment by {self.author} on {self.film.title}'
