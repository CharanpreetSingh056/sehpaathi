from django.contrib import admin
from .models import general_questions_db,answers_db
# Register your models here.
admin.site.register(general_questions_db)
admin.site.register(answers_db)