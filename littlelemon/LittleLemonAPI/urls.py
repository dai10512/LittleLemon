from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.BookingViewSet)  # 空文字列で登録
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/',include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]
