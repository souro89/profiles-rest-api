from django.contrib import admin

#Import the model to register with Django admin
from profiles_api import models

# Register your models here.


admin.site.register(models.UserProfile)