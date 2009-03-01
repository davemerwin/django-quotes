from django.db import models

class Quote(models.Model):
    slug = models.SlugField(max_length=255, unique=True, help_text='A shortname for the quote.')
    author = models.CharField(blank=True, max_length=255, help_text='The quote\'s author')
    circ = models.CharField(blank=True, max_length=100, help_text="When was the quote created?")
    quote = models.TextField()

    class Meta:
        verbose_name_plural = 'Quotes'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Quote, self).save()