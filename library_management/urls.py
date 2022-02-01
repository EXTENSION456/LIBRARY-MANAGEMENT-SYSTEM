"""library_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from readers import views
from staticpages import views as sviews
from home import views as hmviews
from books import views as bkviews
from staff import views as stviews
from administrator import views as adviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/readers.html/',views.signup),
    path('home/',hmviews.home),
    path('home/staff.html/',stviews.staff),
    path('home/admin.html/',adviews.adminin),
    path('home/log.html/',views.login),
    path('home/admin.html/viewcustomer.html/',adviews.viewusers),
    path('home/admin.html/abc.html/',adviews.delusers),
    path('home/admin.html/books.html/',adviews.books),
    path('home/admin.html/editbooks.html/',adviews.editbooks),
    path('home/log.html/editpassword.html',views.useraction),
    path('home/log.html/rqstbook.html',views.rqbook),
    path('home/aboutus.html/',sviews.aboutus),
    path('home/contactus.html/',sviews.contactus),
    path('home/log.html/viewbooks.html',views.viewbooks),

    
   
]
