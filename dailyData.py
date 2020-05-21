# get historical data initially daily open-close/high-low data
# PLANNING add functionality to change resolution
# TOKEN: 

# RESPONSE INFO
# BASE URL: https://finnhub.io/api/v1/stock/candle?
# SYMBOL: symbol=TSLA&
# GRANULARITY: resolution=1&
# START DATE: from=1572651390& unix timestamp
# END DATE: to=1572910590&
# API_KEY token=TOKEN

import datetime
from requests import get
from credentials import api_key

# print(api_key)
# print(f"time: {resp['t'][num]}, open: {resp['o'][num]}, close: {resp['c'][num]}, high: {resp['h'][num]}, low: {resp['l'][num]}, volume: {resp['v'][num]}")


def format_response(json_data):
    candles = []
    for num in range(0, len(json_data['t'])):
        candles.append({
            "time" : json_data['t'][num],
            "open" : json_data['o'][num],
            "close" : json_data['c'][num],
            "high" : json_data['h'][num],
            "low" : json_data['l'][num],
            "volume" : json_data['v'][num]
        })
    return candles

def date_to_unix(year, month, day):
    date_obj = datetime.datetime( year, month, day)
    return int(str(date_obj.timestamp())[0:-2])

def get_today():
    today = datetime.date.today.strftime("%d/%m/%Y")
    return 
    return int(str(today.timestamp())[0:-2])

def build_url(symbol, start, end, token):
    base_url = "https://finnhub.io/api/v1/stock/candle?"
    return f"{base_url}symbol={symbol}&resolution=D&from={start}&to={end}&token={token}"

def pull_data(symbol, start_year, start_month, start_day):
    req_url = build_url(
        symbol,
        date_to_unix( start_year, start_month, start_day),
        get_today,
        api_key
        )
    return get(req_url).json()


# symbol = "TSLA"
# start = 1357016400
# end = 1572910590
# token = api_key


# resp = get(url).json()
# data = format_response(resp)

# data = pull_data( "MSFT", 2010, 1, 1)
# candles = format_response(data)
# print(len(candles))
print(date_to_unix(2010, 1, 1))
print(get_today())