from django.urls import path
from . import views

from web.views import PaymentView

urlpatterns = [
    path('admin/', views.admin, name = "admin"),
    path('signup/', views.signup, name = "signup"),
    path('signin/', views.signin, name = "signin"),
	path('logout/', views.logout, name="logout"),
 
    path("",views.home,name = "home"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("base/",views.base,name = "base"),
    path("contactus/",views.contactus,name = "contactus"),
    path("contactpost/",views.contactpost,name = "contactpost"),
    path("contactlist/",views.contactlist,name = "contactlist"),
    path("viewcontact/<int:id>/",views.viewcontact,name = "viewcontact"),
    path('deletecontact/<int:id>/', views.deletecontact, name = "deletecontact"),
    path("dashboard/",views.dashboard,name = "dashboard"),
    path("services/",views.services,name = "services"),
    
    # url for success message
    path("signupsucces/",views.signupsucces,name = "signupsucces"),
    path("logedout/",views.logedout,name = "logedout"),
    
    
    path("invoices/",views.invoices,name = "invoices"),
    path("payments/",views.payments,name = "payments"),
    
    
    path("allstaff/",views.allstaff,name = "allstaff"),
    path("courses/",views.courses,name = "courses"),
    
    path("productpost/",views.productpost,name = "productpost"),
    path('viewproduct/<str:pk>/', views.viewproduct.as_view(), name = "viewproduct"),
    path('updateproduct/<int:id>/', views.updateproduct, name = "updateproduct"),
    path('deleteproduct/<int:id>/', views.deleteproduct, name = "deleteproduct"),
    
    path("shop/",views.shop,name = "shop"),
    path("arduino/",views.arduino,name = "arduino"),
    path("batteries/",views.batteries,name = "batteries"),
    path("cableadapter/",views.cableadapter,name = "cableadapter"),
    path("camera/",views.camera,name = "camera"),
    path("computer/",views.computer,name = "computer"),
    path("laptop/",views.laptop,name = "laptop"),
    path("microphone/",views.microphone,name = "microphone"),
    path("phone/",views.phone,name = "phone"),
    path("television/",views.television,name = "television"),
    path("watch/",views.watch,name = "watch"),
    path("drone/",views.drone,name = "drone"),
    path("chargers/",views.chargers,name = "chargers"),
    
    path("myproduct/",views.myproduct,name = "myproduct"),
    path("vieworder/<str:pk>/",views.vieworder,name = "vieworder"),
    #path('vieworder/<str:pk>/', views.vieworder.as_view(), name = "vieworder"),
    
    # FOR PAYMENT
    #path('payment/<int:id>/', PaymentView.as_view(), name='payment'),
    path('payment/<int:product_id>/', views.PaymentView.as_view(), name='payment'),  # Update this line
    path('pesapal/transaction/completed/', views.payment_completed, name='payment_completed'),
]
