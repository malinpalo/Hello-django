from django.shortcuts import render, redirect, get_object_or_404
from .models import item
from .forms import itemForm

# Create your views here.


def get_todo_list(request):
    Items = item.objects.all()
    context = {
        'Items': Items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = itemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, Item_id):
    Item = get_object_or_404(item, id=Item_id)
    if request.method == 'POST':
        form = itemForm(request.POST, instance=Item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = itemForm(instance=Item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, Item_id):
    Item = get_object_or_404(item, id=Item_id)
    Item.done = not Item.done
    Item.save()
    return redirect('get_todo_list')


def delete_item(request, Item_id):
    Item = get_object_or_404(item, id=Item_id)
    Item.delete()
    return redirect('get_todo_list')
