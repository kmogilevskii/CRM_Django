from django.urls import path
from .views import lead_create, lead_detail, all_leads, update_lead, delete_lead

app_name = "leads"

urlpatterns = [
    path('', all_leads),
    path('create/', lead_create),
    path('<int:pk>/', lead_detail),
    path('<int:pk>/update/', update_lead),
    path('<int:pk>/delete/', delete_lead)
]
