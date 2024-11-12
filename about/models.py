from django.db import models
from rest_framework.exceptions import ValidationError


class ScientificTeam(models.Model):
    fullname = models.CharField(max_length=100)
    workplace = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    academic_level = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=17, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    admission_day = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.fullname


class Scientists(models.Model):
    fullname = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title


class Provensiya(models.Model):
    provensiya = models.CharField(max_length=200)

    def __str__(self):
        return self.provensiya


class Dictionary(models.Model):
    provensiya = models.ForeignKey(Provensiya, on_delete=models.CASCADE)
    grammatical = models.TextField(blank=True, null=True)
    lexical = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.lexical


class Sentences(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='senten')
    sentence = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sentence[:30]


class AdminContact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    location = models.TextField()
    telegram = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()

    def save(self, *args, **kwargs):
        if AdminContact.objects.exists() and not self.pk:
            raise ValidationError("Faqat bitta AdminContact obyektiga ruxsat berilgan.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    comment = models.TextField(max_length=200)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.phone


class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='sliders/', blank=True, null=True)

    def __str__(self):
        return self.title


class Text(models.Model):
    provensiya = models.ForeignKey(Provensiya, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)


class Category(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Addition(models.Model):
    adition = models.CharField(max_length=200)
    categ = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='additions')

    def __str__(self):
        return self.adition


class UsefulSites(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.URLField()

    def __str__(self):
        return self.title


