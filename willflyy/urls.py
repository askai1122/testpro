from django.urls import include, path
from willflyy import views
from .views import form_name_view,login,logout,newpost,thirdpage
from django.conf import settings
from django.conf.urls.static import static
from willflyy import forms



urlpatterns = [
    path('', views.login, name='login'),
    path('contactus', views.contactus, name='contactus'),
    path('aboutus/', views.aboutus,name='aboutus'),
    path('register', views.form_name_view, name='register'),
    path('home',views.home, name='home'),
    path('logout', views.logout, name='logout'),
    # path('thirdpage',thirdpage,name="thirdpage"),
    path('access', views.accessrecord, name='accessrecord'),
    # path('secondpage',views.secondpage,name='secondpage'),
    # path('thirdpage',views.PostCreate,name='thirdpage'),
    path('myprofile',views.myprofile,name='myprofile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)