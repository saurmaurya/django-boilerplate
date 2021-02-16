from pathlib import Path
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Rename a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help='The new Django project')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # bit of logic to rename the project
        files_to_rename = ['myproject/settings/base.py',
                           'myproject/wsgi.py', 'manage.py']
        folders_to_rename = Path(__file__).resolve(
        ).parent.parent.parent.parent / 'myproject'
        print(folders_to_rename)

        for f in files_to_rename:
            with open(Path(__file__).resolve(
            ).parent.parent.parent.parent / f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('myproject', new_project_name)

            with open(Path(__file__).resolve(
            ).parent.parent.parent.parent / f, 'w') as file:
                file.write(filedata)

        Path.rename(folders_to_rename, Path(__file__).resolve(
        ).parent.parent.parent.parent / new_project_name)

        self.stdout.write(self.style.SUCCESS(
            'Project has been renamed to %s' % new_project_name))
