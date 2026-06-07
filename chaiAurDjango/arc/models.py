from django.db import models
from django.utils import timezone

# Create your models here.

class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('PL', 'PLAIN'),
        ('GR', 'GINGER'),
        ('EL', 'ELAYCHI'),
        ('BL', 'BLACK')
    ]

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chaisImg/')
    price=models.IntegerField(default=90)
    date_added= models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')


    def __str__(self):
        return self.name


# After creating models we have to run command to make a migration--> python manage.py makemigrations arc
# After that command to migrate--> python manage.py migrate