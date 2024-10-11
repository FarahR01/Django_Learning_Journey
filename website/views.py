from django.shortcuts import render

from meetings.models import Meeting

# Create your views here.
# def home_view(request):
#     return render(request, 'website/home.html')


#New verion V3 
def home_view(request):
    context={'meetings': Meeting.objects.all()}
    return render(request, "website/home.html",context=context)

def about_view(request):
    return render(request, 'website/about.html')

