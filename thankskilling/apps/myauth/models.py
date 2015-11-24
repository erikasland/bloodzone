from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateField()
    class Meta:
        db_table = 'users'