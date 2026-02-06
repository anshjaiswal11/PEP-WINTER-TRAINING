from django.contrib import admin

# Register your models here.
from .models import LoginUser, user, formModel
admin.site.register(user)

admin.site.register(formModel)

admin.site.register(LoginUser)