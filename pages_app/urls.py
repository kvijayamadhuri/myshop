from django.urls import path
from .views import about,blog,cart,checkout,contact,index,services,shop,thankyou
 


urlpatterns =[
    path('about/',about),
    path('blog/',blog),
    path('cart/',cart),
    path('checkout/',checkout),
    path('contact/',contact),
    path('',index),
    path('services/',services),
    path('shop/',shop),
    path('thankyou/',thankyou),
     
     
     
]