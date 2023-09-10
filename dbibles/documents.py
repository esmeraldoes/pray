# # myapp/documents.py

# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry
# from .models import BibleVerse, BibleChapter, BibleBook

# @registry.register_document
# class BibleVerseDocument(Document):
#     book_name = fields.TextField(attr='chapter.book.name')
#     chapter_number = fields.IntegerField(attr='chapter.number')
#     verse_number = fields.IntegerField()
#     text = fields.TextField()

#     class Index:
#         name = 'bibleverse'

#     class Django:
#         model = BibleVerse


# @registry.register_document
# class BibleChapterDocument(Document):
#     book_name = fields.TextField(attr='book.name')
#     chapter_number = fields.IntegerField()
#     text = fields.TextField()

#     class Index:
#         name = 'biblechapter'

#     class Django:
#         model = BibleChapter


# @registry.register_document
# class BibleBookDocument(Document):
#     name = fields.TextField()

#     class Index:
#         name = 'biblebook'

#     class Django:
#         model = BibleBook
