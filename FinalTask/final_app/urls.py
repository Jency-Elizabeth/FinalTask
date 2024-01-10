from . import views
from django.urls import path
app_name='final_app'

urlpatterns = [

    path('',views.index,name='index'),
]