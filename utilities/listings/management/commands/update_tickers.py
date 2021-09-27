from django.core.management.base import BaseCommand, CommandError
from listings.jobs import update_tickers


class Command(BaseCommand):
    help = 'Updates the database of listed tickers with new listings.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        update_tickers()
