from django.db import models

# Create your models here.
class Participant(models.Model):
    # participant form fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=150)

    class Meta:
        db_table = "participants"