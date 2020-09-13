from django.urls import path

from . import views

app_name='portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('about-me', views.about_me, name="about-me"),
    path('demos', views.demos, name="demos"),
    path('experience', views.experience, name="experience"),
    path('processing-demo', views.processing_demo, name="processing-demo"),
    path('definitions-api-demo', views.definitions_api_demo, name="definitions-api-demo"),
    path('definitions-api-demo-response', views.definitions_api_demo_response, name="definitions-api-demo-response")
]