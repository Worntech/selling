from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User

from django.utils.text import slugify

import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        if not first_name:
            raise ValueError("Your First Name is required")
        if not last_name:
            raise ValueError("Your Last Name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, first_name, last_name, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

     

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# end user table -------------
# Create your models here.
class Contact(models.Model):
    Full_Name = models.CharField(max_length=100, null=True)
    Subject = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=200, null=True)
    Phone = models.CharField(max_length=100, null=True)
    Message = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


# for the courses to be uploaded
class Website(models.Model):
    courses = (
            ('Frontend', 'Frontend'),
			('Backend', 'Backend'),
			('Fullstack', 'Fullstack'),
			)
    part = (
            ('html and css', 'html and css'),
			('javascript', 'javascript'),
			('React js', 'React js'),
            ('Vue js', 'Vue js'),
			('Bootstrap', 'Bootstrap'),
			('Angular js', 'Angular js'),
            ('Django', 'Django'),
			('Flask', 'Flask'),
			('Php', 'Php'),
            ('Laravel', 'Laravel'),
			('Rub', 'Rub'),
			('Django, html and css', 'Django, html and css'),
            ('Flask, html and css', 'Flask, html and css'),
			('Django and react js', 'Django and react js'),
			('Php, html and css', 'Php, html and css'),
            ('Php and react js', 'Php and react js'),
			('Laravel, html and css', 'Laravel, html and css'),
			)
    Title = models.CharField(max_length=700)
    Course = models.CharField(max_length=200, null=True, choices=courses)
    Part = models.CharField(max_length=200, null=True, choices=part)
    Explanation = models.CharField(max_length=500)
    Image =models.ImageField(upload_to="home/")
    Video = models.FileField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Commentwebsite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Website', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
# for the product to be uploaded
class Product(models.Model):
    product_type = (
            ('Phone', 'Phone'),
			('Arduino', 'Arduino'),
			('Computer', 'Computer'),
            ('Laptop', 'Laptop'),
			('Watch', 'Watch'),
			('Camera', 'Camera'),
            ('Drone', 'Drone'),
			('Chargers', 'Chargers'),
			('Microphones', 'Microphones'),
            ('Batteries', 'Batteries'),
			('Cable and Adapters', 'Cable and Adapters'),
			('Television', 'Television'),
			)
    Product_Name = models.CharField(max_length=700)
    Product_Type = models.CharField(max_length=200, null=True, choices=product_type)
    Product_Description = models.CharField(max_length=500)
    Specification = models.CharField(max_length=1000)
    Details = models.CharField(max_length=1000)
    Features = models.CharField(max_length=1000)
    Selling_Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Actual_Cost = models.DecimalField(max_digits=10, decimal_places=2)
    Image1 =models.ImageField(upload_to="home/")
    Image2 =models.ImageField(upload_to="home/")
    Image3 =models.ImageField(upload_to="home/")
    Image4 =models.ImageField(upload_to="home/")
    Image5 =models.ImageField(upload_to="home/")
    # Video = models.FileField(upload_to="home/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    # product_id = models.CharField(max_length=20, editable=False, unique=True)  # Add unique=True to ensure uniqueness
    
    # def save(self, *args, **kwargs):
    #     if not self.product_id:
    #         # Generate a unique product_id based on the Title
    #         self.product_id = slugify(self.Product_Name)[:20]  # Limit to first 20 characters to fit max_length
    #     super().save(*args, **kwargs)
    
class Commentproduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    Title = models.ForeignKey('Product', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.Full_Name
    
#PAYMENT MODELS
class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    
    unique_code = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = str(uuid.uuid4()).replace('-', '')[:12]  # Generate a unique 12-character code
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user} - {self.product} - {self.amount}"

    @staticmethod
    def get_payments_for_user(user):
        return Payment.objects.filter(user=user, payment_status='paid').select_related('product').values(
            'product__Product_Name', 
            'product__Product_Type', 
            'product__Selling_Cost', 
            'product__Image1',
            'amount',
            'quantity',
            'transaction_id',
            'payment_date'
        )
    
