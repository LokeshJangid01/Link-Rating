from django.shortcuts import render
from link.models import Link

# Create your views here.
def index(request):
    links = Link.objects.all()

    return render(request, 'core/index.html',{
        'links':links
    })

