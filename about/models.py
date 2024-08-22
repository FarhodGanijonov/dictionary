from django.db import models
from ckeditor.fields import RichTextField


class ScientificTeam(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=200, blank=True, null=True)
    academic_level = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=17, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    admission_day = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.fullname


class Scientists(models.Model):
    fullname = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class Expressions(models.Model):
    express = models.TextField()

    def __str__(self):
        return self.express


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title

class Provensiya(models.Model):
    provensiya = models.CharField(max_length=200)

    def __str__(self):
        return self.provensiya


class Dictionary(models.Model):
    provensiya = models.ForeignKey(Provensiya, on_delete=models.CASCADE)
    grammatical = RichTextField(blank=True, null=True)
    lexical = models.CharField(max_length=200)
    comment = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.lexical

class Sentences(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    sentence = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.sentence[:30]


