from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Campus(models.Model):
    name = models.CharField(max_length=128)
    name_ch = models.CharField(max_length=100, blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
	
    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Campus, self).save(*args, **kwargs)

    def __unicode__(self):      
        return self.name


class Subject(models.Model):
    title = models.CharField(max_length=128)
    title_ch = models.CharField(max_length=100, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    campus = models.ForeignKey(Campus)
	
    def save(self, *args, **kwargs):
                self.slug = slugify(self.title)
                super(Subject, self).save(*args, **kwargs)
    def __unicode__(self):      
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    name_ch = models.CharField(max_length=100, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
	
    subject = models.ForeignKey(Subject)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  
        return self.name