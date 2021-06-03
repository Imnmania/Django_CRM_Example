from django.db import models
from django.contrib.auth.models import AbstractUser

# User = get_user_model()

class User(AbstractUser):
    pass

class Lead(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)
    # agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT, default=)
    
    
    
    # SOURCE_CHOICES = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('NewsLetter', 'NewsLetter'),
        
    # )
    
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    
    # ''' OPTIONAL FIELDS '''
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=20)
    # last_name = models.CharField(max_length=20)
    