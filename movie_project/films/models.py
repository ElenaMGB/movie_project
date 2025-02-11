from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4)
    review = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    comment = models.TextField()
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.film.review
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Comment by {self.author} on {self.film.title}'
