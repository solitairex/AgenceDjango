from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Hotel(models.Model):
    HOTEL_CHOICES = [
        ('Sol Oasis', 'Sol Oasis'),
        ('Movenpick', 'Movenpick'),
        ('Riad la Parenthese', 'Riad la Parenthese'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, choices=HOTEL_CHOICES)
    number_of_persons = models.PositiveIntegerField()
    reservation_date = models.DateField()

    def __str__(self):
        return f"Reservation ID: {self.id}, Name: {self.name}"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Adresse Email requis")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

