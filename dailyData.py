# get historical data initially daily open-close/high-low data
# PLANNING add functionality to change resolution
# TOKEN: 

# RESPONSE INFO
# BASE URL: https://finnhub.io/api/v1/stock/candle?
# SYMBOL: symbol=TSLA&
# GRANULARITY: resolution=1&
# START DATE: from=1572651390&
# END DATE: to=1572910590&
# API_KEY token=TOKEN

from requests import get
from credentials.py import api_key

print api_key

