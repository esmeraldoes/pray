import xml.etree.ElementTree as ET
from django.http import HttpResponse
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

def import_bible_data(request):
    # Assuming you have the XML files in the same directory as this views.py file
    bible_files = [
        'bible1.xml',
        'bible2.xml',
        'bible3.xml',
        'bible4.xml',
    ]

    for file in bible_files:
        try:
            tree = ET.parse(file)
            root = tree.getroot()

            bible_name = root.attrib.get('biblename')
            bible_version, created = BibleVersion.objects.get_or_create(name=bible_name)

            for biblebook in root.findall('BIBLEBOOK'):
                book_name = biblebook.get('bname')
                book_number = biblebook.get('bnumber')  # Add this line to fetch the book number
                bible_book, created = BibleBook.objects.get_or_create(version=bible_version, name=book_name, number=book_number)

                for chapter_element in biblebook.findall('CHAPTER'):
                    chapter_number = chapter_element.get('cnumber')
                    bible_chapter, created = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)

                    for verse_element in chapter_element.findall('VERS'):
                        verse_number = verse_element.get('vnumber')
                        verse_text = verse_element.text.strip()
                        BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, content=verse_text)
        
        except FileNotFoundError:
            return HttpResponse(f"File '{file}' not found.")

    return HttpResponse("Bible data import complete.")


















import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.db import transaction
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

def import_bible_data(request):
    bible_files = [
        'bible1.xml',
        'bible2.xml',
        'bible3.xml',
        'bible4.xml',
    ]

    with transaction.atomic():
        for file in bible_files:
            try:
                bible_version, _ = BibleVersion.objects.get_or_create(name=file)
                bible_books = []
                bible_chapters = []
                bible_verses = []

                for event, elem in ET.iterparse(file, events=('start',)):
                    if elem.tag == 'BIBLEBOOK':
                        book_name = elem.get('bname')
                        book_number = elem.get('bnumber')
                        bible_book = BibleBook(version=bible_version, name=book_name, number=book_number)
                        bible_books.append(bible_book)

                    elif elem.tag == 'CHAPTER':
                        chapter_number = elem.get('cnumber')
                        bible_chapter = BibleChapter(book=bible_book, number=chapter_number)
                        bible_chapters.append(bible_chapter)

                    elif elem.tag == 'VERS':
                        verse_number = elem.get('vnumber')
                        verse_text = elem.text.strip()
                        bible_verse = BibleVerse(chapter=bible_chapter, number=verse_number, content=verse_text)
                        bible_verses.append(bible_verse)

                # Bulk create BibleBook, BibleChapter, and BibleVerse objects
                BibleBook.objects.bulk_create(bible_books)
                BibleChapter.objects.bulk_create(bible_chapters)
                BibleVerse.objects.bulk_create(bible_verses)

                # Clear the memory by clearing the parsed elements
                elem.clear()

            except FileNotFoundError:
                return HttpResponse(f"File '{file}' not found.")

    return HttpResponse("Bible data import complete.")


































import xml.etree.ElementTree as ET
from django.shortcuts import HttpResponse
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

def import_bible_data(request):
    file_path = 'path_to_your_xml_file.xml'  # Update with the actual file path

    tree = ET.parse(file_path)
    root = tree.getroot()

    bible_version_name = root.attrib['version']
    bible_version, _ = BibleVersion.objects.get_or_create(name=bible_version_name)

    for book_elem in root.findall('book'):
        book_name = book_elem.attrib['name']
        bible_book, _ = BibleBook.objects.get_or_create(version=bible_version, name=book_name)

        for chapter_elem in book_elem.findall('chapter'):
            chapter_number = int(chapter_elem.attrib['number'])
            bible_chapter, _ = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)

            for verse_elem in chapter_elem.findall('verse'):
                verse_number = int(verse_elem.attrib['number'])
                verse_text = verse_elem.text
                BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, text=verse_text)

    return HttpResponse("Bible data imported successfully.")
































import xml.etree.ElementTree as ET
from django.shortcuts import HttpResponse
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

def import_bible_data(request):
    file_path = 'path_to_your_xml_file.xml'  # Update with the actual file path

    tree = ET.parse(file_path)
    root = tree.getroot()

    bible_version_name = root.attrib['version']
    bible_version, _ = BibleVersion.objects.get_or_create(name=bible_version_name)

    for book_elem in root.findall('book'):
        book_name = book_elem.attrib['name']
        bible_book, _ = BibleBook.objects.get_or_create(version=bible_version, name=book_name)
        bible_book.save()

        for chapter_elem in book_elem.findall('chapter'):
            chapter_number = int(chapter_elem.attrib['number'])
            bible_chapter, created = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)

            # Check if the chapter already exists
            if not created:
                # Chapter already exists, skip to the next chapter
                continue

            bible_chapter.save()

            for verse_elem in chapter_elem.findall('verse'):
                verse_number = int(verse_elem.attrib['number'])
                verse_text = verse_elem.text
                bible_verse, _ = BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, text=verse_text)
                bible_verse.save()

    return HttpResponse("Bible data imported successfully.")














import xml.etree.ElementTree as ET
from django.shortcuts import HttpResponse
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

def import_bible_data(request):
    file_path = 'path_to_your_xml_file.xml'  # Update with the actual file path

    tree = ET.parse(file_path)
    root = tree.getroot()

    bible_version_name = root.attrib['version']
    bible_version, _ = BibleVersion.objects.get_or_create(name=bible_version_name)

    for book_elem in root.findall('book'):
        book_name = book_elem.attrib['name']
        bible_book, _ = BibleBook.objects.get_or_create(version=bible_version, name=book_name)

        for chapter_elem in book_elem.findall('chapter'):
            chapter_number = int(chapter_elem.attrib['number'])
            bible_chapter, created = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)

            # Check if the chapter already exists
            if not created:
                # Chapter already exists, skip to the next chapter
                continue

            for verse_elem in chapter_elem.findall('verse'):
                verse_number = int(verse_elem.attrib['number'])
                verse_text = verse_elem.text
                bible_verse, _ = BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, text=verse_text)

    return HttpResponse("Bible data imported successfully.")






























































from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BibleVerse

class BibleVerseView(APIView):
    def get(self, request, version_id, book, chapter=None, verse=None):
        try:
            bible_verse = BibleVerse.objects.get(chapter__book__version_id=version_id,
                                                 chapter__book__name=book,
                                                 chapter__number=chapter,
                                                 number=verse)
            data = {
                'book': bible_verse.chapter.book.name,
                'chapter': bible_verse.chapter.number,
                'verse': bible_verse.number,
                'content': bible_verse.content
            }
            return Response(data)
        except BibleVerse.DoesNotExist:
            return Response({'error': 'Verse not found'}, status=404)

