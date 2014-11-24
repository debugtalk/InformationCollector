#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from forms import *
from models import ContactInfo

def record_basicinfo(request):
    if request.method == 'POST':
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            shoptype = cd['ShopType'].ShopType
            request.session['tempSession']= cd
            request.session['tempSession']['ShopType'] = shoptype
            request.session['tempSession']['MacAddressList'] = []
            request.session['tempSession']['ContactInfoList'] = []
            request.session.modified = True
            return HttpResponseRedirect('/record/2-macaddress/')
    else:
        form = BasicInfoForm()
        request.session['tempSession'] = {}
    return render(request, 'ShopInfoCollectorApp/step1_basicinfo.html', {'form': form})

def record_macaddress(request):
    if request.method == 'POST':
        form = MacAddressInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            macAddressList = request.session['tempSession'].get('MacAddressList', [])
            macAddressList.append(cd['MacAddress'])
            request.session['tempSession']['MacAddressList'] = macAddressList
            request.session.modified = True
            if request.POST.has_key('add_another_mac'):
                return HttpResponseRedirect('/record/2-macaddress/')
            if request.POST.has_key('next_step'):
                return HttpResponseRedirect('/record/3-contactinfo/')
    else:
        form = MacAddressInfoForm()
    return render(request, 'ShopInfoCollectorApp/step2_macaddress.html', {'form': form})

def record_contactinfo(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['tempSession']['ContactInfoList'].append(cd)
            request.session.modified = True
            if request.POST.has_key('add_another_contact'):
                return HttpResponseRedirect('/record/3-contactinfo/')
            if request.POST.has_key('next_step'):
                if request.session['tempSession']['IsChainShop']:
                    return HttpResponseRedirect('/record/4-chainstoreinfo/')
                else:
                    return HttpResponseRedirect('/record/done/')
    else:
        form = ContactInfoForm()
    return render(request, 'ShopInfoCollectorApp/step3_contactinfo.html', {'form': form})

def record_chainstoreinfo(request):
    if request.method == 'POST':
        form = ChainShopInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            request.session['tempSession']['ChainStoreInfo'] = cd
            request.session.modified = True
            return HttpResponseRedirect('/record/final-verification/')
    else:
        form = ChainShopInfoForm()
    return render(request, 'ShopInfoCollectorApp/step4_chainstoreinfo.html', {'form': form})

def final_verification(request):
    tempSessionDict = request.session.get('tempSession', {})
    if request.method == 'GET':
        return render(request, 'ShopInfoCollectorApp/laststep_recording_verification.html', {'tempSessionDict': tempSessionDict})
    else: # request.method == 'POST'
        if request.POST.has_key('reset_all'):
            request.session['tempSession'] = {}
            return HttpResponseRedirect('/record/1-basicinfo/')
        if request.POST.has_key('conform_and_save'):
            # todo: save to database
            return HttpResponseRedirect('/record/finished/')

def record_successfully(self):
    return HttpResponse('Record Successfully')
