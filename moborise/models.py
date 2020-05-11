from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save, post_delete, post_init
from django.dispatch import receiver
from django.conf import settings
import os
from Agent.models import Agentuploads

def user_directory_path(instance, filename, **kwargs):
    file_path = 'gallery/profile/{filename}'.format( filename=filename)
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return file_path

class UserType(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE,)
    About = models.CharField(max_length = 100, )
    phone = models.CharField(max_length = 100, )
    whatapp_number = models.CharField(max_length = 100, )
    Business_Name = models.CharField(max_length = 100, )
    Employment_status = models.CharField(max_length = 100, )
    Facebook_link = models.CharField(max_length = 100, )
    Successfully_trans = models.IntegerField(default=0,)
    role = models.CharField(max_length = 100, )
    img = models.FileField(upload_to = "gallery/profile/")
    # url = models.URLField("Website", blank=True)
    

    def __unicode__(self):
        return self.role

    def save(self, *args, **kwargs):
        if not self.role:
            self.role = 'U'
        return super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='TheUser', on_delete=models.CASCADE)
    text = models.TextField()
    post_id = models.IntegerField(default='0')
    Username = models.CharField(max_length = 100, )
    time = models.CharField(max_length = 100, )
    created_date = models.DateTimeField(auto_now_add=True)
    to = models.CharField(max_length = 100, )
    

    def __str__(self):
        return self.text

class Reply(models.Model):
    rep = models.ForeignKey(Comment, related_name="reply", on_delete=models.CASCADE)
    reply = models.TextField()
    Username = models.CharField(max_length = 100, )
    post_id = models.IntegerField(default='0')
    time = models.CharField(max_length = 100, )
    created_date = models.DateTimeField(auto_now_add=True)
    to = models.CharField(max_length = 100, )
    

    def __str__(self):
        return self.text

class ProfilPicx(models.Model):
    user = models.OneToOneField(User, related_name="profilePicx", on_delete=models.CASCADE,)
    
    img = models.FileField(upload_to = '', null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.img:
            self.img = 'U'
        return super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if os.path.join(settings.MEDIA_ROOT, self.img.name) == os.path.join(settings.MEDIA_ROOT, 'U'):
            print('first time')
        else:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.img.name))
        
    # def save(self, *args, **kwargs):
    #     if not self.img:
    #         self.img = 'U'
    #     return super().save(*args, **kwargs)
    


    
# Create your models here.
class uploads(models.Model):
    property_image = models.CharField(max_length = 100, blank=True)
    property_name = models.CharField(max_length = 100, blank=True)
    address  = models.CharField(max_length = 100, blank=True)
    location = models.CharField(max_length = 100)
    agent = models.CharField(max_length = 100)





class Agent(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length = 100, null=True, blank=True)
    

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        UserType.objects.create(user=instance)
        ProfilPicx.objects.create(user=instance)
        
