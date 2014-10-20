from django.contrib import admin
from scripts.models import *

# Register your models here.
class ScriptAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder', 'langage', 'last_update')
    list_filter = ['publication_date', 'langage']

admin.site.register(Script, ScriptAdmin)
admin.site.register(Langage)
admin.site.register(Folder)
