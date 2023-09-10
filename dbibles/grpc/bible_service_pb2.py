# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bible_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62ible_service.proto\x12\x05\x62ible\"\x0e\n\x0c\x45mptyRequest\"&\n\x13\x42ibleVersionRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\"4\n\x13\x42ibleChapterRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04\x62ook\x18\x02 \x01(\t\"R\n\x11\x42ibleVerseRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04\x62ook\x18\x02 \x01(\t\x12\x0f\n\x07\x63hapter\x18\x03 \x01(\x05\x12\r\n\x05verse\x18\x04 \x01(\x05\"V\n\x14\x43ompareVersesRequest\x12\x10\n\x08versions\x18\x01 \x03(\t\x12\x0c\n\x04\x62ook\x18\x02 \x01(\t\x12\x0f\n\x07\x63hapter\x18\x03 \x01(\x05\x12\r\n\x05verse\x18\x04 \x01(\x05\"9\n\x10\x42ibleVersionList\x12%\n\x08versions\x18\x01 \x03(\x0b\x32\x13.bible.BibleVersion\"\x1c\n\x0c\x42ibleVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\"0\n\rBibleBookList\x12\x1f\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x10.bible.BibleBook\"\x19\n\tBibleBook\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x10\x42ibleChapterList\x12\x10\n\x08\x63hapters\x18\x01 \x03(\x05\"d\n\x12\x42ibleVerseResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04\x62ook\x18\x02 \x01(\t\x12\x0f\n\x07\x63hapter\x18\x03 \x01(\x05\x12\r\n\x05verse\x18\x04 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\"B\n\x15\x43ompareVersesResponse\x12)\n\x06verses\x18\x01 \x03(\x0b\x32\x19.bible.BibleVerseResponse2\x81\x03\n\x0c\x42ibleService\x12\x42\n\x10GetBibleVersions\x12\x13.bible.EmptyRequest\x1a\x17.bible.BibleVersionList\"\x00\x12G\n\x11GetBooksInVersion\x12\x1a.bible.BibleVersionRequest\x1a\x14.bible.BibleBookList\"\x00\x12J\n\x11GetChaptersInBook\x12\x1a.bible.BibleChapterRequest\x1a\x17.bible.BibleChapterList\"\x00\x12J\n\x11GetVerseInChapter\x12\x18.bible.BibleVerseRequest\x1a\x19.bible.BibleVerseResponse\"\x00\x12L\n\rCompareVerses\x12\x1b.bible.CompareVersesRequest\x1a\x1c.bible.CompareVersesResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bible_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYREQUEST._serialized_start=30
  _EMPTYREQUEST._serialized_end=44
  _BIBLEVERSIONREQUEST._serialized_start=46
  _BIBLEVERSIONREQUEST._serialized_end=84
  _BIBLECHAPTERREQUEST._serialized_start=86
  _BIBLECHAPTERREQUEST._serialized_end=138
  _BIBLEVERSEREQUEST._serialized_start=140
  _BIBLEVERSEREQUEST._serialized_end=222
  _COMPAREVERSESREQUEST._serialized_start=224
  _COMPAREVERSESREQUEST._serialized_end=310
  _BIBLEVERSIONLIST._serialized_start=312
  _BIBLEVERSIONLIST._serialized_end=369
  _BIBLEVERSION._serialized_start=371
  _BIBLEVERSION._serialized_end=399
  _BIBLEBOOKLIST._serialized_start=401
  _BIBLEBOOKLIST._serialized_end=449
  _BIBLEBOOK._serialized_start=451
  _BIBLEBOOK._serialized_end=476
  _BIBLECHAPTERLIST._serialized_start=478
  _BIBLECHAPTERLIST._serialized_end=514
  _BIBLEVERSERESPONSE._serialized_start=516
  _BIBLEVERSERESPONSE._serialized_end=616
  _COMPAREVERSESRESPONSE._serialized_start=618
  _COMPAREVERSESRESPONSE._serialized_end=684
  _BIBLESERVICE._serialized_start=687
  _BIBLESERVICE._serialized_end=1072
# @@protoc_insertion_point(module_scope)