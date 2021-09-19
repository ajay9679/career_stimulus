from django.db import models

class NewsletterUser(models.Model):
    name        =       models.CharField(max_length=50, blank=False)
    email       =       models.EmailField(blank=False)
    date_added  =       models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email














