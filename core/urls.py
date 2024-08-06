from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('wines/', views.wine_index, name='wine-index'),
    path('wines/create/', views.WineCreate.as_view(), name='wine-create'),
    path('wines/<int:wine_id>/', views.wine_detail, name='wine-detail'),
    path('wines/<int:pk>/update', views.WineUpdate.as_view(), name='wine-update'),
    path('wines/<int:pk>/delete', views.WineDelete.as_view(), name='wine-delete'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('user-logout/', views.user_logout, name='user-logout'),
]