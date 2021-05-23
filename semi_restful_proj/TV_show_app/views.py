from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


# Create your views here.
def index(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request , 'shows.html', context)

def new(request):
    if request.method =='POST':
        errors = Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request,val)
            return render(request,'new.html')
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        
        Show.objects.create(title=title, network=network, release_date=release_date, description=description)
    
    return render(request,'new.html')
    
def edit(request, show_id):
    if request.method == 'POST':
        errors = Show.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request,val)
            return render(request,'edit.html')
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        description = request.POST['description']
        show = Show.objects.get(id=show_id)
        show.title=title
        show.network=network
        show.release_date = release_date
        show.description = description
        show.save()
        return redirect('/shows/')
    
    show_to_edit = Show.objects.get(id=show_id)
    context = {
       'show': show_to_edit
    }
    return render(request, 'edit.html' , context)

def show(request, show_id):
    show_to_display = Show.objects.get(id=show_id)
    context = {
        'show': show_to_display
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/')
        

    
