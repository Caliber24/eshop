from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us', views.AboutView.as_view(), name='about_page'),
    # path('site-header', views.site_header_component,name='site_header_partial'),
    # path('site-footer', views.site_footer_component,name='site_footer_partial')
]
