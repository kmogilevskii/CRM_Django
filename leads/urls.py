from django.urls import path
from .views import lead_create, lead_detail, all_leads, update_lead, delete_lead

app_name = "leads"

urlpatterns = [
    path('', all_leads, name="lead-list"),
    path('create/', lead_create, name="lead-create"),
    path('<int:pk>/', lead_detail, name="lead-detail"),
    path('<int:pk>/update/', update_lead, name="lead-update"),
    path('<int:pk>/delete/', delete_lead, name="lead-delete")
]
