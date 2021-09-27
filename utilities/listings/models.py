from django.db import models

class Ticker(models.Model):
    '''
    A ticker that is listed on an exchange.
    '''
    ticker = models.CharField(max_length=8, unique=True)
    ticker_type = models.CharField(max_length=16, unique=False)
    on_robinhood = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ticker_type} : {self.ticker}'
