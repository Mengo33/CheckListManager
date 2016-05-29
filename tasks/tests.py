from tasks import models
from django.test import TestCase


class SimpleTestCase(TestCase):
    def test_add2db(self):
        for i in range(20):
            o = models.Task()
            o.title = "Car #{} for sale..".format(i)
            o.description = "Awesome car!!!"
            o.posted_by = "Meni"
            o.contact_email = "menig@superbootcamp.tech"
            o.price = i * (i + 1)
            o.full_clean()
            o.save()
        self.assertEquals(models.Task.objects.count(), 20)


