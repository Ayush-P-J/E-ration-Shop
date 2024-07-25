

from django.urls import path
from . import views

urlpatterns = [
    path('rationreg',views.rationreg,name='rationreg'),
    path('rationlog',views.rationlog,name='rationlog'),
    path('rationhome',views.rationhome,name='rationhome'),
    path('rationproduct',views.rationproduct,name='rationproduct'),
    path('rationprofile',views.rationprofile,name='rationprofile'),
    path('viewitems',views.viewitems,name='viewitems'),
    path('rationeditprofile',views.rationeditprofile,name='rationeditprofile'),
    path('delitem<int:id>',views.delitem,name='delitem'),
    path('edit_item<int:id>',views.edit_item,name='edit_item'),
    path('booking_information',views.booking_information,name='booking_information'),

   


]
