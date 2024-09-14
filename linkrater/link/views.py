from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
from .models import Link,Review
from .forms import LinkForm,ReviewForm
# Create your views here.

def detail(request, pk):
    link = get_object_or_404(Link, pk=pk)

    return render(request, 'link/details.html', {
        'link': link
    })

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)

        if form.is_valid():
            link = form.save()

            return redirect('/')
    else:
        form = LinkForm()

    return render(request,'link/add_link.html',{
        'form':form
    })

@login_required
def add_review(request, pk):
    link = get_object_or_404(Link, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.link = link
            review.user = request.user
            review.save()

            return redirect('link:detail', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'link/add_review.html', {
        'form': form
    })

