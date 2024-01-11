from django.urls import path
from .views import upload_report,edit_report

urlpatterns = [
    path('upload/', upload_report, name='upload_report'),
    path('report/edit/<int:report_id>/', edit_report, name='edit_report'),
    # โค้ดอื่นๆ...
]
