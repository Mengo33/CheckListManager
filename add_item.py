import os
from tasks import models
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "check_list_manager.settings")

setup()


for i in range(20):
    o = models.Task()
    o.title = "Car #{} for sale..".format(i)
    o.description = "Awesome car!!!"
    o.posted_by = "Meni"
    o.contact_email = "menig@superbootcamp.tech"
    o.full_clean()
    o.save()

    print(o.id)

