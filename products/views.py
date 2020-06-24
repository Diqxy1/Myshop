from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product
from categorys.models import Category
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    context = {'products':products, 'categorys':categorys}
    return render(request, 'products/products_list.html', context)


def product_create(request):
    form = ProductForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('product_list'))
    return render(request, 'products/product_create.html', context)


def product_update(request):
    product = Product.objects.get(id=request.GET['id'])
    form = ProductForm(request.POST or None, instance=product)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('product_list'))
    if product:
        return render(request, 'products/product_update.html', context)
    return redirect(reverse_lazy('product_list'))


def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(reverse_lazy('product_list'))
