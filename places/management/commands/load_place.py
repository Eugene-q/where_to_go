from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Location, Image
import os, requests, urllib.parse

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('load_address', type=str)
        
    def handle(self, *args, **options):
        response = requests.get(options['load_address'])
        response.raise_for_status()
        raw_location = response.json()
        location, created = Location.objects.get_or_create(
            title=raw_location['title'],
            lng_coordinate=raw_location['coordinates']['lng'],
            lat_coordinate=raw_location['coordinates']['lat'],
            defaults={'short_description': raw_location['description_short'],
                      'long_description': raw_location['description_long'],
                  },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    '{location_name} created sucsessfully'.format(
                        location_name=raw_location['title'],
                    ),
                ),
            )
            for img_link in raw_location['imgs']:
                image_obj = Image.objects.create(location=location)
                response = requests.get(img_link)
                response.raise_for_status()
                image_content = ContentFile(response.content)
                img_path = urllib.parse.urlsplit(urllib.parse.unquote(img_link)).path
                image_folder_path, image_name = os.path.split(img_path)
                self.stdout.write('saving ' + image_name)
                image_obj.image.save(image_name, image_content, save=True)
        else:
            self.stdout.write(
                self.style.ERROR(
                    '{raw_location} already exists in database!'.format(
                        raw_location=raw_location['title'],
                    ),
                ),
            )

