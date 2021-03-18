from django.db import models
from geojson import Feature, Point
from django.urls import reverse
from tinymce.models import HTMLField

class Location(models.Model):
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = HTMLField(blank=True, verbose_name='Подробное описание')
    lng_coordinate = models.FloatField(verbose_name='долгота')
    lat_coordinate = models.FloatField(verbose_name='широта')
    
    def __str__(self):
        return self.title
        
    def get_feature(self):
        return Feature(geometry=Point([self.lng_coordinate, self.lat_coordinate]),
                       properties={'title' : self.title,
                                   'placeId' : self.id,
                                   'detailsUrl' : reverse('location_view', args=(self.id,))
                        })
            
        
class Image(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Заголовок')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    image = models.ImageField(verbose_name='файл картинки')
    position = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    def __str__(self):
        return '{} - {}'.format(self.title, self.location.title)
        
    class Meta(object):
        ordering = ['position',]
