from django.contrib import admin
from .models import Image, PersonUpload, Bucket, BucketUpload

# Register your models here.
admin.site.register(Image)
admin.site.register(PersonUpload)
admin.site.register(Bucket)
admin.site.register(BucketUpload)
