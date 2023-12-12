# book_management/management/commands/load_data_from_json.py
import json
from django.core.management.base import BaseCommand
from book_management.models import Author, Book

class Command(BaseCommand):
    help = 'Load data from a JSON file into the database'

    def handle(self, *args, **options):
        try:
            with open('mydata.json') as f:
                data = json.load(f)

                for author_data in data.get('authors', []):
                    Author.objects.create(name=author_data['name'])

                for book_data in data.get('books', []):
                    author = Author.objects.get(name=book_data['author'])
                    Book.objects.create(
                        title=book_data['title'],
                        author=author,
                        publication_year=book_data['publication_year'],
                        isbn=book_data['isbn']
                    )

                self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File mydata.json not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
