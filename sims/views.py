from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

from web.views import *

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.db.models import Sum
from django.shortcuts import get_list_or_404

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'sims/admin.html')
@login_required(login_url='signinsims')
def addstudents(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstudents')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstudents')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, first_name="Student", password=password)
                user.save()
                # messages.info(request, 'Registered Student Succesefull.')
                return redirect('addstudentcontactinfo')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstudents')

    else:
        return render(request, 'sims/addstudents.html')
    
@login_required(login_url='signinsims')
def addstaff(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        # id = request.POST.get('id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyStaff.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('addstaff')
            elif MyStaff.objects.filter(username=username).exists():
                messages.info(request, f"Id Number {username} Already Taken")
                return redirect('addstaff')
            else:
                user = MyStaff.objects.create_user(username=username, email=email, first_name="Staff", password=password)
                user.save()
                messages.info(request, 'Registered Staff Succesefull.')
                return redirect('addstaffcontactinfo')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('addstaff')

    else:
        return render(request, 'sims/addstaff.html')


def signinsims(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('news')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signinsims')

    else:
        return render(request, 'sims/signinsims.html')

# @login_required(login_url='signinsims')
# def logout(request):
#     auth.logout(request)
#     messages.info(request, 'Loged out succesefull.')
#     return redirect('signinsims')

@login_required(login_url='signinsims')
def news(request):
    events = Event.objects.all()
    context={
        "events":events,
    }
    return render(request, 'sims/news.html', context)

@login_required(login_url='signinsims')
def dashboard(request):
    return render(request, 'sims/dashboard.html')

@login_required(login_url='signinsims')
def caresult(request):
    # Fetching CaResult objects related to the logged-in user
    logged_in_user = request.user  # Assuming request.user is the logged-in user
    user_ca_results = CaResult.objects.filter(Ca_Number__user=logged_in_user)

    context = {'user_ca_results': user_ca_results}
    return render(request, 'sims/caresult.html', context)

# def base(request):
#     # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
#     logged_in_user = MyStaff.objects.get(username=request.user.username)

#     # Fetching CA results related to the logged-in user using the obtained 'logged_in_user' instance
#     profilename = StudentContactinfo.objects.filter(Ca_Number__user=logged_in_user)
    
#     context={
#         "profilename":profilename,
#         # "countstaff":countstaff
#     }
#     return render(request, 'sims/base.html', context)

@login_required(login_url='signinsims')
def base(request):
    # Assuming 'username' is the attribute in MyStaff that corresponds to the user's username
    logged_in_user = MyStaff.objects.get(username=request.user.username)

    # Fetching related StudentContactinfo for the logged-in user
    student_contact_info = StudentContactinfo.objects.filter(user=logged_in_user).first()

    if student_contact_info:
        # Accessing first name and last name from StudentContactinfo
        first_name = student_contact_info.First_Name
        last_name = student_contact_info.Last_Name

        return render(request, 'sims/base.html', {'first_name': first_name, 'last_name': last_name})
    else:
        # Handle scenario where there's no related StudentContactinfo
        return render(request, 'sims/base.html')  

@login_required(login_url='signinsims')
def finalresult(request):
    # Fetching CaResult objects related to the logged-in user
    logged_in_user = request.user  # Assuming request.user is the logged-in user
    user_final_results = FinalResult.objects.filter(Exam_Number__user=logged_in_user)

    context = {'user_final_results': user_final_results}
    return render(request, 'sims/finalresult.html', context)


@login_required(login_url='signinsims')
def students(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/students.html', context)

@login_required(login_url='signinsims')
def studentaccount(request):
    studentaccount = MyStaff.objects.all()
    # countstaff= MyStaff.objects.all().count()
    context={
        "studentaccount":studentaccount,
        # "countstaff":countstaff
    }
    return render(request, 'sims/studentaccount.html', context)

@login_required(login_url='signinsims')
def staff(request):
    stafflist = StaffContactinfo.objects.all()
    # countstaff= MyStaff.objects.all().count()
    context={
        "stafflist":stafflist,
        # "countstaff":countstaff
    }
    return render(request, 'sims/staff.html', context)

@login_required(login_url='signinsims')
def addcaresult(request):
    return render(request, 'sims/addcaresult.html')

@login_required(login_url='signinsims')
def addfinalresult(request):
    return render(request, 'sims/addfinalresult.html')

@login_required(login_url='signinsims')
def news(request):
    return render(request, 'sims/news.html')

@login_required(login_url='signinsims')
def payments(request):
    return render(request, 'sims/payments.html')

@login_required(login_url='signinsims')
def profile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        studentcontactinfo= StudentContactinfo.objects.filter(user=user_instance)
        studentcourse = StudentCourse.objects.filter(user=user_instance)

        context={
            "studentcourse":studentcourse,
            "studentcontactinfo":studentcontactinfo,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/profile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found

@login_required(login_url='signinsims')
def myprofile(request):
    current_user = request.user
    
    try:
        user_instance = get_object_or_404(MyStaff, username=current_user.username)
        staffcontactinfo= StaffContactinfo.objects.filter(user=user_instance)

        context={
            "staffcontactinfo":staffcontactinfo,
            "user_instance":user_instance,
            "current_user":current_user
        }
        return render(request, 'sims/myprofile.html', context)

    except MyStaff.DoesNotExist:
        raise Http404("User does not exist")  # Handle case where user is not found


@login_required(login_url='signinsims')
def studentcourse(request):
    return render(request, 'sims/studentcourse.html')

@login_required(login_url='signinsims')
def addstudentcourse(request):
    studentcourse = StudentCourseForm()
    if request.method == "POST":
        studentcourse = StudentCourseForm(request.POST, files=request.FILES)
        if studentcourse.is_valid():
            studentcourse.save()
            messages.info(request, 'Student Registered succesefull.')
            return redirect('addstudents')

    context={
        "studentcourse":studentcourse
    }
    return render(request, 'sims/addstudentcourse.html', context)

@login_required(login_url='signinsims')
def addstudentcontactinfo(request):
    studentcontactinfo = StudentContactinfoForm()
    if request.method == "POST":
        studentcontactinfo = StudentContactinfoForm(request.POST, files=request.FILES)
        if studentcontactinfo.is_valid():
            studentcontactinfo.save()
            messages.info(request, 'Student Registered Succesefull.')
            return redirect('addstudents')

    context={
        "studentcontactinfo":studentcontactinfo
    }
    return render(request, 'sims/addstudentcontactinfo.html', context)

@login_required(login_url='signinsims')
def addstaffcontactinfo(request):
    staffcontactinfo = StaffContactinfoForm()
    if request.method == "POST":
        staffcontactinfo = StaffContactinfoForm(request.POST, files=request.FILES)
        if staffcontactinfo.is_valid():
            staffcontactinfo.save()
            messages.info(request, 'Student Registered Succesefull.')
            return redirect('addstudents')

    context={
        "staffcontactinfo":staffcontactinfo
    }
    return render(request, 'sims/addstaffcontactinfo.html', context)

# views for viewing
@login_required(login_url='signinsims')
def viewstudentaccount(request, id):
    studentaccountview = MyStaff.objects.get(id=id)
    
    context = {"studentaccountview":studentaccountview}
    return render(request, 'sims/viewstudentaccount.html', context)

@login_required(login_url='signinsims')
def viewstudentinfo(request, id):
    studentinfoview = StudentContactinfo.objects.get(id=id)
    
    context = {"studentinfoview":studentinfoview}
    return render(request, 'sims/viewstudentinfo.html', context)

@login_required(login_url='signinsims')
def viewstaffinfo(request, id):
    staffinfoview = StaffContactinfo.objects.get(id=id)
    
    context = {"staffinfoview":staffinfoview}
    return render(request, 'sims/viewstaffinfo.html', context)

# view for updating the information
@login_required(login_url='signinsims')
def updatestudentcontactinfo(request, id):
    a = StudentContactinfo.objects.get(id=id)
    studentinfo =StudentContactinfoForm(instance=a)
    if request.method == "POST":
        studentinfo = StudentContactinfoForm(request.POST, files=request.FILES, instance=a)
        if studentinfo.is_valid():
            studentinfo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('students')
    context = {"studentinfo":studentinfo}
    return render(request, 'sims/updatestudentcontactinfo.html', context)

@login_required(login_url='signinsims')
def updatestaffcontactinfo(request, id):
    b = StaffContactinfo.objects.get(id=id)
    staffinfo =StaffContactinfoForm(instance=b)
    if request.method == "POST":
        staffinfo = StaffContactinfoForm(request.POST, files=request.FILES, instance=b)
        if staffinfo.is_valid():
            staffinfo.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('staff')
    context = {"staffinfo":staffinfo}
    return render(request, 'sims/updatestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def updatestudentaccount(request, id):
    c = MyStaff.objects.get(id=id)
    studentaccount =MyStaffForm(instance=c)
    if request.method == "POST":
        studentaccount = MyStaffForm(request.POST, files=request.FILES, instance=c)
    if studentaccount.is_valid():
        cleaned_data = studentaccount.cleaned_data
        # Check if the new username is different from the existing one
        if 'username' in cleaned_data and cleaned_data['username'] != c.username:
            # If it's different, update the instance and save
            c.username = cleaned_data['username']
            c.save()
            messages.info(request, 'Updated successfully.')
            return redirect('students')
        else:
            # Username remains unchanged, proceed without modifying
            messages.info(request, 'No changes made.')
            return redirect('students')
    context = {"studentaccount":studentaccount}
    return render(request, 'sims/updatestudentaccount.html', context)

# view for deleting information
@login_required(login_url='signinsims')
def deletestudentcontactinfo(request, id):
    studentcontactinfodelete = StudentContactinfo.objects.get(id=id)
    if request.method == "POST":
        studentcontactinfodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('students')
    
    context = {"studentcontactinfodelete":studentcontactinfodelete}
    return render(request, 'sims/deletestudentcontactinfo.html', context)

@login_required(login_url='signinsims')
def deletestaffcontactinfo(request, id):
    staffcontactinfodelete = StaffContactinfo.objects.get(id=id)
    if request.method == "POST":
        staffcontactinfodelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('staff')
    
    context = {"staffcontactinfodelete":staffcontactinfodelete}
    return render(request, 'sims/deletestaffcontactinfo.html', context)

@login_required(login_url='signinsims')
def deletestudentaccount(request, id):
    studentaccountdelete = MyStaff.objects.get(id=id)
    if request.method == "POST":
        studentaccountdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('studentaccount')
    
    context = {"studentaccountdelete":studentaccountdelete}
    return render(request, 'sims/deletestudentaccount.html', context)

# for ca number ca result examnumber and examresult
# add ca number
@login_required(login_url='signinsims')
def addcanumber(request):
    canumber = CaNumberForm()
    if request.method == "POST":
        canumber = CaNumberForm(request.POST, files=request.FILES)
        if canumber.is_valid():
            canumber.save()
            messages.info(request, 'Ca Number Added Succesefull.')
            return redirect('addcanumber')

    context={
        "canumber":canumber
    }
    return render(request, 'sims/addcanumber.html', context)

@login_required(login_url='signinsims')
def addexamnumber(request):
    examnumber = ExamNumberForm()
    if request.method == "POST":
        examnumber = ExamNumberForm(request.POST, files=request.FILES)
        if examnumber.is_valid():
            examnumber.save()
            messages.info(request, 'Ca Number Added Succesefull.')
            return redirect('addexamnumber')

    context={
        "examnumber":examnumber
    }
    return render(request, 'sims/addexamnumber.html', context)

# add ca result
@login_required(login_url='signinsims')
def addcaresult(request):
    caresult = CaResultForm()
    if request.method == "POST":
        caresult = CaResultForm(request.POST, files=request.FILES)
        if caresult.is_valid():
            caresult.save()
            messages.info(request, 'Ca Result Added Succesefull.')
            return redirect('addcaresult')

    context={
        "caresult":caresult
    }
    return render(request, 'sims/addcaresult.html', context)

@login_required(login_url='signinsims')
def addexamresult(request):
    examresult = FinalResultForm()
    if request.method == "POST":
        examresult = FinalResultForm(request.POST, files=request.FILES)
        if examresult.is_valid():
            examresult.save()
            messages.info(request, 'Result Result Added Succesefull.')
            return redirect('addexamresult')

    context={
        "examresult":examresult
    }
    return render(request, 'sims/addexamresult.html', context)

# for displaying ca result for single user who is loged in
@login_required(login_url='signinsims')
def display_ca_results(request):
    logged_in_user = request.user

    try:
        ca_number = CaNumber.objects.get(user=logged_in_user)
        ca_results = CaResult.objects.filter(Ca_Number=ca_number)
    except CaNumber.DoesNotExist:
        ca_number = None
        ca_results = None
        # Handle cases where CaNumber doesn't exist for the user

    return render(request, 'ca_results.html', {'ca_results': ca_results})


@login_required(login_url='signinsims')
def change_password(request):
    if request.method == 'POST':
        passwordchange = PasswordChangeForm(request.user, request.POST)
        if passwordchange.is_valid():
            user = passwordchange.save()
            # This is to keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('signinsims')  # Redirect to the same page after successful password change
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        passwordchange = PasswordChangeForm(request.user)
    return render(request, 'sims/change_password.html', {'passwordchange': passwordchange})




# views for list of students
@login_required(login_url='signinsims')
def computerfirst(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/computerfirst.html', context)

@login_required(login_url='signinsims')
def computersecond(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/computersecond.html', context)

@login_required(login_url='signinsims')
def computerthird(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/computerthird.html', context)

@login_required(login_url='signinsims')
def computerfourth(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/computerfourth.html', context)

@login_required(login_url='signinsims')
def electricalfirst(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/electricalfirst.html', context)

@login_required(login_url='signinsims')
def electricalsecond(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/electricalsecond.html', context)

@login_required(login_url='signinsims')
def electricalthird(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/electricalthird.html', context)

@login_required(login_url='signinsims')
def electricalfourth(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/electricalfourth.html', context)

@login_required(login_url='signinsims')
def mechanicalfirst(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/mechanicalfirst.html', context)

@login_required(login_url='signinsims')
def mechanicalsecond(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/mechanicalsecond.html', context)

@login_required(login_url='signinsims')
def mechanicalthird(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/mechanicalthird.html', context)

@login_required(login_url='signinsims')
def mechanicalfourth(request):
    student = StudentContactinfo.objects.all()
    context={
        "student":student,
    }
    return render(request, 'sims/mechanicalfourth.html', context)

# views for ca result for staff
@login_required(login_url='signinsims')
def computercafirst(request):
    return render(request, 'sims/computercafirst.html')

@login_required(login_url='signinsims')
def computercasecond(request):
    return render(request, 'sims/computercasecond.html')

@login_required(login_url='signinsims')
def computercathird(request):
    return render(request, 'sims/computercathird.html')

@login_required(login_url='signinsims')
def computercafourth(request):
    return render(request, 'sims/computercafourth.html')

def electricalcafirst(request):
    return render(request, 'sims/electricalcafirst.html')

@login_required(login_url='signinsims')
def electricalcasecond(request):
    return render(request, 'sims/electricalcasecond.html')

@login_required(login_url='signinsims')
def electricalcathird(request):
    return render(request, 'sims/electricalcathird.html')

@login_required(login_url='signinsims')
def electricalcafourth(request):
    return render(request, 'sims/electricalcafourth.html')

@login_required(login_url='signinsims')
def mechanicalcafirst(request):
    return render(request, 'sims/mechanicalcafirst.html')

@login_required(login_url='signinsims')
def mechanicalcasecond(request):
    return render(request, 'sims/mechanicalcasecond.html')

@login_required(login_url='signinsims')
def mechanicalcathird(request):
    return render(request, 'sims/mechanicalcathird.html')

@login_required(login_url='signinsims')
def mechanicalcafourth(request):
    return render(request, 'sims/mechanicalcafourth.html')

# views for exam result for staff
@login_required(login_url='signinsims')
def computerexamfirst(request):
    return render(request, 'sims/computerexamfirst.html')

@login_required(login_url='signinsims')
def computerexamsecond(request):
    return render(request, 'sims/computerexamsecond.html')

@login_required(login_url='signinsims')
def computerexamthird(request):
    return render(request, 'sims/computerexamthird.html')

@login_required(login_url='signinsims')
def computerexamfourth(request):
    return render(request, 'sims/computerexamfourth.html')


@login_required(login_url='signinsims')
def electricalexamfirst(request):
    return render(request, 'sims/electricalexamfirst.html')

@login_required(login_url='signinsims')
def electricalexamsecond(request):
    return render(request, 'sims/electricalexamsecond.html')

@login_required(login_url='signinsims')
def electricalexamthird(request):
    return render(request, 'sims/electricalexamthird.html')

@login_required(login_url='signinsims')
def electricalexamfourth(request):
    return render(request, 'sims/electricalexamfourth.html')


@login_required(login_url='signinsims')
def mechanicalexamfirst(request):
    return render(request, 'sims/mechanicalexamfirst.html')

@login_required(login_url='signinsims')
def mechanicalexamsecond(request):
    return render(request, 'sims/mechanicalexamsecond.html')

@login_required(login_url='signinsims')
def mechanicalexamthird(request):
    return render(request, 'sims/mechanicalexamthird.html')

@login_required(login_url='signinsims')
def mechanicalexamfourth(request):
    return render(request, 'sims/mechanicalexamfourth.html')


# ca and exam result for students
@login_required(login_url='signinsims')
def studentcaresult(request):
    return render(request, 'sims/studentcaresult.html')

@login_required(login_url='signinsims')
def studentexamresult(request):
    return render(request, 'sims/studentexamresult.html')

@login_required(login_url='signinsims')
def event(request):
    addevent = EventForm()
    if request.method == "POST":
        addevent = EventForm(request.POST, files=request.FILES)
        if addevent.is_valid():
            addevent.save()
            messages.info(request, 'Event Added Succesefull.')
            return redirect('event')

    context={
        "addevent":addevent
    }
    return render(request, 'sims/event.html', context)
