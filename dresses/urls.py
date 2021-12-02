
from django.urls import path, include

from dresses import views

app_name='dresses'
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('contactus/',views.contactus,name='contactus'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('service/',views.service,name='service'),
    path('shop/',views.shop,name='shop'),
    path('shopdeatil/',views.shopdetail,name='shopdetail'),
    path('kurta/',views.kurtas,name='kurtas'),
    path('kurtaset/',views.kurtasets,name='kurtasets'),
    path('saree/',views.sarees,name='sarees'),
    path('top/',views.tops,name='tops'),
    path('jewellery/',views.jewellerys,name='jewellerys'),
    path('handbag/',views.handbags,name='handbags'),
    path('kurtadetail/<int:pk>',views.kurtadetails,name='kurtadetails'),
    path('kurtasetdetail/<int:pk>',views.kurtasetdetails,name='kurtasetdetails'),
    path('topdetail/<int:pk>',views.topdetails,name='topdetails'),
    path('sareedetail/<int:pk>',views.sareedetails,name='sareedetails'),
    path('jewellerydetail/<int:pk>',views.jewellerydetails,name='jewellerydetails'),
    path('handbagdetail/<int:pk>',views.handbagdetails,name='handbagdetails'),
    path('booking/',views.booking,name='booking')
]