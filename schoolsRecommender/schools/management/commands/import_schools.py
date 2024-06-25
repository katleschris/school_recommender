import csv
from django.core.management.base import BaseCommand
from schools.models import School

class Command(BaseCommand):
    help = 'Load schools data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to load data from')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                School.objects.create(
                        school_name=row['School Name'],
                        street=row['Street'],
                        suburb=row['Suburb'],
                        state=row['State'],
                        postcode=row['Postcode'],
                        postal_street=row['Postal Street'],
                        postal_suburb=row['Postal Suburb'],
                        postal_state=row['Postal State'],
                        postal_postcode=row['Postal Postcode'],
                        latitude=row['Latitude'],
                        longitude=row['Longitude'],
                        phone=row['Phone'],
                        education_region=row['Education Region'],
                        broad_classification=row['Broad Classification'],
                        classification_group=row['Classification Group'],
                        low_year=row['Low Year'],
                        high_year=row['High Year'],
                        total_students=row['Total Students'],
                        be_score=row['BE Score'],
                        icsea=row['ICSEA'],
                        atar_rank=row['ATAR Rank'],
                        median_atar=row['Median ATAR'],
                        percent_students_with_atar=row['% students with ATAR']
                    
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        
    