from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index1, name='index1'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signup/add_user/',views.add_user,name='add_user'),
    path('login/check_user/',views.check_user,name='check_user'),
    path('signup/add_user/seller/buyer/',views.buyer,name='buyer'),
    path('login/check_user/seller/buyer/',views.buyer,name='buyer'),
    path('signup/add_user/seller/',views.seller,name='seller'),
    path('login/check_user/seller/',views.seller,name='seller'),
    path('login/check_user/fe/',views.fe,name='fe'),
    path('login/check_user/comp/',views.comp,name='comp'),
    path('login/check_user/it/',views.it,name='it'),
    path('login/check_user/entc/',views.entc,name='entc'),
    path('signup/add_user/fe/',views.fe,name='fe'),
    path('signup/add_user/comp/',views.comp,name='comp'),
    path('signup/add_user/it/',views.it,name='it'),
    path('signup/add_user/entc/',views.entc,name='entc'),
    path('signup/add_user/seller/add_book',views.add_book,name='add_book'),
    path('login/check_user/seller/add_book',views.add_book,name='add_book'),
    path('login/check_user/seller/fe/',views.fe,name='fe'),
    path('login/check_user/seller/comp/',views.comp,name='comp'),
    path('login/check_user/seller/it/',views.it,name='it'),
    path('login/check_user/seller/entc/',views.entc,name='entc'),
    path('signup/add_user/buyer/',views.buyer,name='buyer'),
    path('login/check_user/buyer/',views.buyer,name='buyer'),
    path('signup/add_user/buyer/buy_book/',views.buy_book,name='buy_book'),
    path('login/check_user/buyer/buy_book/',views.buy_book,name='buy_book'),
    path('signup/add_user/seller/buyer/buy_book/',views.buy_book,name='buy_book'),
    path('login/check_user/seller/buyer/buy_book/',views.buy_book,name='buy_book'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)