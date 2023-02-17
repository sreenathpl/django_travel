from django.shortcuts import render
from . models import place, team
# Create your views here.
def home(request):
    obj = place.objects.all()
    #return render(request,'index.html',{'result':obj})

    people = team.objects.all()
    return render(request,'index.html',{'result':obj, 'team':people})
