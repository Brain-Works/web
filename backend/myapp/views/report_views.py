from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.http import require_http_methods
from xhtml2pdf import pisa
import os
from django.conf import settings
from datetime import datetime
import pytz


@require_http_methods(["GET", "POST"])
def fetch_data(request):
    kst = pytz.timezone('Asia/Seoul')
    now = datetime.now(kst)
    if request.method == 'POST':
        context = {
            'patient_name': request.POST.get('patient_name', 'None'),
            'patient_id': request.POST.get('patient_id', 'None'),
            'age': request.POST.get('age', 'None'),
            'gender': request.POST.get('gender', 'None'),
            'date_of_birth': request.POST.get('date_of_birth', 'None'),
            'radiology_type': request.POST.get('radiology_type', 'None'),
            'test_date': request.POST.get('test_date', now.strftime('%Y-%m-%d')),
            'test_time': request.POST.get('test_time', now.strftime('%H:%M')),
            'department': request.POST.get('department', 'None'),
            'diagnosis': request.POST.get('diagnosis', 'None'),
            'medications': request.POST.get('medications', 'None'),
            'ordering_physician': request.POST.get('ordering_physician', 'None'),
            'radiology_physician': request.POST.get('radiology_physician', 'None'),
            'ai_analysis_image': request.POST.get('ai_analysis_image', request.session.get('image_url', 'None')),
            'ai_interpretation': request.POST.get('ai_interpretation', 'None'),
            'physician_manifestation': request.POST.get('physician_manifestation', 'None'),
            'predicted_class_name': request.session.get('predicted_class_name', 'None'),
            'confidence': request.session.get('confidence', 'None')
        }
        return generate_pdf(request, context)
    else:
        return render(request, 'report_form.html')

def generate_pdf(request, context):
    template_path = 'myapp/report_template.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="alzheimer_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('오류가 발생했습니다. <pre>' + html + '</pre>')
    return response

@require_http_methods(["GET"])
def download_report(request):
    kst = pytz.timezone('Asia/Seoul')
    now = datetime.now(kst)

    context = {
        'patient_name': '홍길동',
        'patient_id': '12345',
        'age': '30',
        'gender': '남성',
        'date_of_birth': '1993-01-01',
        'radiology_type': 'MRI',
        'test_date': now.strftime('%Y-%m-%d'),
        'test_time': now.strftime('%H:%M'),
        'department': '신경외과',
        'diagnosis': '알츠하이머',
        'medications': 'None',
        'ordering_physician': 'Dr. Kim',
        'radiology_physician': 'Dr. Lee',
        'ai_analysis_image': request.session.get('image_url', os.path.join(settings.MEDIA_URL, 'images/MRI.jpg')),
        'ai_interpretation': 'AI 해석 결과',
        'physician_manifestation': '의사 소견',
        'predicted_class_name': request.session.get('predicted_class_name'),
        'confidence': request.session.get('confidence')
    }
    return generate_pdf(request, context)
