from django.urls import path
from empregapp import views

urlpatterns=[

    path('empregistration/',views.empregistration),
    path('login/',views.login),
    path('view/',views.view),
    path('remove/',views.remove),
    path('update/',views.update),
    path('check/',views.check)
    # path('giveMeEmployee/',views.giveMeEmployee)

]

