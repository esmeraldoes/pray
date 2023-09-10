









from rest_framework import serializers
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse














from rest_framework import serializers
from .models import BibleVersion, BibleBook, BibleChapter, BibleVerse

class BibleVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleVersion
        fields = ('id', 'name')

# class BibleChapterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleChapter
#         fields = ('number',)


class BibleChapterSerializer(serializers.Serializer):
    number = serializers.IntegerField()  # This field represents the chapter number

    def to_representation(self, instance):
        return {'number': instance}  # Serialize the chapter number


class BibleVerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleVerse
        fields = ('number', 'content')

class BibleBookSerializer(serializers.ModelSerializer):
    chapters = BibleChapterSerializer(many=True, read_only=True)
    verses = serializers.SerializerMethodField()

    def get_verses(self, obj):
        # Retrieve the verses for the book as a list of dictionaries
        verses = BibleVerse.objects.filter(chapter__book=obj)
        serialized_verses = BibleVerseSerializer(verses, many=True).data
        return serialized_verses

    class Meta:
        model = BibleBook
        fields = ('id', 'version', 'number', 'name', 'chapters', 'verses')





































# class BibleVersionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleVersion
#         fields = ('id', 'name')

# class BibleChapterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleChapter
#         fields = ('number',)

# class BibleVerseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleVerse
#         fields = ('number', 'content')

# class BibleBookSerializer(serializers.ModelSerializer):
#     chapters = BibleChapterSerializer(many=True, read_only=True)
#     verses = serializers.SerializerMethodField()

#     def get_verses(self, obj):
#         return BibleVerse.objects.filter(chapter__book=obj).values_list('number', flat=True)

#     class Meta:
#         model = BibleBook
#         fields = ('id', 'version', 'number', 'name', 'chapters', 'verses')




































# from rest_framework import serializers
# from .models import BibleBook, BibleVersion, BibleChapter, BibleVerse
# # from .models import BibleVersion

# class BibleVerseSerializer(serializers.ModelSerializer):
#     version_name = serializers.CharField(source='chapter.book.version.name', read_only=True)
#     book_name = serializers.CharField(source='chapter.book.name', read_only=True)
#     chapter_number = serializers.IntegerField(source='chapter.number', read_only=True)

#     class Meta:
#         model = BibleVerse
#         fields = ['version_name', 'book_name', 'chapter_number', 'number', 'content']

# # class BibleVerseSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = BibleVerse
# #         fields = '__all__'



# class BibleChapterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleChapter
#         fields = '__all__'

#         # fields = ['id', 'book', 'number']
#         # fields = ['id', 'number', 'text']

# # class BibleChapterSerializer(serializers.ModelSerializer):
# #     # verses = BibleVerseSerializer(many=True)

# #     class Meta:
# #         model = BibleChapter
# #         fields = '__all__'

# # class BibleBookSerializer(serializers.ModelSerializer):
# #     chapters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

# #     # chapters = BibleChapterSerializer(many=True)

# #     class Meta:
# #         model = BibleBook
# #         fields = '__all__'
# from rest_framework import viewsets, serializers
# from .models import BibleVersion

# class BibleVersionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleVersion
#         fields = '__all__'

# class BibleVersionViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = BibleVersionSerializer
#     queryset = BibleVersion.objects.all()


# # class BibleBookSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = BibleBook
# #         fields = ('name',)

# # class VerseComparisonSerializer(serializers.Serializer):
# #     versions = serializers.ListField(child=serializers.CharField())
# #     chapter = serializers.IntegerField()
# #     verse = serializers.IntegerField()


# class VersionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BibleVersion
#         fields = ['id', 'name']
