from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from django.contrib.auth.models import User

from inventory import forms
from inventory.models import Item, Help


def index(request):
    items = Item.objects.exclude()
    return render(request, 'inventory/index.html', {
        'items': items,
    })
def users_details(request):
    user = User.objects.exclude()
    return render(request, 'inventory/users_details.html', {
        'user': user,
    })



def item_detail(request):
    try:
        items = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404("this item does not exist")

    return render(request, 'inventory/item_detail.html', {
        'items': items,

    })


def add_item(request):
    form = forms.AddItem()
    if request.method == 'POST':
        form = forms.AddItem(request.POST)
        if form.is_valid():
            item = Item()
            item.title = form.cleaned_data['Item_Name']
            item.serial_number = form.cleaned_data['Serial_Number']
            item.amount = form.cleaned_data['Cost']
            item.description = form.cleaned_data['Item_Description']
            item.save()
            messages.add_message(request, messages.SUCCESS, "Item Added Successful")
            return HttpResponseRedirect(reverse('inventory:landing'))
    return render(request, 'inventory/add_item.html', {'form': form})


def help(request):
    form = forms.help()
    if request.method == 'POST':
        form = forms.help(request.POST)
        if form.is_valid():
            help = Help()
            help.description = form.cleaned_data['Item_Description']
            help.save()
            messages.add_message(request, messages.SUCCESS, "Your problem has been submitted")
            return HttpResponseRedirect(reverse('inventory:landing'))
    return render(request, 'inventory/help.html', {'form': form})
