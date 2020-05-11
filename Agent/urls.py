from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
     path('', views.AgentHome, name='Agent'),
     path('Agentupload/', views.Agentupload, name='Agentupload'),
     path('NewAgent/', views.NewAgent, name='NewAgent'),
     path('Agentupdate/', views.Agentupdate, name='Agentupdate'),
     path('Agenthome/', views.Agenthome, name='Agenthome'),
     path('upload/', views.upload_file, name="upload_file"),
     path('Become-Agent/', views.SignupAgent, name="SignupAgent"),
     path('Ekosodin/', views.ekosodin, name="ekosodin"),
     path('BDPA/', views.bdpa, name="BDPA"),
     path('osasoge/', views.osasoge, name="osasoge"),
     path('UpdateProfile/<user_id>/', views.UpdateProfile, name="UpdateProfile"),
     path('UpdateProfilePicx/<user_id>/', views.upload_profilePicx, name="UpdateProfilePicx"),
     path('delete/<id_image>/', views.delete, name='delete'),
     path('view_Agentproperty/<str:property_id>//<str:username>/', views.show_Agentproperty, name='view_Agentproperty'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)