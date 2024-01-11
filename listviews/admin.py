from django.contrib import admin
from .models import Report
from .forms import ReportForm

class ReportAdmin(admin.ModelAdmin):
    form = ReportForm
    list_display = ('header', 'report_id', 'file')
    search_fields = ('header', 'report_id')

    def save_model(self, request, obj, form, change):
        if change:  # การแก้ไขรายงาน
            # ลบไฟล์เก่าถ้ามีการอัปโหลดไฟล์ใหม่
            if 'file' in request.FILES:
                if obj.file:
                    obj.file.delete()
        super().save_model(request, obj, form, change)

admin.site.register(Report, ReportAdmin)
