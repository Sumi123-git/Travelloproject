from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from. models import place
from. models import member
# Create your views here.
def demo(request):
    obj=place.objects.all()
    abab=member.objects.all()
    return render(request,"index.html",{'result':obj,'resu':abab})