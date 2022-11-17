from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import InventoryItems
from .forms import AddItems
from django.contrib.auth.decorators import login_required

@login_required
def ItemListView(request):
    obj = InventoryItems.objects.all().first()
    qs = InventoryItems.objects.all()
    
    context = {
        'obj': obj,
        'qs': qs,
    }
    
    return render(request, 'inventory/list.html', context=context)

@login_required
def ItemDetailView(request, slug=None):
    obj = get_object_or_404(InventoryItems, slug=slug)
    
    context = {
        'obj': obj
    }
    
    return render(request, 'inventory/detail.html', context=context)

@login_required
def ItemCreateView(request):
    form = AddItems(request.POST or None, request.FILES or None)
    # image = request.files["thumbnail"]
    
    if form.is_valid():
        form.save()
        return redirect(reverse('inventory:list'))
    
    context = {
        'form': form,
    }
    
    return render(request, 'inventory/create.html', context=context)

@login_required
def ItemUpdateView(request, slug=None):
    obj = get_object_or_404(InventoryItems, slug=slug)
    form = AddItems(request.POST or None, request.FILES or None, instance=obj)
    context = {
        "form": form,
        "obj": obj,
    }
    if form.is_valid():
        form.save()
        return redirect(reverse('inventory:detail', kwargs={'slug': obj.slug}))
    return render(request, 'inventory/update.html', context)

@login_required
def ItemDeleteView(request, slug=None):
    try:
        obj = InventoryItems.objects.get(slug=slug)
    except:
        obj = None
        
    if request.method == "POST":
        obj.delete()
        return redirect(reverse('inventory:list'))
    
    context = {
        "obj": obj
    }
    return render(request, 'inventory/delete.html', context)


