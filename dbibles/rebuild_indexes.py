from django.core.management.base import BaseCommand
from elasticsearch_dsl import Index
from dbibles.search_indexes import BibleVerseIndex


class Command(BaseCommand):
    help = 'Rebuilds the Elasticsearch indexes'

    def handle(self, *args, **options):
        # Delete the existing index
        index = Index(BibleVerseIndex._doc_type.index)
        index.delete(ignore=404)

        # Create a new index and rebuild it
        index.create()
        BibleVerseIndex.init()
        self.stdout.write(self.style.SUCCESS('Elasticsearch indexes have been rebuilt successfully.'))
