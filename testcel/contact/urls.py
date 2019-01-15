from django.conf.urls import url
from contact.views import * # ContactView, Partenaires, MentionsLegales,Nous,Batiment,Allimentation,Riz,cg,Services,ChouhouliView
from . import views 
app_name='contact'

urlpatterns = [
    url(r'^youtube/',views.YoutubeView, name='youtube'),
    url(r'^$',ContactView.as_view(), name='contact'),
    url(r'^facebook/',views.facebookView, name='facebook'),
    url(r'^partenaires/',Partenaires.as_view(),name='partenaires'),
    url(r'^legales/',MentionsLegales.as_view(),name='legales'),
    url(r'^cg/',cg.as_view(),name='cg'),
    url(r'^services/',Services.as_view(),name='services'),
    url(r'^nous/',Nous.as_view(),name='nous'),
    url(r'^batiment/',Batiment.as_view(),name='batiment'),
    url(r'^allimentation/',Allimentation.as_view(),name='alliment'),
    url(r'^riz/',Riz.as_view(),name='riz'),
    url(r'^machouhouli$',ChouhouliView.as_view(), name='chouhouli'),

    url(r'^MpessaOnLine/',MpessaOnLine.as_view(),name='MpessaOnLine'),
    
    
]
