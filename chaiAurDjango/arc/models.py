from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



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


# relationship --->

# one to many


class chaiReview(models.Model):
    chai= models.ForeignKey(chaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user= models.ForeignKey(chaiVarity, on_delete=models.CASCADE)
    ratings= models.IntegerField()
    comments= models.TextField()
    date_added= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    

# many to many--->

class store(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    chai_varieties= models.ManyToManyField(chaiVarity, related_name='stores')
    

    def __str__(self):
        return self.name
    

# one to one --->

class chaiCerificate(models.Model):
    chai= models.OneToOneField(chaiVarity, related_name= 'certificate', on_delete=models.CASCADE)
    certificateNum= models.CharField(  max_length=100)
    issuedDate= models.DateTimeField(default=timezone.now)
    valid_till= models.DateTimeField

    def __str__(self):
        return f'Certificate for{self.chai}'
    