from django.contrib import admin
from .models import rejection_reasons_db,rejection_reasons_comments_db
# Register your models here.
admin.site.register(rejection_reasons_comments_db)
admin.site.register(rejection_reasons_db)
