from django.urls import path
from studentformapp import views

urlpatterns=[

    path('registerform/', views.registerform),
    path('loginnew/', views.loginnew)
]