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
    path('', views.index, name='index'),
    path('load_index/', views.load_index, name='load_index'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_request, name="logout"),
    path('search/', views.search, name="search"),
    path('AgentReg/', views.NewUser, name="NewUser"),
    path('Login/', views.loginreq, name="Login"),
    path('reply/', views.replyy, name="reply"),
    path('Userlogin/', views.loginUser, name="UserLogin"),
    path('signup/', views.signup, name="Signup"),
    path('view_property/<str:property_id>//<str:username>/', views.show_property, name='view_property'),
    path('comment/<str:property_id>//<str:username>/', views.comment, name='comment'),
    path('reply/<str:comment_id>//<str:username>/', views.send_reply, name='send_reply'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)