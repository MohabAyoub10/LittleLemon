from django.urls import path, include
from rest_framework import routers
from Restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()


router.register('menu', views.MenuItemsViewSet)
router.register('booking', views.BookingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
