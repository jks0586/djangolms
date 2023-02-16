from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS =(
    (0,'Draft'),
    (1,'Publish'),
)

class Ocrimage(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.FileField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title