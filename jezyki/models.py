from django.db import models
from django.utils import timezone


class LanguageManager(models.Manager):
    def get_by_natural_key(self, language):
        return self.get(language=language)


class Language(models.Model):
    language = models.CharField(max_length=32)

    objects = LanguageManager()

    def __str__(self):
        return self.language

    def natural_key(self):
        return (self.language,)


class Article(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    link = models.URLField(blank=True)  
    language = models.ForeignKey(Language, related_name='articles', on_delete=models.CASCADE)
    date = models.DateTimeField("Date published", default=timezone.now)
    # author = models.CharField(max_length=32)

    def __str__(self):
        return f"Article ({self.language}) {self.title} published at {self.date}."


