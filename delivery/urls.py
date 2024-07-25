from django.urls import path,include
from . import views

urlpatterns = [
    path('delireg',views.delireg,name='delireg'),
    path('delilog',views.delilog,name='delilog'),
    path('delihome',views.delihome,name='delihome'),
    path('dprofile',views.dprofile,name='dprofile'),
    path('deditprofile',views.deditprofile,name='deditprofile'),
    path('dBooking',views.dBooking,name='dBooking'),
    path('orderconf<int:id>',views.orderconf,name="orderconf"),
    path('completedstatus<int:id>',views.completedstatus,name="completedstatus"),


    
]
