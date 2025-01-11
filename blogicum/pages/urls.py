from django.urls import path
from django.views.generic import TemplateView as TV


app_name = 'pages'

urlpatterns = [
    path('about/', TV.as_view(template_name='pages/about.html'), name='about'),
    path('rules/', TV.as_view(template_name='pages/rules.html'), name='rules'),
]
