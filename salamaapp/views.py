from django.contrib import auth
from django.shortcuts import redirect, render
from .models import youthpost,January,Feburary,March,April,May,June,July,August,September,October,November,December,fileupload
from .models import audioMessage, pastorsCorner
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def index(request):

    message= audioMessage.objects.all()

    return render(request, 'index.html', {'messages':message})


def about(request):

    return render(request, 'about.html')


def donation(request):
    


    return render(request, 'donation.html')


def programs(request):
    jan= January.objects.all()
    feb= Feburary.objects.all()
    march= March.objects.all()
    april= April.objects.all()
    may= May.objects.all()
    june= June.objects.all()
    july= July.objects.all()
    aug= August.objects.all()
    sept= September.objects.all()
    oct= October.objects.all()
    nov= November.objects.all()
    dec= December.objects.all()

    

    return render(request, 'programs.html', {'jan': jan, 'feb': feb, 'march': march, 'april': april, 'may': may, 'june':june, 'july':july, 'august': aug, 'sept': sept, 'oct':oct, 'nov': nov, 'dec': dec})

def post(request,pk):

    post= youthpost.objects.get(id=pk)

    return render(request, 'post.html', {'posts':post})

def youthpage(request):
    post= youthpost.objects.all()

    return render(request, 'youthpage.html', {'posts':post})
  

def download(request):
    file= fileupload.objects.all()

    

    return render(request, 'download.html', {'files':file})


def message(request):
    message= pastorsCorner.objects.all()



    return render(request, 'message.html', {'messages': message})


def pastorpost(request, pk):

    message= pastorsCorner.objects.get(id=pk)

    return render(request, 'pastorpost.html', {'messages':message})