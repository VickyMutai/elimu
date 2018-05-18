from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length =30)

class Chapters(models.Model):
    chapter_name = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject)

class Topics(models.Model):
    topic_name = models.CharField(max_length=60)
    chapter = models.ForeignKey(Chapters)
    subject = models.ForeignKey(Subject)

class Content(models.Model):
    notes = HTMLField()
    document = models.FileField(upload_to='multimedia/',null=True,blank=True)
    chapter = models.ForeignKey(Chapters)
    subject = models.ForeignKey(Subject)
    topics = models.ForeignKey(Topics)