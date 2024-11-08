from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from pesapal.views import *
from django.urls import reverse

# FOR PAYMENT
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView

from django_pesapal.views import PaymentRequestMixin

from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Payment, Product
from decimal import Decimal

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'web/admin.html')
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                # messages.info(request, 'Registered succesefull.')
                return redirect('signupsucces')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Loged out succesefull.')
    return redirect('signin')


def home(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/home.html', context)
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('name')
        Subject = request.POST.get('subject')
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        Phone = request.POST.get('phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
# @login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
# @login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
# @login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        messages.info(request, 'Message deleted succesefull.')
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)


# @login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

def services(request):
    return render(request, 'web/services.html')


# views for success message
def signupsucces(request):
    return render(request, 'web/signupsucces.html')
def logedout(request):
    return render(request, 'web/logedout.html')


def invoices(request):
    return render(request, 'web/invoices.html')
def payments(request):
    return render(request, 'web/payments.html')


def allstaff(request):
    return render(request, 'web/allstaff.html')
def courses(request):
    return render(request, 'web/courses.html')

def productpost(request):
    productpost = ProductForm()
    if request.method == "POST":
        productpost = ProductForm(request.POST, files=request.FILES)
        if productpost.is_valid():
            productpost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('productpost')
    context={
        "productpost":productpost
    }
    return render(request, 'web/productpost.html',context)


# class viewproduct(DetailView):
#     model = Product
#     template_name = 'web/viewproduct.html'
#     form = CommentproductForm

#     def post(self, request, *args, **kwargs):
#         form = CommentproductForm(request.POST)
#         if form.is_valid():
#             Title = self.get_object()
#             form.instance.user = request.user
#             form.instance.Title = Title
#             form.save()

#             return redirect(reverse("viewproduct", kwargs={
#                     'pk':Title.pk

#                 }))
#     def get_context_data(self, **kwargs):
#         #kwa ajili ya kudisplay comment huo mstari wa chini
#         post_comments = Commentproduct.objects.all().filter(Title=self.object.id)
        
#         #zinaendelea za kupost comment kwa admin
#         context = super().get_context_data(**kwargs)
#         #context["form"] = self.form
#         context.update({
#                 'form':self.form,
#                 'post_comments':post_comments,
#                 # 'post_comments_count':post_comments_count,
#             })
#         return context

class viewproduct(DetailView):
    model = Product
    template_name = 'web/viewproduct.html'
    comment_form_class = CommentproductForm
    payment_form_class = PaymentForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment_submit' in request.POST:
            comment_form = self.comment_form_class(request.POST)
            if comment_form.is_valid():
                comment_form.instance.user = request.user
                comment_form.instance.Title = self.object
                comment_form.save()
                return redirect(reverse("viewproduct", kwargs={'pk': self.object.pk}))
        elif 'payment_submit' in request.POST:
            payment_form = self.payment_form_class(request.POST)
            if payment_form.is_valid():
                quantity = payment_form.cleaned_data['quantity']
                amount = self.object.Selling_Cost * quantity
                payment = Payment.objects.create(
                    user=request.user,
                    product=self.object,
                    name=self.object.Product_Name,
                    quantity=quantity,
                    amount=amount,
                    payment_status='pending'
                )
                
                # Store necessary data in the session
                request.session['unique_code'] = str(payment.unique_code)
                # request.session['product_id'] = self.object.id
                request.session['amount'] = f"{amount:.2f}"
                request.session['product_name'] = slugify(self.object.Product_Name)
                
                # Redirect to the payment URL with required parameters
                return redirect(reverse('payment', kwargs={
                    # 'unique_code': str(payment.unique_code),
                    'product_id': self.object.id,
                    # 'amount': f"{amount:.2f}",  # Ensure amount is a string
                    # 'product_name': slugify(self.object.Product_Name)  # Slugify product name
                }))
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        post_comments = Commentproduct.objects.filter(Title=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'comment_form': self.comment_form_class(),
            'payment_form': self.payment_form_class(),
            'post_comments': post_comments,
        })
        return context

def shop(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/shop.html', context)

def arduino(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/arduino.html', context)

def batteries(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/batteries.html', context)

def cableadapter(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/cableadapter.html', context)

def camera(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/camera.html', context)

def computer(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/computer.html', context)

def drone(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/drone.html', context)

def laptop(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/laptop.html', context)

def microphone(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/microphone.html', context)

def phone(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/phone.html', context)

def television(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/television.html', context)

def watch(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/watch.html', context)

def chargers(request):
    product = Product.objects.all()
    context={
        "product":product
    }
    return render(request, 'web/chargers.html', context)


# def myproduct(request):
#     product = Product.objects.all()
#     context={
#         "product":product
#     }
#     return render(request, 'web/myproduct.html', context)

def myproduct(request):
    user = request.user
    payments = Payment.get_payments_for_user(user)
    context = {
        'payments': payments
    }
    return render(request, 'web/myproduct.html', context)

# def vieworder(request):
#     user = request.user
#     payments = Payment.get_payments_for_user(user)
#     context = {
#         'payments': payments
#     }
#     return render(request, 'payments/vieworder.html', context)

def vieworder(request, pk):
    # Get the specific payment for the logged-in user
    payment = get_object_or_404(Payment, pk=pk, user=request.user)
    
    # Include related product details using select_related
    product = payment.product

    # Build the context data for the template
    context = {
        'payment': payment,
        'product': product
    }
    return render(request, 'web/vieworder.html', context)

def updateproduct(request, id):
    c = Product.objects.get(id=id)
    product = ProductForm(instance=c)
    if request.method == "POST":
        product = ProductForm(request.POST, files=request.FILES, instance=c)
        if product.is_valid():
            product.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('home')
    context = {"product":product}
    return render(request, 'web/updateproduct.html', context)
    
def deleteproduct(request, id):
    productdelete = Product.objects.get(id=id)
    if request.method == "POST":
        productdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('desktopapp')
    
    context = {"productdelete":productdelete}
    return render(request, 'web/deleteproduct.html', context)


# FOR PAYMENT
class PaymentView(LoginRequiredMixin, View, PaymentRequestMixin):
    """
    Make payment view 
    """
    
    template_name = "web/payment.html"
    
    def get(self, request, product_id):
        unique_code = request.session.get('unique_code')
        product_name = request.session.get('product_name')
        #amount = request.session.get('amount')
        amount = Decimal(request.session.get('amount', '0.00'))
        
        context = {
            'product_id': product_id,
        }

        # Store the unique_code in the session
        request.session['unique_code'] = unique_code
        request.session['product_id'] = product_id

        # Generate payment order info
        order_info = {
            "amount": amount,
            "description": f"Payment for {product_name}",
            "reference": product_id,  # Use payment ID as reference
            "email": request.user.email,  # Use user's email for payment
        }

        # Generate the Pesapal payment URL
        pesapal_url = self.get_payment_url(**order_info)

        # Render the payment page template with Pesapal URL
        return render(request, self.template_name, {'pesapal_url': pesapal_url})
          
def payment_completed(request):
    # Assuming the transaction ID is passed as a GET parameter
    transaction_id = request.GET.get('pesapal_transaction_tracking_id')
    payment = Payment.objects.filter(user=request.user).last()
    unique_code = request.session.get('unique_code')
    product_id = request.session.get('product_id')
    
    if payment:
        product_id = payment.product_id
        payment = get_object_or_404(Payment, product_id=product_id, unique_code=unique_code,  user=request.user)

        # Update the payment status to 'paid'
        payment.payment_status = 'paid'
        payment.transaction_id = transaction_id
        payment.save()

        return redirect(reverse('viewproduct', args=[product_id]))
    else:
        # Handle the case where transaction_id is not found
        # For demonstration, using the latest payment for the user
        payment = Payment.objects.filter(user=request.user).last()
        if payment:
            product_id = payment.product_id
            return redirect(reverse('viewproduct', args=[product_id]))
        else:
            # Handle the case where no payments are found for the user
            return redirect('shop')  # Or any other appropriate view