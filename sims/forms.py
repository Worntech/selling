from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyStudentsForm(UserCreationForm):
    class Meta:
        model = MyStudents
        fields = ['email', 'username', 'first_name']
        
class MyStaffForm(UserCreationForm):
    class Meta:
        model = MyStaff
        fields = ['email', 'username', 'first_name']

class StudentCourseForm(ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'
        
class StudentContactinfoForm(ModelForm):
    class Meta:
        model = StudentContactinfo
        fields = '__all__'
        
class StaffContactinfoForm(ModelForm):
    class Meta:
        model = StaffContactinfo
        fields = '__all__'
        
class CaNumberForm(ModelForm):
    class Meta:
        model = CaNumber
        fields = '__all__'
        
class ExamNumberForm(ModelForm):
    class Meta:
        model = ExamNumber
        fields = '__all__'
        
class CaResultForm(ModelForm):
    class Meta:
        model = CaResult
        fields = '__all__'
        
class FinalResultForm(ModelForm):
    class Meta:
        model = FinalResult
        fields = '__all__'
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
