from django.shortcuts import render

from anasayfa.models import InfoBox, RecruitmentStep, AboutSection, WhoWeAreSection


def home(request):
    return render(request , 'anasayfa/home.html')

# Create your views here.

def home_view(request):
   info_boxes = InfoBox.objects.all()
   steps = RecruitmentStep.objects.all()
   sections = AboutSection.objects.all()
   who_we_are = WhoWeAreSection.objects.all()
   return render(request , 'anasayfa/home.html' , {
       'info_boxes':info_boxes,
       'recruitment_steps':steps,
       'sections':sections,
       'who_we_are':who_we_are,
   })



def recruitment_view(request):
    steps = RecruitmentStep.objects.all()
    return render(request , 'anasayfa/recruitment.html' , {'recruitment_steps':steps})



def about_view(request):
    sections = AboutSection.objects.all()
    return render(request , 'anasayfa/about.html' , {'sections':sections})