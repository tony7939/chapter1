from django.shortcuts import render
from second.models import Post

def list(request):
    context ={
        'items': Post.objects.all()
    }
    
    return render(request, 'second/list.html', context)
# Create your views here.
