from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from core import views


from core.views import CachorroViewSet, ComedouroViewSet, TagViewSet, PublicacoesViewSet

router = DefaultRouter()
router.register(r'cachorros', CachorroViewSet)
router.register(r'comedouro', ComedouroViewSet)
router.register(r'tags', TagViewSet)
router.register(r'publis', PublicacoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('', include(router.urls)),
    path('', views.home, name='home'),
]

