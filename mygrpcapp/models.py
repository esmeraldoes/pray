from django.db import models

# Create your models here.

class BibleVersion(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    #managed stops it from migrating during migrations
    # class Meta:
    #     managed = False
        
class BibleBook(models.Model):
    version = models.ForeignKey(BibleVersion, on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.version})"
    
    
class BibleChapter(models.Model):
    book = models.ForeignKey(BibleBook, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.book}: Chapter {self.number}"



class BibleVerse(models.Model):
    # version = models.ForeignKey(BibleVersion, on_delete=models.CASCADE)
    chapter = models.ForeignKey(BibleChapter, on_delete=models.CASCADE)
    # book = models.ForeignKey(BibleBook, on_delete=models.CASCADE)
    number = models.IntegerField()
    content = models.TextField()
    
    def __str__(self):
        return f"{self.chapter}: Verse {self.number}"
