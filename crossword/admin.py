from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Crossmap)
admin.site.register(models.Word)
admin.site.register(models.CrossmapResult)
admin.site.register(models.WordResult)