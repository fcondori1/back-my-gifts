from django.db import models

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'users.User', related_name='gifts', on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

class Information(models.Model):
    title = models.CharField(max_length=100)
    gift = models.ForeignKey(
        Gift, on_delete=models.CASCADE, related_name='information')
    owner = models.ForeignKey(
        'users.User', related_name='information', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
