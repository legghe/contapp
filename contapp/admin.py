from django.contrib import admin
from .models import Counter, WebPageTxt

admin.site.register(WebPageTxt)

class CounterAdmin(admin.ModelAdmin):
    readonly_fields = ('nome',)

admin.site.register(Counter, CounterAdmin)

admin.site.site_header = 'Amministrazione'
admin.site.site_title = 'contapp'
admin.site.index_title = 'Indice'