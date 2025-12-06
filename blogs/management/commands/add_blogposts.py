from django.core.management.base import BaseCommand
from django.core.management import call_command
from blogs.models import BlogPost


class Command(BaseCommand):
    help = 'Load test data BlogPost from fixture'
    
    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        BlogPost.objects.all().delete()
        
        call_command('loaddata', 'blogpost_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
