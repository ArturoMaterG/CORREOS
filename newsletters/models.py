from django.db import models

class NewslettersUser(models.Model):
    email=models.EmailField(null=False, unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email


class Newsletter(models.Model):
    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body=models.TimeField(blank=True, null=True)
    email=models.ManyToManyField(NewslettersUser)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
