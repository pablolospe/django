from django.db import models
from django.db.models import Model

# Create your models here.

class User(Model):
    name = models.CharField(max_length=100) 
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "cryptoplus"

    def __str__(self):
        return f"Usuario {self.name} {self.lastname}, email: {self.email}"
    
    def get_fields(self):
        return [
            (field.verbose_name, filter.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]

# registrar la app en admin.py