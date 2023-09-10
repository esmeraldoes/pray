from rest_framework import serializers

class EmptySerializer(serializers.Serializer):
    pass

class GetBooksRequestSerializer(serializers.Serializer):
    version = serializers.CharField()

class GetChaptersRequestSerializer(serializers.Serializer):
    version = serializers.CharField()
    book = serializers.CharField()

class GetVersesRequestSerializer(serializers.Serializer):
    version = serializers.CharField()
    book = serializers.CharField()
    chapter = serializers.IntegerField()

class GetVerseRequestSerializer(serializers.Serializer):
    version = serializers.CharField()
    book = serializers.CharField()
    chapter = serializers.IntegerField()
    verse = serializers.IntegerField()

class BibleVersionListSerializer(serializers.Serializer):
    versions = serializers.ListField(child=serializers.CharField())

# class BibleBookListSerializer(serializers.Serializer):
#     books = serializers.ListField(child=serializers.CharField())
class BibleBookListSerializer(serializers.Serializer):
    Old_Testament = serializers.ListField(child=serializers.CharField())
    New_Testament = serializers.ListField(child=serializers.CharField())

class BibleChapterListSerializer(serializers.Serializer):
    chapters = serializers.ListField(child=serializers.IntegerField())

# class BibleVerseSerializer(serializers.Serializer):
#     content = serializers.CharField()



class BibleVerseSerializer(serializers.Serializer):
    content = serializers.CharField()

    def to_representation(self, instance):
        """
        Override the to_representation method to handle the "number" field.
        """
        data = super().to_representation(instance)
        
        # Check if the "number" field is present in the instance
        if 'number' in instance:
            data['number'] = instance['number']
        
        return data



