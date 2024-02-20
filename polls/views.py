from django.shortcuts import render
from polls.models import ODS_CLUBS,ODS_Player

# Create your views here.
def index(request):
    ods_clubs = ODS_CLUBS.objects.all()
    ods_player = ODS_Player.objects.all()
    
    context = {'ball':'blabla', 'ods_clubs':ods_clubs, 'ods_player':ods_player}
    return render(request, 'index.html', context)
