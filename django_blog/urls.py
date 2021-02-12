"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('sign_up/', user_views.sign_up, name='sign_up'),
    path('sign_in/', auth_views.LoginView.as_view(template_name='users/sign_in.html'), name='sign_in'),
    path('sign_out/', auth_views.LogoutView.as_view(template_name='users/sign_out.html'), name='sign_out'),
    path('profile/', user_views.profile, name='profile'),
    path('blog/', include('blog.urls')),
    path('password-reset/', 
          auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
          name='password_reset'),
    path('password-reset/done', 
          auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
          name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', 
          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
          name='password_reset_confirm'),
    path('password-reset-complete/', 
          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
          name='password_reset_complete'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
