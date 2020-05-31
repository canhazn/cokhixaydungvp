from django.db import models

# Create your models here.

def path_file_name(instance, filename):    
    return '/'.join(filter(None, ('service', instance.slug, filename)))

class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField()
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to = path_file_name, null=True, blank=True)

    def __str__(self):
        return self.title
