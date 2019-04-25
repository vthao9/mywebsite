from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Image, PersonUpload
from . import models
from . import views
# Create your views here.

def index(request):
    all_images = Image.objects.all()
    context = {
        'all_images': all_images
    }
    return render(request, "gallery/images.html", context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    context = {
        'image': image
    }
    return render(request, "gallery/detail.html", context)

class ImageCreate(CreateView):
    model = Image
    fields = ['name', 'description', 'imagefile']

class PersonUploadCreate(CreateView):
    model = PersonUpload
    fields = ['pname', 'imgname']
