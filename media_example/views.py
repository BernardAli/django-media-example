from django.shortcuts import render, redirect

from .forms import UploadForm
from .models import ExampleModel


def media(request):
    instance = None

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("images")
    else:
        form = UploadForm()

    return render(request, "media.html", {"form": form, "instance": instance})


def images(request):
    all_images = ExampleModel.objects.all()
    context = {'all_images': all_images}
    return render(request, "images.html", context)