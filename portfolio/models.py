from django.db import models
from django.utils.text import slugify
# Create your models here.

def project_image_url(instance,filename):
    return 'projects/{0}/{1}'.format(instance.title,filename)


class Technologies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=project_image_url)
    gitlink = models.URLField()
    technologies = models.ManyToManyField(Technologies)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)


    def save(self,*args,**kwargs):

        count = Projects.objects.all().count()
        count+=1

        self.slug = slugify(self.title + '-' + str(count))

        super().save(*args,**kwargs)


    def __str__(self):
        return self.title    