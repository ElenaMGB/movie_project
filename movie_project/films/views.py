from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    else:
        form = CommentForm()
    return render(request, 'films/add_comment.html', {'form': form})


def comments_list(request):
    films = Comment.objects.all()
    return render(request, 'films/comments_list.html', {'comment': comment})


from django.shortcuts import render

# Create your views here.
