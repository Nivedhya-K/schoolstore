from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    #path('credentials/register', views.register, name='register'),
    path('login', views.login, name='login'),
    #path('credentials/login', views.login, name='login'),
    path('button',views.button,name="button"),
    #path('form',views.form,name='form'),
    path('form',views.form, name='form'),
    #path('process_form',views.process_form,name='process_form'),
    path('order_confirm',views.order_confirm,name='order_confirm'),
    path('logout',views.logout,name='logout')
]
    #path('next_page/<str:message>/',next_page,name='next_page'),
    #path('logout', views.logout, name='logout'),
    #path('get_message',views.get_message,name='get_message'),
    #path('get_courses/',views.get_courses, name='get_courses')
