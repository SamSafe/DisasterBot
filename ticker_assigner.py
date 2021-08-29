import random
import quandl
from functools import lru_cache

load dotenv()

quandl.ApiConfig.api_key = os.environ("TICKER_TOKEN")

@lru_cache()
def list_maker():
    with open('WIKI_PRICES.csv') as csvfile:
        return csvfile.read().split('\n')[1:]

def get_ticker_price():
    return quandl.get(f'WIKI/{random.choice(list_maker())}')
