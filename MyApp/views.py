from django.shortcuts import render, get_object_or_404
from .models import Item

def home(request):
    """Обработчик главной страницы"""
    return render(request, 'home.html')

def about(request):
    """Обработчик страницы о себе"""
    return render(request, 'about.html')

def item_detail(request, item_id):
    """Обработчик страниц товаров"""
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item.html', {'item': item})

def item_list(request):
    """Список всех товаров"""
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})
