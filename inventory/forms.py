from __future__ import unicode_literals
from django.db import models
from django import forms


class AddItem(forms.Form):
    Item_Name = forms.CharField()
    Serial_Number = forms.CharField()
    Cost = forms.CharField()
    Item_Description = forms.CharField(widget=forms.Textarea)

class Users(forms.Form):
     name = forms.CharField(max_length=200)
     email_address = forms.EmailField
     position=forms.CharField
     telephone_number = forms.IntegerField()
     department = forms.CharField
     position=forms.CharField



class Help(forms.Form):
    Description = forms.CharField(widget=forms.Textarea)


# for my sign_up
class Sign_up(forms.Form):
    First_Name = forms.CharField()
    Surname = forms.CharField()
    email_address = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()


# for my sign_up
class Login(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()


class DeleteItem(forms.Form):
    model = AddItem
    fields = []
