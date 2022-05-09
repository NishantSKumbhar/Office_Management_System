from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='emp-home'),
    path('about/', views.about, name='emp-about'),
    path('contact/', views.contact, name='emp-contact'),
    path('employeeInfo_Table/', views.emp_table, name='emp-table'),
    path('employeeInfo_Card/', views.emp_card, name='emp-card'),
    path('add_Employee/', views.emp_add, name='emp-add'),
    path('remove_Employee/', views.remove_emp, name='emp-remove'),
    path('remove_Employee/remove_emp/<int:emp_id>', views.remove_emp, name='emp-remove'),
]
