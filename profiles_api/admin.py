from django.contrib import admin

from profiles_api import models
# Register your models here.

admin.site.register(models.UserProfile)  # added the UserProfile model to admin interface
admin.site.register(models.ProfileFeedItem)
