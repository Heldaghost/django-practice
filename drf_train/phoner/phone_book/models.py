from django.db import models


class PhoneNote(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    is_friend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta():
        ordering = ['-created_at']