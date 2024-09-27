from django.shortcuts import render, get_object_or_404
from third.models import Restaurant 

from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator

from third.forms import RestaurantForm
from django.http import HttpResponseRedirect

@csrf_exempt
def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)
    
    page = request.GET.get('page')
    items = paginator.get_page(page)
    
    context = {
        'restaurants':items
    }
    
    return render(request, 'third/list.html', context)


@csrf_exempt
def detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    context = {
        'restaurant':restaurant
    }
    
    return render(request, 'third/detail.html', context)

@csrf_exempt
def create(request):
    if request.method=='POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item =form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form':form})


@csrf_exempt
def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    item.delete()
    return HttpResponseRedirect('/third/list/')

@csrf_exempt
def update(request):
    if request.method=='POST' and 'id' in request.POST:
        item =Restaurant.objects.get(pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance = item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        item = Restaurant.objects.get(pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form':form})
    return HttpResponseRedirect('/third/list/')
    