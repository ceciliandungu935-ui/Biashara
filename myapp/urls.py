
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
     path('index/', views.index, name = 'index'),
      path('error/', views.error, name = 'error'),
       path('blogdetails/', views.blogdetails, name = 'blogdetails'), 
        path('blog/', views.blog, name = 'blog'),
         path('portfoilodetails/', views.portfoliodetails, name  = 'portfoilodetails'),
          path('service/', views.servicedetails, name = 'service'),
           path('starterpage/', views.starterpage, name = 'starterpage'),
            path('admin/', admin.site.urls),
             path('show/', views.show, name = 'show'),
              path('delete/<int:id>', views.delete),
               path('edit/<int:id>', views.edit),
                path('pay/<int:id>', views.pay),

        #Mpesa Urls
         path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('payment-result/', views.payment_result, name='payment_result'),
    path('transactions/', views.transactions_list, name='transactions'),




]
