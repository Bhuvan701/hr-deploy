"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from create_resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('apply/', views.getInput,name='accept'),
    path('login/', views.loginuser,name='login'),
    path('logout/', views.custom_logout,name='logout'),
    path('view/', views.viewAllPdf,name='viewpdf'),
    path('view/<str:name>',views.viewIndividualPdf,name='viewresume'),
    path('short-listed/>',views.viewshortlisted,name='shortlisted'),
    path('addpost/',views.vacancy,name='vacancy'),
    path('available-jobs/',views.available,name='available'),
    path('hr/',views.hrdelete,name='a'),
    path('rnd/',views.rnd,name='rnd'),
    path('verified/',views.verified,name='verified'),
    path('appointed/',views.appointed,name='appointed'),
    path('rnd/<str:name>',views.viewresearch,name='research'),
    path('research/<str:aadhar>',views.viewresearch2,name='viewresearch'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
