import os
import sys
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from models import BibleVersion, BibleBook, BibleChapter, BibleVerse
import django

dbibles_app_path = '/dbibles'
sys.path.append(dbibles_app_path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Initialize Django
django.setup()


class Command(BaseCommand):
    help = 'Populates the database with Bible versions from XML files.'

    def handle(self, *args, **options):
        # Specify the path to the XML files
        xml_files_path = 'data/'  # Update with the actual path

        # Get the list of XML files in the directory
        xml_files = [f for f in os.listdir(xml_files_path) if f.endswith('.xml')]
        print(xml_files)

        for xml_file in xml_files:
            file_path = os.path.join(xml_files_path, xml_file)

            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Get the Bible version name from the XML
            biblename = root.get('biblename')

            # Create the BibleVersion object
            bible_version, _ = BibleVersion.objects.get_or_create(name=biblename)

            # Iterate over the BIBLEBOOK elements
            for biblebook in root.findall('BIBLEBOOK'):
                bnumber = int(biblebook.get('bnumber'))
                bname = biblebook.get('bname')

                # Create the BibleBook object
                bible_book, _ = BibleBook.objects.get_or_create(version=bible_version, number=bnumber, name=bname)

                # Iterate over the CHAPTER elements
                for chapter_element in biblebook.findall('CHAPTER'):
                    cnumber = int(chapter_element.get('cnumber'))

                    # Create the BibleChapter object
                    bible_chapter, _ = BibleChapter.objects.get_or_create(book=bible_book, number=cnumber)

                    # Iterate over the VERS elements
                    for verse_element in chapter_element.findall('VERS'):
                        vnumber = int(verse_element.get('vnumber'))
                        content = verse_element.text

                        # Create the BibleVerse object
                        bible_verse, _ = BibleVerse.objects.get_or_create(chapter=bible_chapter, number=vnumber, content=content)

        self.stdout.write(self.style.SUCCESS('Bible versions imported successfully.'))
