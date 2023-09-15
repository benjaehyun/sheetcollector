from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sheet, Practice
from .forms import ListeningForm

# Create your views here.

# sheets = [
#     {'title': 'Clair de lune', 'description': 'The third movement of the "Suite Bergamasque", translated to moonlight from French', 'composer': 'Debussy', 'key': 'D flat Major'},
#     {'title': 'Capriccio brillant, Op. 22: Adante', 'description': 'The first movement of Op.22 composed in the 19th century for piano with or without orchesta', 'composer': 'Mendelssohn', 'key': 'B minor'},
#     {'title': 'La Campanella', 'description': "The third of Liszt's six \"Grandes etudes de Paganini\" translated to little bells from Italian", 'composer': 'Lizst', 'key': 'G sharp Minor'},
# ]

def home(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def sheets_index(request): 
    sheets = Sheet.objects.all()
    return render(request, 'sheets/index.html', {
        'sheets': sheets
    })

def sheets_detail(request, sheet_id): 
    sheet = Sheet.objects.get(id=sheet_id) 
    id_list = sheet.practices.all().values_list('id')
    practices_sheet_doesnt_have = Practice.objects.exclude(id__in=id_list)
    listening_form = ListeningForm()
    return render(request, 'sheets/detail.html', {
        'sheet': sheet, 
        'listening_form': listening_form, 
        'practices': practices_sheet_doesnt_have
    })

def add_listening(request, sheet_id): 
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.sheet_id = sheet_id
        new_listening.save()
    return redirect('detail', sheet_id = sheet_id)

def assoc_practice(request, sheet_id, practice_id): 
    Sheet.objects.get(id=sheet_id).practices.add(practice_id)
    return redirect('detail', sheet_id = sheet_id)

def unassoc_practice(request, sheet_id, practice_id): 
    Sheet.objects.get(id=sheet_id).practices.remove(practice_id)
    return redirect('detail', sheet_id = sheet_id)


class SheetCreate(CreateView): 
    model = Sheet
    fields = ['title', 'description', 'composer', 'key', 'diatonic']

class SheetUpdate(UpdateView):
    model = Sheet
    fields = '__all__'

class SheetDelete(DeleteView): 
    model = Sheet 
    success_url = '/sheets'

class PracticeList(ListView): 
    model = Practice 

class PracticeDetail(DetailView): 
    model = Practice 

class PracticeCreate(CreateView): 
    model = Practice 
    fields = '__all__'

class PracticeUpdate(UpdateView): 
    model = Practice 
    fields = ['notes']

class PracticeDelete(DeleteView): 
    model = Practice 
    success_url = '/practices'



