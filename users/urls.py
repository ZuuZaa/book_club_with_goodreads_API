from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('editprofile/', editprofile, name="editprofile"),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name="logout"),
    path('userprofile/<int:user_id>/', userprofile, name = 'userprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)