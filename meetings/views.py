from django.shortcuts import redirect, render, get_object_or_404
from .models import Meeting

def meeting_list(request):
    # Récupérer toutes les réunions
    meetings = Meeting.objects.all()
    # Rendre la page meeting.html avec les données des réunions
    return render(request, 'meetings.html', {'meetings': meetings})

# Home View
def home_view(request):
    context = {'meetings': Meeting.objects.all()}
    return render(request, "website/home.html", context)

# def detail(request, id):
#     meeting = Meeting.objects.get(pk=id)
#     return render(request, "meetings/detail.html", {"meeting": meeting})

def detail(request, id):
    meeting = get_object_or_404(Meeting, id) # Récupérer le meeting par ID
    return render(request, "meetings/detail.html", {"meeting": meeting})

def delete_meeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)  # Get the meeting by ID
    if request.method == "POST":
        meeting.delete()  # Delete the meeting
        return redirect('meetings_list_view')  # Redirect to the meetings list view after deletion
    return render(request, 'confirm_delete.html', {'meeting': meeting})  # Render confirmation page