
from django.contrib import admin
from django.urls import path, include
from noteapp import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView


router = DefaultRouter()
router.register('notes', views.NoteView, basename='notes')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('refreshtoken/', TokenRefreshView.as_view(), name ='token_refresh_pair'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify_pair'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair')

]
