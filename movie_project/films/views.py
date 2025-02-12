from django.shortcuts import render, redirect
from .models import Film, Comment
from .forms import FilmForm, CommentForm


def comments_list(request):
    comments = Comment.objects.all()
    return render(request, 'films/comments_list.html', {'comments': comments})

def add_comment(request):
    # error = ""
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    else:
            # error = "Данные были заполнены некорректно"
        form = CommentForm()
    return render(request, 'films/add_comment.html', {'form': form})

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'add_film.html', {'form': form})

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})


