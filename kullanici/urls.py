from django.conf.urls import patterns, include, url
import kullanici.views

urlpatterns = patterns('kullanici.views',
    url(r'^index', 'anasayfa'),
	url(r'^profil', 'profilsayfasi'),
    url(r'^login', 'kayit_ekle'),
	
)
