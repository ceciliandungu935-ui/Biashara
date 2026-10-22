
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
     path('index/', views.index, name = 'inedx'),
      path('error/', views.error, name = 'error'),
       path('blogdetails/', views.blogdetails, name = 'blogdetails'), 
        path('blog/', views.blog, name = 'blog'),
         path('portfoilodetails/', views.portfoliodetails, name  = 'portfoilodetails'),
          path('service/', views.servicedetails, name = 'service'),
           path('starterpage/', views.starterpage, name = 'starterpage'),
            path('admin/', admin.site.urls),
           path('show/', views.show, name = 'show'),






]
