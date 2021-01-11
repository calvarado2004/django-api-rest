from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Comment #{}'.format(self.id)
    
class TypeContact(models.Model):
    
    TYPE = (
        (1,"Business"),
        (2,"School"),
        (3,"Club"),
        (4,"Work")
    )
    name = models.CharField(max_length=50, choices=TYPE, default=1)
    
    def __str__(self):
        return self.name
class Contact(models.Model):
    
    GENDER = ( ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non binary'))
    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    vgender = models.CharField(max_length=15, choices=GENDER, default='M')
    document = models.FileField(upload_to='uploads/contact',default='',null=True)
    type_contact = models.ForeignKey(TypeContact, on_delete=models.CASCADE, default=1)
