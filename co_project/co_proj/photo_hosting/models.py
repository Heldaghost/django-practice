from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_visible = models.BooleanField(default=False)
    collection = models.ForeignKey('Collections', on_delete=models.PROTECT, blank=True, null=True)
    user = models.ForeignKey('UserProfile', on_delete=models.PROTECT, blank=True)
    # tags = models.ManyToManyField('Tags', db_table='tags_process', blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True)
    birth_date = models.DateTimeField(blank=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_slug': self.user.username})

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.userprofile.save()
        except ObjectDoesNotExist:
            UserProfile.objects.create(user=instance)


class Likes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Collections(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    avatar = models.ImageField(upload_to='col_avatars/%Y/%m/%d/')
    user_id = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField(max_length=100)

#
# class Tags(models.Model):
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
