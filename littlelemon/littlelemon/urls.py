# update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include
from restaurant import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/menu/', include('restaurant.urls')),
    path('restaurant/booking/',include(router.urls))
]
