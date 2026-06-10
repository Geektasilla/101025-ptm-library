import re

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_phone_number(value: str) -> None:
    if not re.fullmatch(
            pattern=r"^\+?\d{1,4}?[\s-]?(?:\(?\d{2,5}\)?[\s-]?)?\d{2,5}[\s-]?\d{2,5}[\s-]?\d{0,5}$",
            string=value
    ):
        raise ValidationError(
            "Invalid phone number. Please, try again."
        )


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        admin = "admin", "Admin"
        moderator = "moderator", "Moderator"
        lib_member = "lib_member", "Library Member"

    class Gender(models.TextChoices):
        male = "male", "Male"
        female = "female", "Female"
        other = "other", "Other"

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(
        max_length=25,
        unique=True,
        null=True,
        blank=True,
        validators=[
            validate_phone_number,
        ]
    )
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=Role)
    gender = models.CharField(max_length=10, choices=Gender)
    age = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(10),
            MaxValueValidator(90)
        ]
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role", "gender"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Membership(models.Model):
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_records"
    )
    library = models.ForeignKey(
        to='Library',
        on_delete=models.CASCADE,
        related_name="membership_records"
    )
    joined_at = models.DateField(
        default=timezone.now
    )
