from django.db import models


class EmailList(models.Model):
    email = models.EmailField(unique=True)