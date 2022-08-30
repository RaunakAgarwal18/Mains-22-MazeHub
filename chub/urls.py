from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='chub/login.html'), name='login'),
    path('guidelines',views.guide,name='guide'),
    path('dsafasgadfdkh',views.q1,name='1'),
    path('dsfsafsfsdf',views.q2,name='2'),
    # path('3',views.q3,name='3'),
    # path('4',views.q4,name='4'),
    # path('5',views.q5,name='5'),
]