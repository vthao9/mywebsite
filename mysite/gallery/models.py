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

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    comment_on = models.ForeignKey(Image, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('gallery:index')

    def __str__(self):
        return self.addcomment

class Bucket(models.Model):
    name = models.CharField(max_length=500)
    imagefile = models.ImageField(upload_to='images/', null=True, verbose_name="")
    description = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('gallery:bucketdetail', kwargs={'bucket_id': self.pk})

    def __str__(self):
        return self.name + " - " + str(self.imagefile)

class BucketUpload(models.Model):
    imgname = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('gallery:bucketlist')

    def __str__(self):
        return self.pname
