from django.urls import path

from .views import PostViewSet
from rest_framework.routers import SimpleRouter
# from .views import PostList, PostDetail

# Using router with viewset
router = SimpleRouter()
router.register('', PostViewSet, base_name='posts')
urlpatterns = router.urls

# Example of using the normal pattern
# urlpatterns = [
#     path('', PostList.as_view()),
#     path('<int:pk>/', PostDetail.as_view())
# ]
