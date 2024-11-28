from django.urls import path
from testapp import views

urlpatterns=[
    # path('hello/',views.hello),
    # path('hii',views.hii),
    path('add/',views.add),
    path('giveMePage/',views.giveMePage),
    path('save/',views.save),
    path('giveMeRegister/',views.giveMeRegister),
    path('getmestudinfo/',views.getmestudinfo)

]
