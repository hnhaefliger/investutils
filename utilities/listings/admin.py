from django.contrib import admin

from .models import Ticker

class TickerAdmin(admin.ModelAdmin):
    fields = ('ticker', 'token_type')
    readonly_fields = ('ticker', 'token_type')

    def token(self, obj): return obj.ticker
    def token_type(self, obj): return obj.ticker_type


admin.site.register(Ticker, TickerAdmin)
