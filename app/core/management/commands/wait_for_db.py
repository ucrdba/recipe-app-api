"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        """Entry point for command."""
        pass
        self.stdout.write("Waiting for database...")
        # Here you would typically check the database connection
        # For example, using Django's database connection check:
        from django.db import connections
        from django.db.utils import OperationalError
        import time

        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))