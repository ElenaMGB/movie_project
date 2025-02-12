from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Comment, Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year', 'review']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['film', 'comment', 'author']
        widgets = {
            'film': forms.Select(attrs={'class': 'form-control'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор отзыва'})
        }