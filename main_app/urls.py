from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path(
        'cars/<int:car_id>/add-info/',
        views.add_info,
        name='add-info'
    ),
    path('rims/create', views.RimCreate.as_view(), name='rim-create'),
    path('rims/<int:pk>/', views.RimDetail.as_view(), name='rim-detail'),
    path('rims/', views.RimList.as_view(), name='rim-index'),
    path('rims/<int:pk>/update/', views.RimUpdate.as_view(), name='rim-update'),
    path('rims/<int:pk>/delete/', views.RimDelete.as_view(), name='rim-delete'),
    path('cars/<int:car_id>/associate-rim/<int:rim_id>/', views.associate_rim, name='associate-rim'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)