from django.db import models

class Student(models.Model):
    # Name of the student
    name = models.CharField(max_length=100)
    
    # Unique Control Number (assuming it acts as a unique identifier)
    ucn = models.CharField(max_length=20, unique=True)
    
    # Department name
    dept = models.CharField(max_length=50)
    
    # Email address with built-in validation
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.ucn})"
