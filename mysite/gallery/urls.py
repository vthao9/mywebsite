from django.urls import path, re_path

from . import views

app_name = 'gallery'

urlpatterns = [
    # path('', views.showimage),
    path('', views.index, name='index'),
    re_path(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    path('add/', views.ImageCreate.as_view(), name='add'),
    path('p-add/', views.PersonUploadCreate.as_view(), name='p-add')
]
