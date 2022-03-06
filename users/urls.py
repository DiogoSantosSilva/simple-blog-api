from django.urls import path

from .views import UserViewSet
from rest_framework.routers import SimpleRouter
# from .views import UserList, UserDetail

# Using router with viewset
router = SimpleRouter()
router.register('', UserViewSet, base_name='users')
urlpatterns = router.urls

# Example of using the normal pattern
# urlpatterns = [
#     path('', UserList.as_view()),
#     path('<int:pk>/', UserDetail.as_view())
# ]
