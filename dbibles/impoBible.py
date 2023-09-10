
# # import xml.etree.ElementTree as ET
# # from django.shortcuts import HttpResponse
# # # from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

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

