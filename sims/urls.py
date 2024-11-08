from django.urls import path
from . import views

from .views import change_password

urlpatterns = [
    # path('signup/', views.signup, name = "signup"),
    path('addstudents/', views.addstudents, name = "addstudents"),
    path('addstaff/', views.addstaff, name = "addstaff"),
    # path('signin/', views.signin, name = "signin"),
    path('signinsims/', views.signinsims, name = "signinsims"),
	# path('logout/', views.logout, name="logout"),
 
 
    path('news/', views.news, name = "news"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    
    path('caresult/', views.caresult, name = "caresult"),
    path('finalresult/', views.finalresult, name = "finalresult"),
    path('students/', views.students, name = "students"),
    path('staff/', views.staff, name = "staff"),
    path('studentaccount/', views.studentaccount, name = "studentaccount"),
    path('addfinalresult/', views.addfinalresult, name = "addfinalresult"),
    path('payments/', views.payments, name = "payments"),
    path('profile/', views.profile, name = "profile"),
    path('myprofile/', views.myprofile, name = "myprofile"),
    path('base/', views.base, name = "base"),
    
    path('studentcourse/', views.studentcourse, name = "studentcourse"),
    path('addstudentcourse/', views.addstudentcourse, name = "addstudentcourse"),
    path('addstudentcontactinfo/', views.addstudentcontactinfo, name = "addstudentcontactinfo"),
    path('addstaffcontactinfo/', views.addstaffcontactinfo, name = "addstaffcontactinfo"),
    # path('studentaccount/', views.studentaccount, name = "studentaccount"),
    
    path('addcanumber/', views.addcanumber, name = "addcanumber"),
    path('addcaresult/', views.addcaresult, name = "addcaresult"),
    
    path('addexamnumber/', views.addexamnumber, name = "addexamnumber"),
    path('addexamresult/', views.addexamresult, name = "addexamresult"),

    # url for viewing
    path("viewstudentaccount/<int:id>/",views.viewstudentaccount,name = "viewstudentaccount"),
    path("viewstudentinfo/<int:id>/",views.viewstudentinfo,name = "viewstudentinfo"),
    path("viewstaffinfo/<int:id>/",views.viewstaffinfo,name = "viewstaffinfo"),
    
    # url for updating the information
    path('updatestudentcontactinfo/<int:id>/', views.updatestudentcontactinfo, name = "updatestudentcontactinfo"),
    path('updatestaffcontactinfo/<int:id>/', views.updatestaffcontactinfo, name = "updatestaffcontactinfo"),
    path('updatestudentaccount/<int:id>/', views.updatestudentaccount, name = "updatestudentaccount"),
    
    # url for deletting information
    path('deletestudentcontactinfo/<int:id>/', views.deletestudentcontactinfo, name = "deletestudentcontactinfo"),
    path('deletestaffcontactinfo/<int:id>/', views.deletestaffcontactinfo, name = "deletestaffcontactinfo"),
    path('deletestudentaccount/<int:id>/', views.deletestudentaccount, name = "deletestudentaccount"),
    
    path('change-password/', change_password, name='change_password'),
    
    
    # new ##################################################################################
    path("computerfirst/",views.computerfirst,name = "computerfirst"),
    path("computersecond/",views.computersecond,name = "computersecond"),
    path("computerthird/",views.computerthird,name = "computerthird"),
    path("computerfourth/",views.computerfourth,name = "computerfourth"),
    
    path("electricalfirst/",views.electricalfirst,name = "electricalfirst"),
    path("electricalsecond/",views.electricalsecond,name = "electricalsecond"),
    path("electricalthird/",views.electricalthird,name = "electricalthird"),
    path("electricalfourth/",views.electricalfourth,name = "electricalfourth"),
    
    path("mechanicalfirst/",views.mechanicalfirst,name = "mechanicalfirst"),
    path("mechanicalsecond/",views.mechanicalsecond,name = "mechanicalsecond"),
    path("mechanicalthird/",views.mechanicalthird,name = "mechanicalthird"),
    path("mechanicalfourth/",views.mechanicalfourth,name = "mechanicalfourth"),
    
    # for ca result for staff
    path("computercafirst/",views.computercafirst,name = "computercafirst"),
    path("computercasecond/",views.computercasecond,name = "computercasecond"),
    path("computercathird/",views.computercathird,name = "computercathird"),
    path("computercafourth/",views.computercafourth,name = "computercafourth"),
    
    path("electricalcafirst/",views.electricalcafirst,name = "electricalcafirst"),
    path("electricalcasecond/",views.electricalcasecond,name = "electricalcasecond"),
    path("electricalcathird/",views.electricalcathird,name = "electricalcathird"),
    path("electricalcafourth/",views.electricalcafourth,name = "electricalcafourth"),
    
    path("mechanicalcafirst/",views.mechanicalcafirst,name = "mechanicalcafirst"),
    path("mechanicalcasecond/",views.mechanicalcasecond,name = "mechanicalcasecond"),
    path("mechanicalcathird/",views.mechanicalcathird,name = "mechanicalcathird"),
    path("mechanicalcafourth/",views.mechanicalcafourth,name = "mechanicalcafourth"),
    
    # for exam result for staff
    path("computerexamfirst/",views.computerexamfirst,name = "computerexamfirst"),
    path("computerexamsecond/",views.computerexamsecond,name = "computerexamsecond"),
    path("computerexamthird/",views.computerexamthird,name = "computerexamthird"),
    path("computerexamfourth/",views.computerexamfourth,name = "computerexamfourth"),
    
    path("electricalexamfirst/",views.electricalexamfirst,name = "electricalexamfirst"),
    path("electricalexamsecond/",views.electricalexamsecond,name = "electricalexamsecond"),
    path("electricalexamthird/",views.electricalexamthird,name = "electricalexamthird"),
    path("electricalexamfourth/",views.electricalexamfourth,name = "electricalexamfourth"),
    
    path("mechanicalexamfirst/",views.mechanicalexamfirst,name = "mechanicalexamfirst"),
    path("mechanicalexamsecond/",views.mechanicalexamsecond,name = "mechanicalexamsecond"),
    path("mechanicalexamthird/",views.mechanicalexamthird,name = "mechanicalexamthird"),
    path("mechanicalexamfourth/",views.mechanicalexamfourth,name = "mechanicalexamfourth"),
    
    # ca and exam result for student
    path("studentcaresult/",views.studentcaresult,name = "studentcaresult"),
    path("studentexamresult/",views.studentexamresult,name = "studentexamresult"),
    
    path("event/",views.event,name = "event"),

]
