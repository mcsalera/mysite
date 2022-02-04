from django.urls import path
from django.views.generic.base import TemplateView


app_name = 'purehtml'
urlpatterns = [
    path('', TemplateView.as_view(template_name='purehtml/index.html'), name='home'),
    path('interval/', TemplateView.as_view(template_name='purehtml/interval.html'), name='interval'),
    path('button/', TemplateView.as_view(template_name='purehtml/button.html'), name='button'),
    path('name/', TemplateView.as_view(template_name='purehtml/name.html'), name='name')
]
