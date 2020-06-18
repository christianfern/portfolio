from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-me', views.about_me, name="about-me"),
    path('demos', views.demos, name="demos"),
    path('processing-demo', views.processing_demo, name="processing-demo"),
    path('definitions-api-demo', views.definitions_api_demo, name="definitions-api-demo"),
]