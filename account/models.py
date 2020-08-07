from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Created a model tying directly to the built in django User Model.
    # Contains extra information on the User that will make up the profile page.
    #
    # Fields:
    # - user: The single user the profile corresponds with
    # - bio: Text field bio
    # - website: optional URL to the bio
    # - gender: text field for whatever gender the user is
    # - profile_picture: profile picture for user
    # - followers: the people following this profile 
    # - following: the people that this profile is following

    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                related_name='profiles')
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    gender = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', default='default.png')
    followers = models.ManyToManyField(User,
                                       blank=True,
                                       null=True,
                                       related_name='followers')
    following = models.ManyToManyField(User,
                                       blank=True,
                                       null=True,
                                       related_name='following')

    def __str__(self):
        return "{}'s Profile".format(self.user.username)


