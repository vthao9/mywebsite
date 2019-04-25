from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your models here.
# class UploadImage(models.Model):
#     image = models.ImageField(upload_to='images/')

class Image(models.Model):
    name = models.CharField(max_length=500)
    imagefile = models.ImageField(upload_to='images/', null=True, verbose_name="")
    description = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'image_id': self.pk})

    def __str__(self):
        return self.name + " - " + str(self.imagefile)

class PersonUpload(models.Model):
    imgname = models.ForeignKey(Image, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('gallery:index')
        # return reverse('gallery:detail', kwargs={'image_id': self.pk})

    def __str__(self):
        return self.pname
