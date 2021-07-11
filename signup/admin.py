from django.contrib import admin
from .models import user_data
from .models import User,user_validation,user_forgot_password
from rest_framework_simplejwt.token_blacklist import models
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin

# Register your models here.
admin.site.register(user_data)
admin.site.register(User)
admin.site.register(user_validation)
admin.site.register(user_forgot_password)

class NewOutstandingTokenAdmin(OutstandingTokenAdmin): #model to delete users even if they have a token 

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(models.OutstandingToken)
admin.site.register(models.OutstandingToken, NewOutstandingTokenAdmin)
