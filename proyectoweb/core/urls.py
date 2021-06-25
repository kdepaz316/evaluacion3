from django.urls import path
from .views import home, personas, registro, form_persona, form_mod_persona,form_del_persona

urlpatterns = [
    path('',home,name ="home"),
    path('personas',personas,name ="personas"),
    path('registro',registro,name ="registro"),
    path('form-personas',form_persona,name ="form_persona"),
    path('form-mod-persona/<id>',form_mod_persona,name ="form_mod_persona"),
    path('form-del-persona/<id>',form_del_persona,name ="form_del_persona"),
]