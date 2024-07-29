from django.urls import path
from . import views



urlpatterns=[
    path("",views.index,name="index"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("old_url",views.old_url,name='old_page_url'),
    path("new_something_url",views.new_url,name='new_page_url'),
    path("contact",views.contact_view,name='contact'),
    path("about",views.about_view,name='about'),

    
]