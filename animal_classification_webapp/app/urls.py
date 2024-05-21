from django.urls import path,include
from . import views

app_name='app'

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('classify',views.classificationPage,name="classification_page")
]
