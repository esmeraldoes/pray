# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bible_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x62ible_service.proto\x12\x07\x64\x62ibles\x1a\x1bgoogle/protobuf/empty.proto\"\x1c\n\x0c\x42ibleVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\")\n\tBibleBook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\"\x1e\n\x0c\x42ibleChapter\x12\x0e\n\x06number\x18\x01 \x01(\x05\"-\n\nBibleVerse\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"+\n\x13\x42ibleVersionRequest\x12\x14\n\x0cversion_name\x18\x01 \x01(\t\";\n\x10\x42ibleVersionList\x12\'\n\x08versions\x18\x01 \x03(\x0b\x32\x15.dbibles.BibleVersion\"(\n\x10\x42ibleBookRequest\x12\x14\n\x0cversion_name\x18\x01 \x01(\t\"2\n\rBibleBookList\x12!\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x12.dbibles.BibleBook\">\n\x13\x42ibleChapterRequest\x12\x14\n\x0cversion_name\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\";\n\x10\x42ibleChapterList\x12\'\n\x08\x63hapters\x18\x01 \x03(\x0b\x32\x15.dbibles.BibleChapter\"j\n\x11\x42ibleVerseRequest\x12\x14\n\x0cversion_name\x18\x01 \x01(\t\x12\x11\n\tbook_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63hapter_number\x18\x03 \x01(\x05\x12\x14\n\x0cverse_number\x18\x04 \x01(\x05\"%\n\x12\x42ibleVerseResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t2\xb0\x02\n\x0c\x42ibleService\x12\x45\n\x10GetBibleVersions\x12\x16.google.protobuf.Empty\x1a\x19.dbibles.BibleVersionList\x12I\n\x11GetBooksInVersion\x12\x1c.dbibles.BibleVersionRequest\x1a\x16.dbibles.BibleBookList\x12I\n\x11GetChaptersInBook\x12\x19.dbibles.BibleBookRequest\x1a\x19.dbibles.BibleChapterList\x12\x43\n\x08GetVerse\x12\x1a.dbibles.BibleVerseRequest\x1a\x1b.dbibles.BibleVerseResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bible_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BIBLEVERSION']._serialized_start=61
  _globals['_BIBLEVERSION']._serialized_end=89
  _globals['_BIBLEBOOK']._serialized_start=91
  _globals['_BIBLEBOOK']._serialized_end=132
  _globals['_BIBLECHAPTER']._serialized_start=134
  _globals['_BIBLECHAPTER']._serialized_end=164
  _globals['_BIBLEVERSE']._serialized_start=166
  _globals['_BIBLEVERSE']._serialized_end=211
  _globals['_BIBLEVERSIONREQUEST']._serialized_start=213
  _globals['_BIBLEVERSIONREQUEST']._serialized_end=256
  _globals['_BIBLEVERSIONLIST']._serialized_start=258
  _globals['_BIBLEVERSIONLIST']._serialized_end=317
  _globals['_BIBLEBOOKREQUEST']._serialized_start=319
  _globals['_BIBLEBOOKREQUEST']._serialized_end=359
  _globals['_BIBLEBOOKLIST']._serialized_start=361
  _globals['_BIBLEBOOKLIST']._serialized_end=411
  _globals['_BIBLECHAPTERREQUEST']._serialized_start=413
  _globals['_BIBLECHAPTERREQUEST']._serialized_end=475
  _globals['_BIBLECHAPTERLIST']._serialized_start=477
  _globals['_BIBLECHAPTERLIST']._serialized_end=536
  _globals['_BIBLEVERSEREQUEST']._serialized_start=538
  _globals['_BIBLEVERSEREQUEST']._serialized_end=644
  _globals['_BIBLEVERSERESPONSE']._serialized_start=646
  _globals['_BIBLEVERSERESPONSE']._serialized_end=683
  _globals['_BIBLESERVICE']._serialized_start=686
  _globals['_BIBLESERVICE']._serialized_end=990
# @@protoc_insertion_point(module_scope)