from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='Books.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=250, blank=True, null=True)
    genre = models.CharField(max_length=250, blank=True, null=True)
    bday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'

    # def save(self, *args, **kwargs):
    #     self.instance.user = self.user
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    

