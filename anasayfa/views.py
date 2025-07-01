from django.shortcuts import render

from anasayfa.models import InfoBox


def home(request):
    return render(request , 'anasayfa/home.html')

# Create your views here.

def home_view(request):
   info_boxes = InfoBox.objects.all()
   return render(request , 'anasayfa/home.html' , {'info_boxes':info_boxes})