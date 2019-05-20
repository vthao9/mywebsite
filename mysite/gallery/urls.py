from django.urls import path, re_path

from . import views

app_name = 'gallery'

urlpatterns = [
    # path('', views.showimage),
    path('', views.index, name='index'),
    path('bucket/', views.bucketindex, name='bucketlist'),
    re_path(r'^(?P<image_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^bucketdetail/(?P<bucket_id>[0-9]+)/$', views.bucketdetail, name='bucketdetail'),
    path('add/', views.ImageCreate.as_view(), name='add'),
    path('p-add/', views.PersonUploadCreate.as_view(), name='p-add'),
    path('add-bucket/', views.BucketCreate.as_view(), name='add-bucket'),
    path('p-add-bucket/', views.BucketUploadCreate.as_view(), name='p-add-bucket'),
    path('register/', views.UserFormView.as_view(), name='register'),
]
