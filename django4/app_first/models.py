from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    content = models.TextField()
    cover = models.FileField(null=True, blank=True, upload_to='media/')
    create_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['create_at']

class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

class Tag(models.Model):
    address = models.CharField(max_length=200, blank=True)

"""

pf = PostForm()
pf.is_valid
False

dir(pf)
is_valid, initial..

pf = PostForm(name=bek, content=content1)

pf.is_valid()
True
dir(pf)
is_valid, initial, cleaned_data




"""

