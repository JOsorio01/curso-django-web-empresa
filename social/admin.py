from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name', 'created_at', 'updated_at')
        else:
            return ('created_at', 'updated_at')

admin.site.register(Link, LinkAdmin)
