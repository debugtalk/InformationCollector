#encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from forms import *
from models import ContactInfo
from models import DistrictInfo

def record_basicinfo(request):
    if request.method == 'POST':
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            shoptype = cd['shop_type'].shop_type
            request.session['tempSession']= cd
            request.session['tempSession']['shop_type'] = shoptype
            request.session['tempSession']['shop_district_dict'] = {
                'province':request.REQUEST['DistrictProvince'],
                'city':request.REQUEST['DistrictCity'],
                'county':request.REQUEST['DistrictCounty']
            }
            request.session['tempSession']['mac_address_list'] = []
            request.session['tempSession']['contact_info_list'] = []
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
            macAddressList = request.session['tempSession'].get('mac_address_list', [])
            macAddressList.append(cd['mac_address'])
            request.session['tempSession']['mac_address_list'] = macAddressList
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
            request.session['tempSession']['contact_info_list'].append(cd)
            request.session.modified = True
            if request.POST.has_key('add_another_contact'):
                return HttpResponseRedirect('/record/3-contactinfo/')
            if request.POST.has_key('next_step'):
                if request.session['tempSession']['is_chain_shop']:
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
            request.session['tempSession']['chain_store_info'] = cd
            request.session.modified = True
            return HttpResponseRedirect('/record/final-verification/')
    else:
        form = ChainShopInfoForm()
    return render(request, 'ShopInfoCollectorApp/step4_chainstoreinfo.html', {'form': form})

from models import MacAddressInfo, ShopInfo, ChainStoreInfo

def save_sessiondict_to_database(sessiondict):
    mac_address_list = sessiondict.get('mac_address_list', [])
    contact_info_list = sessiondict.get('contact_info_list', [])
    is_chain_shop = sessiondict.get('is_chain_shop', False)
    c_s_i = sessiondict.get('chain_store_info', {})
    shopname = sessiondict.get('shop_name', '')
    shopaddress = sessiondict.get('shop_address', '')
    shoptype = ShopType.objects.get(shop_type=sessiondict.get('shop_type', ''))

    chainstoreinfo = ChainStoreInfo.objects.create(
        store_name = c_s_i['store_name'],
        store_adress = c_s_i['store_adress'],
        contact_name = c_s_i['contact_name'],
        contact_phone = c_s_i['contact_phone'],
    )
    shop_district_dict = sessiondict.get('shop_district_dict', {})
    district=DistrictInfo.objects.create(**shop_district_dict)
    shopinfo = ShopInfo.objects.create(
        shop_name=shopname,
        shop_address=shopaddress,
        shop_type=shoptype,
        chain_store_info=chainstoreinfo,
        shop_district=district
    )
    for mac in mac_address_list:
        m = MacAddressInfo.objects.create(mac_address = mac)
        shopinfo.mac_address_list.add(m)
    for contact in contact_info_list:
        c = ContactInfo.objects.create(
            name = contact['name'],
            duty = contact['duty'],
            phone = contact['phone'],
            email = contact['email'],
        )
        shopinfo.contact_info_list.add(c)
    shopinfo.save()

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
            save_sessiondict_to_database(tempSessionDict)
            return HttpResponseRedirect('/record/finished/')

def record_successfully(request):
    return HttpResponse('Record Successfully')
