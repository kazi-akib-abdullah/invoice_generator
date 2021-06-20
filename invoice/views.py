from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Profile
import pdfkit
from django.http import HttpResponse, Http404
from django.template import loader
import os
from django.conf import settings
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

import io

# Create your views here.

def accept(request):
    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        product_details = request.POST.get("product_details")
        quantity = request.POST.get("quantity")
        profile = Profile(name=name, phone=phone, address=address, product_details=product_details, quantity=quantity)        
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



def update(request, id):
    user_profile = Profile.objects.get(pk=id)
    if request.method == "POST":
        if request.POST.get("name") and request.POST.get("phone") and request.POST.get("address") and request.POST.get("price") and request.POST.get("product_details") and request.POST.get("quantity"):
            Profile.objects.filter(id=id).update(name = request.POST.get("name"), phone = request.POST.get("phone"), address = request.POST.get("address"), price = request.POST.get("price"), product_details = request.POST.get("product_details"), quantity = request.POST.get("quantity"))
            context = {'user_profile':user_profile}
            return render(request, 'invoice/edit_invoice.html')
        else:
            context = {'user_profile':user_profile,  'error': 'The post was not successfully updated.'}
            return render(request, 'invoice/edit_invoice.html', context)

        # name = request.POST.get("name")
        # phone = request.POST.get("phone")
        # address = request.POST.get("address")
        # price = request.POST.get("price")
        # product_details = request.POST.get("product_details")
        # quantity = request.POST.get("quantity")
        # profile = Profile(name=name, phone=phone, address=address, price=price, product_details=product_details, quantity=quantity)
        # profile.save()
        # return redirect('list')

    return render(request, 'invoice/edit_invoice.html', {'user_profile':user_profile})
