from django.db import models
from django.urls import reverse 
from datetime import date
 
MEALS = (
    ('1', 'first feeding'),
    ('2', 'second feeding'),
    ('3', 'third feeding')
) 
 
class Toy(models.Model):
  name = models.CharField(max_length=150)
  color = models.CharField(max_length=120)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id}) 

class Bird(models.Model): 
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField() 
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  feeding = models.CharField(
    max_length=1,
    choices=MEALS, 
    default=MEALS[0][0]
  )
  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
  
  def __str__(self): 
    return f"{self.get_feeding_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    
       
    