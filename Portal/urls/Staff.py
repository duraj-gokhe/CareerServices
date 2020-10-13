from django.urls import path
from Portal.views import Staff

urlpatterns = [
    path('details',Staff.person_details, name='Persons_details'),
    path('detail/<str:pk>',Staff.person, name='Person_details'),
    path('create',Staff.create_users, name='create_users'),
    path('update/<str:pk>',Staff.update_users, name='update_users'),
    path('staff',Staff.staffId, name='staffIds')
]