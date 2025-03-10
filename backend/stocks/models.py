from django.db import models

class Stock(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    def str(self):
        return f"{self.trade_code} - {self.date}"