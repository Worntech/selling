from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username']


    #for contact 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
     
     #for website
class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
        
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    #for comment of the website
class CommentproductForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentproduct
        fields = ('content',)

# PAYMENT MODEL
# class PaymentForm(ModelForm):
#     class Meta:
#         model = Payment
#         fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['quantity']  # Only include the quantity field
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }
   