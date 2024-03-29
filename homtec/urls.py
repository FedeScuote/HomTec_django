from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'client', views.ClientViewSet)
router.register(r'user', views.MobileUserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'subcategory', views.SubCategoryViewSet)
router.register(r'publication', views.PublicationViewSet)
router.register(r'rating', views.RatingViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
