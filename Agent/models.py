from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver

#from rest_framework.authtoken.models import Token 
import os




 

# Create your models here.


def user_directory_path(instance, filename, **kwargs):
    file_path = 'gallery/{username}/{filename}'.format( username = str(instance.author.username), filename=filename)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return file_path


class Agentuploads(models.Model):
    file = models.FileField(upload_to=user_directory_path, null=False, blank=False)
    
    filename = models.CharField(max_length = 100, blank=True)
    username = models.CharField(max_length = 100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False, blank=False)
    property_Name = models.CharField(max_length = 100)
    property_Address = models.CharField(max_length = 100)
    property_Location = models.CharField(max_length = 100)
    property_Description = models.CharField(max_length = 100)
    property_Type = models.CharField(max_length = 100)
    
    price = models.IntegerField(default=0)
    verify = models.TextField(default='Not verified' ,max_length = 100)

    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length = 150, unique=False)
  

    def __unicode__(self):
        return '%s' % (self.file.name)

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        if self.uploadsfile:
            self.uploadsfile.delete()
        Agentuploads.delete()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.property_Description, allow_unicode=True)
        super(Agentuploads, self).save(*args, **kwargs)


class uploadsfile(models.Model):
    post = models.ForeignKey(Agentuploads, related_name="picture", on_delete=models.CASCADE,)
    file = models.FileField(upload_to='gallery/', null=True, blank=True)
   


# @receiver(post_save, sender= settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)



# Create your models here.
