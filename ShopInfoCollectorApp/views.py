#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from forms import *
from models import ContactInfo


def record_districinfo(request):
    return render(request, 'ShopInfoCollectorApp/step1_districtinfo.html', locals())

def record_basicinfo(request):
    form = BasicInfoForm(
        initial={}
    )
    return render(request, 'ShopInfoCollectorApp/step2_basicinfo.html', locals())

def record_macaddress(request):
    form = MacAddressInfoForm(
            initial={}
        )
    return render(request, 'ShopInfoCollectorApp/step3_macaddress.html', locals())

def record_contactinfo(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # save to database ContactInfo
            ContactInfo.objects.create(**cd)
            return HttpResponseRedirect('/record/done/')
    else:
        form = ContactInfoForm()
    return render(request, 'ShopInfoCollectorApp/step4_contactinfo.html', {'form': form})

def record_chainstoreinfo(request):
    form = ChainShopInfoForm()
    return render(request, 'ShopInfoCollectorApp/step5_chainstoreinfo.html', locals())

def content_verification(request):
    return render(request, 'ShopInfoCollectorApp/step6_recording_verification.html', locals())

def record_successfully(self):
    return HttpResponse('Record Successfully')
