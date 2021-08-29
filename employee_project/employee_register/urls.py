from django.contrib import auth
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView
import employee_register
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # get and post  req . for insert operation (hoat dong chen )
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', views.loginpage, name='loginpage'),
    # path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('insert/', views.employee_form1, name='employee_insert'),
    # get and post  req . for update operation (hoat dong update)
    path('<int:id>/', views.employee_form1, name='employee_update'),
    # get req . to retrieve and display all records
    path('list/', views.employe_list, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # path('logout/', LogoutView, {'next/page': '/'}, name='logout'),
    # Login and logout
]
