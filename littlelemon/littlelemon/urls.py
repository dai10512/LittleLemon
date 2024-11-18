# update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from LittleLemonAPI import views

# router = routers.DefaultRouter()
# router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 外部向け
    # path('restaurant/', include('restaurant.urls')),
    # path('restaurant/menu/', include('restaurant.urls')),
    # path('restaurant/booking/', include(router.urls)),
    # 内部むけ
    path('api/', include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
