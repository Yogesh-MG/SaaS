from django.db import models

# Create your models here.


class PageVisit(models.Model):
    no_visit = models.TextField()
    date_area  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.no_visit} {self.id}"