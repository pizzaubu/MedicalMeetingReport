from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm
from .models import Report

def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_report.html')
    else:
        form = ReportForm()
    return render(request, 'listviews/upload_report.html', {'form': form})


def edit_report(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            # ลบไฟล์เก่าถ้ามีการอัปโหลดไฟล์ใหม่
            if 'file' in request.FILES:
                if report.file:
                    report.file.delete()
            form.save()
            return redirect('edit_report.html')
    else:
        form = ReportForm(instance=report)
    return render(request, 'listviews/edit_report.html', {'form': form, 'report': report})

def view_reports(request):
    reports = Report.objects.all()
    return render(request, 'listviews/view_reports.html', {'reports': reports})