
from django import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.static import serve
from mobikode_app.views import delete_view, login , home ,addnew, myTeam_view, signout,delete ,update_data, myTeamView,download_data_as_excel

from django.http import HttpResponse

urlpatterns = [
    
    path('' , home , name='home' ), 
    #path('admin/auth/' , home , name='home' ), 
#    path('static/' , home , name='home' ), 
    path('login/' ,login  , name='login'),
    path('addnew',addnew,name='addnew'),
    # path('delete-emp/<int:id>' , delete ),
    path('<int:id>/delete', delete_view , name="delete_view"),
    path('login/' ,login  , name='login'),
    path('<int:id>/edit' , update_data,name="update_data" ), 
    path('logout/',signout,name='signout'),
    path('myTeam/', myTeam_view, name='myTeam_view'),
    re_path(r'^myTeamView/$', myTeamView, name="myTeamView"),
    path('download/', download_data_as_excel, name='download_data'),

    
    # old code
    # path('myTeam/<str:data>/', myTeam_view, name='myTeam_view'),
    # path('<int:id>/<int:pageType>/edit', update_data1, name='update_data1'),
    # path('myTeamView/', myTeam_view, name='myTeam_view'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   