from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sheet 

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
    return render(request, 'sheets/detail.html', {
        'sheet': sheet
    })

class SheetCreate(CreateView): 
    model = Sheet
    fields = '__all__'

class SheetUpdate(UpdateView):
    model = Sheet
    fields = '__all__'

class SheetDelete(DeleteView): 
    model = Sheet 
    success_url = '/sheets'