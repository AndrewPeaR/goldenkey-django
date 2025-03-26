from django.shortcuts import render
# from .models import Product

def index(request):
    # products = Product.objects.all()
    
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
        'array': [1, 2, 3, 4],
        # 'items': Product.objects.filter(name='server')
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')