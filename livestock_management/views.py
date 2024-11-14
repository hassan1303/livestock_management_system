
# Create your views here.
from django.shortcuts import render
from .models import Animal, HealthRecord, BreedingRecord, ProductivityRecord

# View for listing all animals
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'farm_management/animal_list.html', {'animals': animals})

# View for animal health records
def health_record_list(request):
    health_records = HealthRecord.objects.all()
    return render(request, 'livestock_management/health_record_list.html', {'health_records': health_records})

# View for breeding records
def breeding_record_list(request):
    breeding_records = BreedingRecord.objects.all()
    return render(request, 'livestock_management/breeding_record_list.html', {'breeding_records': breeding_records})

# View for productivity records
def productivity_list(request):
    productivity_records = ProductivityRecord.objects.all()
    return render(request, 'livestock_management/productivity_list.html', {'productivity_records': productivity_records})
