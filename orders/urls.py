from rest_framework.routers import DefaultRouter

from orders import views

app_name = 'orders'


router = DefaultRouter()
router.register('', views.OrderViewSet, basename='orders')
router.register('status', views.StatusViewSet, basename='status')


urlpatterns = [

] + router.urls
