import os
import django.shortcuts
from django.shortcuts import render, redirect, HttpResponse
from .form import Form_input
from .models import Image_upload, image_groups
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
 
def home(request):
    image_diff = image_groups()
    image_diff.macro_name = 'Macro'
    image_diff.sky_name = 'Sky'
    image_diff.light_name = 'Light'
    image_diff.thunder_name = 'Insect'
    Img_obj = Image_upload.objects.filter(Name='macro')[0:12:2]
    sky_img_obj = Image_upload.objects.filter(Name="sky")[0:3]
    contents = {'images': Img_obj, 'image': sky_img_obj, 'image_diff': image_diff}
    return django.shortcuts.render(request, 'Home.html', contents)


def upload_forms(request):
    Img_obj = Image_upload.objects.all()
    form_obj = Form_input()
    context = {"form": form_obj, 'images': Img_obj}
    return django.shortcuts.render(request, 'Upload.html', context)


@login_required(login_url="{% url 'Login' %}")
def uploads(request):
    if request.method == 'POST':
        form_obj = Form_input(request.POST, request.FILES)
        if form_obj.is_valid():
            MyFile_name = request.POST.get('Form_name')
            MyFile_image = request.FILES.get('Form_image')
            Image_upload.objects.create(Name=MyFile_name, Image=MyFile_image).save()
        return django.shortcuts.redirect('Upload')


def delete(request, id):
    delete_data = Image_upload.objects.get(id=id)
    delete_data.delete()
    os.remove(delete_data.Image.path)
    # return render(request, 'Home.html')
    return django.shortcuts.redirect('Home')


def images_show(request):
    Img_obj = Image_upload.objects.filter(Name="macro")
    sky_img_obj = Image_upload.objects.filter(Name="sky")
    contents = {'images': Img_obj, 'sky_img': sky_img_obj}
    return django.shortcuts.render(request, 'Images.html', contents)


def images_shows(request, name):
    Img_obj = Image_upload.objects.filter(Name=name.lower())
    # sky_img_obj = Image_upload.objects.filter(Name="sky")
    # contents = {'images': Img_obj, 'sky_img': sky_img_obj}
    size = 0
    if name == 'macro' or name == 'insect' or name == 'light':
        size = 15
    elif name == 'sky':
        size = 25

    contents = {'images': Img_obj, 'name': name.upper(), 'size': size}
    return django.shortcuts.render(request, 'Images.html', contents)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('Upload')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'Login.html')

# Login request:
def Logout(request):
    logout(request)
    return render(request, 'Login.html')
