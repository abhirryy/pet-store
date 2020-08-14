from django.shortcuts import render
from django.http import Http404

from .models import Pet 
def home(request):
	pets = Pet.objects.all() # the render functions pass the responsibility of rendering Html to the templets 
	return render(request, 'home.html', {'pets':pets,})

def pet_detail(request, pet_id):
	try:
		pet =Pet.objects.get(id=pet_id)
	except Pet.DoesNotExist:
		raise Http404('pet not found')
	return render(request,'pet_detail.html',{'pet':pet,}) 