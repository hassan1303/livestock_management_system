
# Create your models here.
from django.db import models

# Basic Animal model for tracking
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)  # e.g., 'Cattle', 'Poultry'
    breed = models.CharField(max_length=50)
    rfid_tag = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.rfid_tag})"

# Health management model to record animal health checkups
class HealthRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    checkup_date = models.DateField()
    notes = models.TextField()
    medication_given = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.animal.name} - {self.checkup_date}"

# Breeding management model to track breeding schedules
class BreedingRecord(models.Model):
    male = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='breeding_male')
    female = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='breeding_female')
    breeding_date = models.DateField()
    expected_birth_date = models.DateField()

    def __str__(self):
        return f"{self.male.name} & {self.female.name} - {self.breeding_date}"

# Productivity tracking model to monitor productivity (e.g., milk yield or growth)
class ProductivityRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    milk_yield = models.FloatField(null=True, blank=True)  # For dairy animals
    weight = models.FloatField(null=True, blank=True)      # Track growth

    def __str__(self):
        return f"{self.animal.name} - {self.date}"
