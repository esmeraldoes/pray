



# import xml.etree.ElementTree as ET
# from django.http import HttpResponse
# from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

# def import_bible_data(request):
# # Retrieve a verse by its ID
#     verse = BibleVerse.objects.get(id=1)

#     # Access the verse attributes
#     chapter = verse.chapter
#     number = verse.number
#     text = verse.content

#     # Print the verse details
#     print(f"Verse {number} from Chapter {chapter.number} in {chapter.book.name}:")
#     print(text)
#     return HttpResponse(f"Verse {number} from Chapter {chapter.number} in {chapter.book.name}:")








# # def import_bible_data(request):
# #     # Assuming you have the XML files in the same directory as this views.py file
# #     bible_files = [
# #         'dbibles\data\Bible_English_AMP.xml',
# #         'dbibles\data\Bible_English_MKJV.xml',
# #         'dbibles\data\Bible_English_MSG.xml',
# #         'dbibles\data\Bible_English_NASB_Strong.xml',
# #         'dbibles\data\Bible_English_NKJV.xml',
# #     ]

    
    
# #     for file in bible_files:
# #         try:
# #             tree = ET.parse(file)
# #             root = tree.getroot()

# #             bible_name = root.attrib.get('biblename')
# #             print('BIBLE NAME: ',bible_name)
# #             bible_version, created = BibleVersion.objects.get_or_create(name=bible_name)
# #             print('BIBLE VERSION :', bible_version)
# #             bible_version.save()

# #             for biblebook in root.findall('BIBLEBOOK'):
# #                 book_name = biblebook.get('bname')
# #                 book_number = biblebook.get('bnumber')  # Add this line to fetch the book number
# #                 bible_book, created = BibleBook.objects.get_or_create(version=bible_version, name=book_name, number=book_number)
# #                 print('BIBLE BOOK :', bible_book)
# #                 bible_book.save()

# #                 for chapter_element in biblebook.findall('CHAPTER'):
# #                     chapter_number = chapter_element.get('cnumber')
# #                     bible_chapter, created = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)
# #                     bible_chapter.save()
# #                     print('BIBLE CHAPTER :', bible_chapter)

# #                     for verse_element in chapter_element.findall('VERS'):
# #                         verse_number = verse_element.get('vnumber')
# #                         verse_text = verse_element.text.strip()
# #                         bible_verse, created = BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, content=verse_text)
# #                         bible_verse.save()
        
# #         except FileNotFoundError:
# #             return HttpResponse(f"File '{file}' not found.")

# #     return HttpResponse("Bible data import complete.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# # import xml.etree.ElementTree as ET
# # from django.shortcuts import HttpResponse
# # from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

# # def import_bible_data(request):
# #     file_path = 'path_to_your_xml_file.xml'  # Update with the actual file path

# #     tree = ET.parse(file_path)
# #     root = tree.getroot()

# #     bible_version_name = root.attrib['version']
# #     bible_version, _ = BibleVersion.objects.get_or_create(name=bible_version_name)

# #     for book_elem in root.findall('book'):
# #         book_name = book_elem.attrib['name']
# #         bible_book, _ = BibleBook.objects.get_or_create(version=bible_version, name=book_name)
# #         bible_book.save()

# #         for chapter_elem in book_elem.findall('chapter'):
# #             chapter_number = int(chapter_elem.attrib['number'])
# #             bible_chapter, _ = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)
# #             bible_chapter.save()

# #             for verse_elem in chapter_elem.findall('verse'):
# #                 verse_number = int(verse_elem.attrib['number'])
# #                 verse_text = verse_elem.text
# #                 bible_verse, _ = BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, text=verse_text)
# #                 bible_verse.save()

# #     return HttpResponse("Bible data imported successfully.")




















































    
#     # for file in bible_files:
#     #     try:
#     #         tree = ET.parse(file)
#     #         root = tree.getroot()

#     #         bible_name = root.attrib.get('biblename')
#     #         print(bible_name)
#     #         bible_version, created = BibleVersion.objects.get_or_create(name=bible_name)

#     #         for biblebook in root.findall('BIBLEBOOK'):
#     #             book_name = biblebook.get('bname')
#     #             bible_book, created = BibleBook.objects.get_or_create(version=bible_version, name=book_name)

#     #             for chapter_element in biblebook.findall('CHAPTER'):
#     #                 chapter_number = chapter_element.get('cnumber')
#     #                 bible_chapter, created = BibleChapter.objects.get_or_create(book=bible_book, number=chapter_number)

#     #                 for verse_element in chapter_element.findall('VERS'):
#     #                     verse_number = verse_element.get('vnumber')
#     #                     verse_text = verse_element.text.strip()
#     #                     BibleVerse.objects.get_or_create(chapter=bible_chapter, number=verse_number, text=verse_text)
        
#     #     except FileNotFoundError:
#     #         return HttpResponse(f"File '{file}' not found.")

#     # return HttpResponse("Bible data import complete.")




























































































































# # from django.shortcuts import render

# # import xml.etree.ElementTree as ET
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from .models import BibleVerse




# # from rest_framework import viewsets
# # from .models import BibleVersion
# # from .serializers import BibleVersionSerializer

# # class BibleVersionViewSet(viewsets.ModelViewSet):
# #     queryset = BibleVersion.objects.all()
# #     serializer_class = BibleVersionSerializer




# # # class BibleVerseView(APIView):
# # #     def get(self, request, book_id, chapter_num, verse_num):
# # #         try:
# # #             verse = BibleVerse.objects.get(book_id=book_id, chapter_num=chapter_num, verse_num=verse_num)
# # #             return Response({'verse': verse.text})
# # #         except BibleVerse.DoesNotExist:
# # #             return Response({'error': 'Verse not found'}, status=404)

# # # def parse_bible_xml():
# # #     tree = ET.parse('path/to/your/bible.xml')
# # #     root = tree.getroot()
# # #     verses = []

# # #     for book in root.findall('BIBLEBOOK'):
# # #         book_id = book.attrib['bnumber']
# # #         for chapter in book.findall('CHAPTER'):
# # #             chapter_num = chapter.attrib['cnumber']
# # #             for verse in chapter.findall('VERS'):
# # #                 verse_num = verse.attrib['vnumber']
# # #                 text = verse.text.strip()
# # #                 verses.append(BibleVerse(book_id=book_id, chapter_num=chapter_num, verse_num=verse_num, text=text))

# # #     BibleVerse.objects.bulk_create(verses)

