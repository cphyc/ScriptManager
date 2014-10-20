from django.db import models

# Create your models here.

class Langage(models.Model):
    """ Describes a langage """
    langage = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return self.langage

class Folder(models.Model):
    """ Describes a folder to sort many differents scripts. """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Script(models.Model):
    """ Describes a script (name + langage + content)"""
    publication_date = models.DateTimeField(auto_now_add=True,)
    last_update = models.DateTimeField()
    folder = models.ForeignKey(Folder)
    title = models.CharField(max_length=100,)
    code = models.TextField()
    langage = models.ForeignKey(Langage)

    def __unicode__(self):
        return self.title
