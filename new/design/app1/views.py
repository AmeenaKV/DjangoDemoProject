from django.shortcuts import render
from app1.models import Place,Team
# Create your views here.
def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})
# def addplace(request):
#     if(request.method=="POST"):
#         n=request.POST['n']
#         d=request.POST['d']
#         i=request.FILES['i']
#         p=Place.objects.create(name=n,description=d,image=i)
#         p.save()
#         return viewplace(request)
#     return render(request,'addplace.html')
# def viewplace(request):
#     pl=Place.objects.all()
#     return render(request,'viewplace.html',{'p':pl})