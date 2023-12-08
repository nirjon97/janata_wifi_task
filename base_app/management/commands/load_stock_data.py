import json
from django.core.management.base import BaseCommand
from base_app.models import StockData

class Command(BaseCommand):
    help = 'Load stock data from JSON and store in the database'

    def handle(self, *args, **kwargs):
        with open('C:/Users/nirjon/Desktop/janata wifi task/janata_wifi/base_app/management/commands/stock_market_data.json') as file:
            data = json.load(file)

        for entry in data:
            StockData.objects.create(
                date=entry['date'],
                trade_code=entry['trade_code'],
                high=float(entry['high'].replace(',', '')),
                low=float(entry['low'].replace(',', '')),
                open=float(entry['open'].replace(',', '')),
                close=float(entry['close'].replace(',', '')),
                volume=int(entry['volume'].replace(',', ''))  # Remove commas from volume
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded stock data'))