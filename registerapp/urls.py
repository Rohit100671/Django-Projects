from django.urls import path
from registerapp import views

urlpatterns=[

    path('save/',views.save),
    path('login/',views.login),
    path('getallusers/',views.getallusers),
    path('delete/<userfrombrowser>',views.delete),
    path('view/',views.view),
    path('add/',views.add),
    path('remove/',views.remove),
    path('update/',views.update),
    path('giveMecrud/',views.giveMecrud),
    path('setsession/',views.setsession),
    path('increase/',views.increase),
    path('check/',views.check),
    path('getuser/',views.getuser)
]