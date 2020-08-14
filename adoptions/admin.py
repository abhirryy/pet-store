from django.contrib import admin

from .models import Pet

@admin.register(Pet)   #register is a decorator take model class as argument
class PetAdmin(admin.ModelAdmin): 
	list_display = ['name','species','breed','sex',] 
	# the value of the list_display should not be ManyToMany relation so vaccination is not used it.
