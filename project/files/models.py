from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Files(models.Model):
    name = models.CharField(max_length=100)
    docfile = models.FileField(blank=True)
    code_md5 = models.CharField(max_length=100)
    code_sha256 = models.CharField(max_length=100)

    def __str__(self):
        return self.name