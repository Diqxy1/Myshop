from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

# Create your views here.
def category_list(request):
    categorys = Category.objects.all()
    context = {'categorys':categorys}
    return render(request, 'categorys/category_list.html', context)


def category_create(request):
    form = CategoryForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('category_list'))
    return render(request, 'categorys/category_create.html', context)
