from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, email, name, employee_id, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        if not name:
            raise ValueError("The Name field is required.")
        if not employee_id:
            raise ValueError("The Employee ID is required.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, employee_id=employee_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email, name, employee_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", False)
        return self.create_user(email, name, employee_id, password, **extra_fields)

    def create_superuser(self, email, name, employee_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, employee_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    employee_id = models.CharField(max_length=5, unique=True, validators=[
            RegexValidator(r'^\d{3,5}$', 'Employee ID must be between 3 and 5 digits.')])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "employee_id"]

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
