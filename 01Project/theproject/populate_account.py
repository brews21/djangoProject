import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','theproject.settings')

import django
# Import settings
django.setup()

import random
from theapp.models import Account
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_date = fakegen.date()

        # password = models.CharField(max_length=128)
        # last_login = models.DateTimeField(blank=True, null=True)
        # is_superuser = models.BooleanField()
        # username = models.CharField(max_length=150)
        # first_name = models.CharField(max_length=30)
        # last_name = models.CharField(max_length=150)
        # email = models.CharField(max_length=254)
        # is_staff = models.BooleanField()
        # is_active = models.BooleanField()
        # date_joined = models.DateTimeField()

        # Create new User Entry
        user = Account.objects.get_or_create(username=fake_name,
                                            password=fake_name,
                                            email=fake_email,
                                            created_on=fake_date,
                                            last_login=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(1)
    print('Populating Complete')
