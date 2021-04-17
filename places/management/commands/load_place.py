from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Location, Image
import requests, json, os

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('load_address', type=str)
        
    def handle(self, *args, **options):
        place = json.loads(requests.get(options['load_address']).content)
        new_location, created = Location.objects.get_or_create(
            title=place['title'],
            short_description=place['description_short'],
            long_description=place['description_long'],
            lng_coordinate=place['coordinates']['lng'],
            lat_coordinate=place['coordinates']['lat'],
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    '{place} created sucsessfully'.format(
                        place=place['title'],
                    ),
                ),
            )
            for img_link in place['imgs']:
                image_obj = Image.objects.create(location=new_location)
                image_content = ContentFile(requests.get(img_link).content)
                folder_url, sep, image_name = img_link.rpartition('/')
                self.stdout.write('saving', image_name)
                image_obj.image.save(image_name, image_content, save=True)
        else:
            self.stdout.write(
                self.style.ERROR(
                    '{place} already exists in database!'.format(
                        place=place['title'],
                    ),
                ),
            )

