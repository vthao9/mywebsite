from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView#, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import View
from .models import Image, PersonUpload
from . import models
from . import views
from .forms import UserForm
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

class UserFormView(View):
    form_class = UserForm
    template_name = 'gallery/register_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('gallery:index')

        return render(request, self.template_name, {'form': form})
