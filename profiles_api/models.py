from django.db import models
#To overwrite the default user  model provided by django below 2 imports are necessary
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#Required for Usermanager class
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create for user profiles"""
        if not email:
            raise ValueError('User must have email address')
        
        email = self.normalize_email(email)
        user = self.model(email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user=self.create_user(email, name ,password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

# Create your models here.

#Need to inherit from the above imports
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Django needs a custom model manager to create and manage 
    # users model , this class needs to be created
    objects = UserProfileManager()

    #to overwrite the default USERNAME_FIELD to email
    USERNAME_FIELD = 'email'
    #To mention any required fields
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email 