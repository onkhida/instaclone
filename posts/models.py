from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Post(models.Model):
    # A table for items posted by a user
    # Fields:
    #  - user: the user who posted this
    #  - id: unique UUID url for post
    #  - date: the date and time posted
    #  - image: image uploaded by a user
    #  - caption: optional text caption for image
    #  - location: just a text representation of the date
    #  - likes: the number of likes the image has

    user = models.ForeignKey(User,
                             related_name='posts',
                             on_delete=models.CASCADE)
    
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, 
                          editable=False)
    date = models.DateTimeField(auto_now_add=True,
                                db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    caption = models.TextField()
    location = models.CharField(max_length=250)
    likes = models.ManyToManyField(User,
                                   related_name='posts_liked',
                                   blank=True)

    def __str__(self):
        return '{}: {}'.format(self.user.username, self.caption)


class Comment(models.Model):
    # One to many field to a specific post
    # Fields:
    # - post: the post the comment is under
    # - user: who commented what
    # - text: the text that was commented
    # - date: the date it was written

    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)

    user = models.ForeignKey(User,
                             related_name='comments',
                             on_delete=models.CASCADE)

    text = models.TextField()

    date = models.DateTimeField(auto_now_add=True,
                                db_index=True)
    def __str__(self):
        return '{}: {}'.format(self.user.username, self.text)