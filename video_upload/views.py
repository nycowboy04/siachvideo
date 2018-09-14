from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Map
from .forms import VideoForm

def vid_up(request):
    submitted = False
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote?submitted=True')
        else:
            form = VideoForm()
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'video_upload/upload.html', {'form':form, 'submitted': submitted})
# Create your views here.
