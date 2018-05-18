from django.db import models

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