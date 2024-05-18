from django.shortcuts import render
from models import Tasks
# Create your views here.
def Tasklist(request):
    items=Tasks.objects.all()
    context={
        'Tasklist':items
    }
    return render(request,'home.html',context)
def Create_task(request):
#    creating tasks on the todo list
 
def Update_tasks(request):
    # updating tasks on the todo list
    
def remove_tasks(request):
    # deleting tasks on the todo list        
