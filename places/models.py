from django.db import models
from geojson import Feature, Point
from django.urls import reverse
from tinymce.models import HTMLField

class Location(models.Model):
    title = models.CharField(max_length=300)
    description_short = models.TextField(default='Краткое описание')
    description_long = HTMLField(default='Подробное описание')
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()
    
    def __str__(self):
        return self.title
        
    def get_feature(self):
        return Feature(geometry=Point([self.coordinates_lng, self.coordinates_lat]),
                       properties={'title' : self.title,
                                   'placeId' : self.id,
                                   'detailsUrl' : reverse('location_view', args=(self.id,))
                        })
            
        
class Image(models.Model):
    title = models.CharField(max_length=100, default='Картинка')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    image = models.ImageField()
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    def __str__(self):
        return '{} - {}'.format(self.title, self.location.title)
        
    class Meta(object):
        ordering = ['position',]
    
