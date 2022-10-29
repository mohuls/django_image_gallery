from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
# Create your views here.
def home(request):
    image = request.FILES.get('image')
    if image:
        Image.objects.create(image=image)
        message = "Image successfully uploaded!"
        messages.add_message(request, messages.INFO, message)

        return redirect('home')
    images = Image.objects.all().order_by('-id')
    return render(request, 'gallery/home.html', {'images': images})