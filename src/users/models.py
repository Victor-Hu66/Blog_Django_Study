from django.db import models
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.author.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_path, default='indir.png')
    bio = models.TextField(blank=True)
    
    