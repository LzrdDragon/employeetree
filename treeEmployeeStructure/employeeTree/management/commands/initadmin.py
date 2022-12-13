from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create a superuser if none exists or if you want to
    Example:
        manage.py initadmin --user=admin --password=password
    """

    def add_arguments(self, parser):
        parser.add_argument("--user", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--email", default="admin@example.com")
        parser.add_argument("--force", default=False)

    def handle(self, *args, **options):
        user = get_user_model()

        # if --force is not on and some superuser does already exist, do not create a new one
        if not options["force"] and user.objects.exists():
            return

        username = options["user"]
        password = options["password"]
        email = options["email"]

        user.objects.create_superuser(username=username, password=password, email=email)

        self.stdout.write(f'Local user "{username}" was created')
