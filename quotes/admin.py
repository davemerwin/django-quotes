from django.contrib import admin

from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('slug', 'content')
    ordering = ('slug',)

admin.site.register(QuoteContent, QuoteContentAdmin)
