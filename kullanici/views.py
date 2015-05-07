from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.template import RequestContext
from kullanici.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User



def anasayfa(request):
	return render_to_response('index.html', locals())


# Create your views here.


def giris(request):
 if request.GET.get('cikis'):
  logout(request)
  return HttpResponseRedirect('/index/')

 if request.POST.get('giris'):
  giris_formu = uye(data=request.POST)
  if giris_formu.is_valid():
   kullaniciadi = request.POST['adi']
   sifre = request.POST['parola']
   kullanici = authenticate(adi=kullaniciadi,parola=sifre)
   if kullanici is not None:
    if kullanici.is_active:
     login(request,kullanici)
 else:
  giris_formu = uye()

 return render_to_response('login.html',locals(),context_instance = RequestContext(request))



def profilsayfasi(request):
	return render_to_response('profil.html', locals())

def kayit_ekle(request):
    if request.method=='POST':
        adi=request.POST.get('adi')
        soyadi=request.POST.get('soyadi')
        eposta=request.POST.get('eposta')
        parola=request.POST.get('parola')

        kyt= uye(adi=adi, soyadi=soyadi, eposta=eposta, parola=parola)
        kyt.save()
        return HttpResponseRedirect('/login/')
    else:
        return render_to_response('login.html', context_instance=RequestContext(request))

