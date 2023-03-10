from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Bird, Toy
from .forms import FeedingForm 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request): 
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  id_list = bird.toys.all().values_list('id')
  toys_bird_doesnt_have = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', { 
    'bird': bird,
    'feeding_form': feeding_form,
    'toys': toys_bird_doesnt_have
  }) 

def add_feeding(request, bird_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save() 
  return redirect('detail', bird_id=bird_id)

def assoc_toy(request, bird_id, toy_id): 
  Bird.objects.get(id=bird_id).toys.add(toy_id)
  return redirect('detail', bird_id=bird_id) 

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'species', 'description', 'age']
    success_url= '/birds/'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['species', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'




