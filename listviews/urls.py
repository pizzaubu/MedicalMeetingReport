from django.urls import path
from . import views 

urlpatterns = [
    path('upload_report/', views.upload_report, name='upload_report'),
    path('report/edit/<int:report_id>/', views.edit_report, name='edit_report'),
    path('report/', views.view_reports, name='reports')
]
