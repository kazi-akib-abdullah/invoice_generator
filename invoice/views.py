from django.shortcuts import render
from django.db.models import Q
from .models import Profile
import pdfkit
from django.http import HttpResponse, Http404
from django.template import loader
import os
from django.conf import settings

import io

# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        profile = Profile(name=name, phone=phone, address=address)
        profile.save()
    return render(request, 'invoice/accept.html')

def list(request):
    profiles = Profile.objects.all()
    name = request.GET.get('name')
    if name != '' and name is not None:
        profiles = profiles.filter(Q(phone__icontains = name) | Q(name__icontains = name))
    return render(request, 'invoice/list.html', {'profiles':profiles})

def read_invoice(request, id):
	user_profile = Profile.objects.get(pk=id)
	return render(request, 'invoice/xx.html', {'user_profile':user_profile})

def invoice(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('invoice/xx.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'A4',
        'page-height': '210mm',
        'page-width': '148mm',
        'encoding':"UTF-8",
        'dpi': 400,
        'custom-header' : [('Accept-Encoding', 'gzip')],
        'no-outline': None,
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "{}.pdf"'.format(Profile.name)
    return response
