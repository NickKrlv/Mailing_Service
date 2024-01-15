from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mailing import views

app_name = 'mailing'

urlpatterns = [
    path('', views.index, name='index'),
    path('client_list/', views.ClientListView.as_view(), name='client_list'),
    path('client_detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('distribution_list/', views.DistributionListView.as_view(), name='distribution_list'),
    path('distribution_detail/<int:pk>/', views.DistributionDetailView.as_view(), name='distribution_detail'),
    path('distribution_create/', views.DistributionCreateView.as_view(), name='distribution_create'),
    path('distribution_update/<int:pk>/', views.DistributionUpdateView.as_view(), name='distribution_update'),
    path('distribution_delete/<int:pk>/', views.DistributionDeleteView.as_view(), name='distribution_delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
