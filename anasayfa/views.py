from django.shortcuts import render

from anasayfa.models import InfoBox , RecruitmentStep


def home(request):
    return render(request , 'anasayfa/home.html')

# Create your views here.

def home_view(request):
   info_boxes = InfoBox.objects.all()
   steps = RecruitmentStep.objects.all()
   return render(request , 'anasayfa/home.html' , {
       'info_boxes':info_boxes,
       'recruitment_steps':steps
   })



def recruitment_view(request):
    steps = RecruitmentStep.objects.all()
    return render(request , 'anasayfa/recruitment.html' , {'recruitment_steps':steps})