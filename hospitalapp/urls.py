from django.urls import path
from hospitalapp import views

urlpatterns=[

        path('newregistration/', views.newregistration),
        path('login/', views.login),
        path('doctorlist/', views.doctorlist),
        path('view/', views.view),
        path('update/', views.update),
        path('delete/', views.delete),
        path('contact/', views.contact),
        path('rjthospital.com/', views.rjthospital)
]