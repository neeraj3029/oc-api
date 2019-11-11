from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=3000)
    cuser = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        # Add other status choices if required
        choices = [("submitted", 'submitted'), 
                        ("under review", "under review"), 
                            ("resolved", "resolved") ],
        max_length=20
    )
    
    def __str__(self):
        return self.title
