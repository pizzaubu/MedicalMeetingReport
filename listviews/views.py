from django.shortcuts import render
from .forms import ReportForm

def upload_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = ReportForm()
    return render(request, 'upload_report.html', {'form': form})
