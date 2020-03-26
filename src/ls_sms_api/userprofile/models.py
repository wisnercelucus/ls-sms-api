from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):

    def creat_user(self, email, name, password=None):
        """Create a new user profile object."""
        if not email:
            raise ValueError("A user must have a valid email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        user = self.creat_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)






class UserProfile(AbstractBaseUser, PermissionsMixin):
    """This class represent represents a user profile inside of the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Use to get a User's fullname."""

        return self.name

    def get_short_name(self):
        """Use to get a user's short nmae."""

        return self.name

    def __str__(self):
        """Convert a user object to a string."""

        return self.email
