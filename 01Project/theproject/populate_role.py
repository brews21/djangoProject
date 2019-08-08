import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','theproject.settings')

import django
# Import settings
django.setup()

import random
from theapp.models import Account, AccountRole, Role
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_company = fakegen.company()
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        fake_date = fakegen.date()

        # Create new User Entry
        user = Account.objects.get_or_create(username=fake_name,
                                            password=fake_name,
                                            email=fake_email,
                                            created_on=fake_date,
                                            last_login=fake_date)[0]

        role = Role.objects.get_or_create(role_name=fake_company)[0]


def populateAccRole(N=5):
    for entry in range(N*2):
        temp = random.randint(1,N)
        value = random.randint(1,N)
        accID = Account.objects.get(user_id=value)
        roleID = Role.objects.get(role_id=temp)
        accRole = AccountRole.objects.get_or_create(user_id=accID.user_id,
                                                    role_id=roleID.role_id)



if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    n=5
    populate(n)
    populateAccRole(n)
    print('Populating Complete')
