from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Comment #{}'.format(self.id)
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField()
    document = models.FileField(upload_to='uploads/contact')