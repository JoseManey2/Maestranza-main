from django.contrib import admin
from django.urls import path, include
from inventario import views as inventario_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventario.urls')),   
    path('login/', auth_views.LoginView.as_view(template_name='inventario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', inventario_views.RegisterView.as_view(), name='register'),

]
