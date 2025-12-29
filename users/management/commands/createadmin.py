from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.create(
            email='testadmin@mail.ru'
        )

        user.set_password('1234')

        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'Success created admin user with email {user.email}'))
