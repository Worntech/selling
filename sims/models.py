from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import get_user_model


# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        if not first_name:
            raise ValueError("Your First Name is required")
        # if not last_name:
        #     raise ValueError("Your Last Name is required")
        # if not id:
        #     raise ValueError("Your Middle Name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            # last_name=last_name,
            # middle_name=middle_name,
            # phone=phone,
            # id=id,
            # course=course,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            # first_name=first_name,
            # last_name=last_name,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

     

class MyStudents(AbstractBaseUser):

    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=True, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
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

class MyStaff(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="username", max_length=100, unique=True)
    # id=models.CharField(verbose_name="id", max_length=100, unique=False, primary_key=True)
    # last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
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
    
class StudentCourse(models.Model):
    Course = [
    ("computer engineering", "computer engineering"),
    ("electrical engineering", "electrical engineering"),
    ("mechanical engineering", "mechanical engineering"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
]
    Years = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
]
    collage = [
    ("coste", "coste"),
    ("coict", "coict"),
]
    department = [
    ("computer engineering", "computer engineering"),
    ("computer science", "computer science"),
    ("civil engineering", "civil engineering"),
]
    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    Collage = models.CharField(max_length=40, choices=collage)
    Department = models.CharField(max_length=40, choices=department)
    Level = models.CharField(max_length=40, choices=level)
    course = models.CharField(max_length=40, choices=Course)
    years = models.CharField(max_length=40, choices=Years)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class StudentContactinfo(models.Model):
    region = [
    ("Arusha", "Arusha"),
    ("Dodoma", "Dodoma"),
    ("Mwanza", "Mwanza"),
    ("Iringa", "Iringa"),
    ("Tabora", "Tabora"),
]
    user_type = [
    ("Student", "Student"),
]
    Course = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
]
    Years = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
]
    collage = [
    ("coste", "coste"),
    ("coict", "coict"),
]
    department = [
    ("computer engineering", "computer engineering"),
    ("computer science", "computer science"),
    ("civil engineering", "civil engineering"),
]
    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    User_type = models.CharField(max_length=40, choices=user_type)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Collage = models.CharField(max_length=40, choices=collage)
    Department = models.CharField(max_length=40, choices=department)
    Level = models.CharField(max_length=40, choices=level)
    course = models.CharField(max_length=40, choices=Course)
    years = models.CharField(max_length=40, choices=Years)
    Region = models.CharField(max_length=40, choices=region)
    Phone = models.CharField(max_length=100)
    Profile_Image =models.ImageField(upload_to="home/")
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)

class StaffContactinfo(models.Model):
    region = [
    ("Arusha", "Arusha"),
    ("Dodoma", "Dodoma"),
    ("Mwanza", "Mwanza"),
    ("Iringa", "Iringa"),
    ("Tabora", "Tabora"),
]
    user_type = [
    ("Staff", "Staff"),
]
    professional = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    level = [
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("Bachelor", "Bachelor"),
    ("Master", "Master"),
    ("Phd", "Phd"),
]
    collage = [
    ("coste", "coste"),
    ("coict", "coict"),
]
    department = [
    ("computer engineering", "computer engineering"),
    ("computer science", "computer science"),
    ("civil engineering", "civil engineering"),
]
    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    User_type = models.CharField(max_length=40, choices=user_type)
    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Collage = models.CharField(max_length=40, choices=collage)
    Department = models.CharField(max_length=40, choices=department)
    Level_Of_Education = models.CharField(max_length=40, choices=level)
    course = models.CharField(max_length=40, choices=professional)
    Region = models.CharField(max_length=40, choices=region)
    Phone = models.CharField(max_length=100)
    Form4_Certificate = models.FileField(upload_to="home/")
    Form6_Certificate = models.FileField(upload_to="home/")
    Univercity_Certificate = models.FileField(upload_to="home/")
    Profile_Image =models.ImageField(upload_to="home/")
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class CaNumber(models.Model):
    academic_year = [
    ("2023/2024", "2023/2024"),
    ("2024/2025", "2024/2025"),
    ("2025/2026", "2025/2026"),
    ("2026/2027", "2026/2027"),
    ("2027/2028", "2027/2028"),
    ("2029/2030", "2029/2030"),
]
    semister = [
    ("1", "1"),
    ("2", "2"),
]
    Course = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    Ca_Number = models.CharField(max_length=100, primary_key=True)
    course = models.CharField(max_length=40, choices=Course)
    Academic_Year = models.CharField(max_length=40, choices=academic_year)
    Semister = models.CharField(max_length=40, choices=semister)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class ExamNumber(models.Model):
    academic_year = [
    ("2023/2024", "2023/2024"),
    ("2024/2025", "2024/2025"),
    ("2025/2026", "2025/2026"),
    ("2026/2027", "2026/2027"),
    ("2027/2028", "2027/2028"),
    ("2029/2030", "2029/2030"),
]
    semister = [
    ("1", "1"),
    ("2", "2"),
]
    Course = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    user = models.ForeignKey(MyStaff, on_delete=models.CASCADE)
    Exam_Number = models.CharField(max_length=100, primary_key=True)
    Academic_Year = models.CharField(max_length=40, choices=academic_year)
    course = models.CharField(max_length=40, choices=Course)
    Semister = models.CharField(max_length=40, choices=semister)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class CaResult(models.Model):
    course_code = [
    ("COB2211", "COB2211"),
    ("COB2212", "COB2212"),
]
    course_name = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    academic_year = [
    ("2023/2024", "2023/2024"),
    ("2024/2025", "2024/2025"),
    ("2025/2026", "2025/2026"),
    ("2026/2027", "2026/2027"),
    ("2027/2028", "2027/2028"),
    ("2029/2030", "2029/2030"),
]
    semister = [
    ("1", "1"),
    ("2", "2"),
]
    Ca_Number = models.ForeignKey(CaNumber, on_delete=models.CASCADE)
    Course_Name = models.CharField(max_length=40, choices=course_name)
    Course_Code = models.CharField(max_length=40, choices=course_code)
    Academic_Year = models.CharField(max_length=40, choices=academic_year)
    Semister = models.CharField(max_length=40, choices=semister)
    Assignment = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    Quiz = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    Test_1 = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    Test_2 = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class FinalResult(models.Model):
    course_code = [
    ("COB2211", "COB2211"),
    ("COB2212", "COB2212"),
]
    course_name = [
    ("Computer Engineering", "Computer Engineering"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Mechanical Engineering", "Mechanical Engineering"),
]
    academic_year = [
    ("2023/2024", "2023/2024"),
    ("2024/2025", "2024/2025"),
    ("2025/2026", "2025/2026"),
    ("2026/2027", "2026/2027"),
    ("2027/2028", "2027/2028"),
    ("2029/2030", "2029/2030"),
]
    semister = [
    ("1", "1"),
    ("2", "2"),
]
    Exam_Number = models.ForeignKey(ExamNumber, on_delete=models.CASCADE)
    Course_Name = models.CharField(max_length=40, choices=course_name)
    Course_Code = models.CharField(max_length=40, choices=course_code)
    Academic_Year = models.CharField(max_length=40, choices=academic_year)
    Semister = models.CharField(max_length=40, choices=semister)
    CA_Result = models.IntegerField(blank=True, null=True)
    Result = models.IntegerField(blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
class Event(models.Model):
    Event_Name = models.CharField(max_length=100)
    Event_Place = models.CharField(max_length=100)
    Event_Start = models.CharField(max_length=100)
    Event_End = models.CharField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)