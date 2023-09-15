from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.aboutus,name="about"),
    path('home-games/',views.home_game,name="homegame"),
    path('panier/',views.panier,name="panier"),
    
    path('check-out/',views.checkout,name="checkout"),
    path('check-out/paiment/',views.paiment,name="paiment"),
    path('signup/',views.signup,name='signup') ,
    path('signin/',views.signin,name='signin'), 
    path('logout/', views.logout_view, name='logout'),
]