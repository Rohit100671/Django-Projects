from django.urls import path
from calciapp import views

urlpatterns=[

    path('result/',views.result),
    path('giveMeResult/',views.giveMeResult) 
]