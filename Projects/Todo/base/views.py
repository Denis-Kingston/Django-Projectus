from django.shortcuts import render
from .models import Tasks
# Create your views here.
def Tasklist(request):
    items=Tasks.objects.all()
    context={
        'Tasklist':items
    }
    return render(request,'home.html',context)
def Create_task(request):
   return('create') 
    
def Update_task(request):
    return ('update') 

def Delete_task(request):
    return('delete')   