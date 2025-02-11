from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Comment, Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'review']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['film_title', 'description', 'comment']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['film', 'description', 'comment', 'author']
        widgets = {
            'film': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание фильма'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор отзыва'})
        }