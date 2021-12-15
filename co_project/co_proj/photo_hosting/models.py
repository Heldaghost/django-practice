from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(max_length=500, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Time updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
    collection = models.ForeignKey('Collections', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Collection')
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, verbose_name='Author')
    # tags = models.ManyToManyField('Tags', db_table='tags_process', blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User related')
    description = models.TextField(max_length=100, blank=True, verbose_name='Description')
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True, verbose_name='Avatar')
    birth_date = models.DateTimeField(blank=True, null=True, verbose_name='Birth date')

    def get_absolute_url(self):
        return reverse('profile', kwargs={'user_slug': self.user.username})

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


@receiver(post_save, sender=User)
def save_or_create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, )
    else:
        try:
            instance.userprofile.save()
        except ObjectDoesNotExist:
            UserProfile.objects.create(user=instance)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Post')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Collections(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    description = models.TextField(max_length=100, verbose_name='Description')
    avatar = models.ImageField(upload_to='col_avatars/%Y/%m/%d/', verbose_name='Avatar')
    user_id = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'


class Comments(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Author')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='To post')
    content = models.TextField(max_length=100, blank=False, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']


class FavCollections(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    col = models.ForeignKey(Collections, on_delete=models.CASCADE, verbose_name='Collection')

    class Meta:
        verbose_name = 'Favourites'
        verbose_name_plural = 'Favourites'

#
# class Tags(models.Model):
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
