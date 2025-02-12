from django.db import models

class Film(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    year = models.CharField('Год выпуска',max_length=4)
    review = models.TextField('Краткое описание фильма', max_length=200)

    def __str__(self):
        return f'{self.title} ({self.review})'

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    description = models.TextField('Краткое описание фильма', max_length=200, blank=True)
    comment = models.TextField('Отзыв о фильме', max_length=200)
    author = models.CharField('Автор отзыва', max_length=100)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.film.review
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Comment by {self.author} on {self.description}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
