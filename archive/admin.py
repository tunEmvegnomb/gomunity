from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Archive)
admin.site.register(models.ArchiveAnswer)
admin.site.register(models.ArchiveCategory)
admin.site.register(models.ArchiveLike)
admin.site.register(models.ArchiveAnswerLike)
