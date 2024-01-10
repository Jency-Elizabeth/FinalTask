from . import views
from django.urls import path
app_name='course_app'

urlpatterns = [

    path('cs',views.cs,name='cs'),
    path('comm',views.comm,name='comm'),
    path('bio',views.bio,name='bio'),
    path('BE',views.BE,name='BE'),
    path('diploma',views.diploma,name='diploma'),
]