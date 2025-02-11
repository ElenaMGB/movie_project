from django import forms
from .models import Comment, Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['film_title', 'description', 'comment']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['film', 'description', 'comment', 'author']