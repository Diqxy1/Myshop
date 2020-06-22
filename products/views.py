from django.shortcuts import render, redirect
from .models import Product, Category

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products, 'categorys':categorys}
    return render(request, 'products/products_list.html', context)


def category_create(request):
    if request.method == 'POST':
        title_data = request.POST['title_category']
        Category.objects.create(title=title_data)
        return redirect('/products/')
    return render(request, 'products/category_create.html')


def product_create(request):
    categorys = Category.objects.all()
    context = {'categorys':categorys}
    if request.method == 'POST':
        title_data = request.POST['title']
        category_data = request.POST['category']
        price_data = request.POST['price']
        Product.objects.create(title=title_data, category=category_data, price=price_data)
        return redirect('/products/')
    return render(request, 'products/product_create.html', context)


def product_update(request):
    product = Product.objects.get(id=request.GET['id'])
    context = {'product':product}
    if request.method == 'POST':
        new_title = request.POST['title']
        new_category = request.POST['category']
        new_price = request.POST['price']
        product.title = new_title
        product.category = new_category
        product.price = new_price
        product.save()
        return redirect('/products/')
    if product:
        return render(request, 'products/product_update.html', context)
    return redirect('/products/')


def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/products/')
