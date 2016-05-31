from django.db import models

# ORM - Object Relational Mapper


class Task(models.Model):
    class Status:
        UNDONE = 1
        DONE = 2

        choices = (
            (UNDONE, 'Undone'),
            (DONE, 'Done'),
        )

    posted_at = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=Status.choices, default=Status.UNDONE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    start_time = models.DateTimeField(null=True, blank=True)
    dead_line_time = models.DateTimeField(null=True, blank=True)

    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)



