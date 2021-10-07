from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json 
from progress.bar import ChargingBar

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'25',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
} #Add CoinMarketCap API Key 

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  length = len(data['data'])
  i = 0;
  total = 0;

  print("{:<17}\t{:>}".format("Crypto", "Dominance"))
  print("-"*33)
  while i < length:
    name = data['data'][i]['name']
    MCD = str(data['data'][i]['quote']['USD']['market_cap_dominance'])
    total += float(MCD)

    #print(name + ' ' + MCD)

    print("{:<17}\t{:<7.6}".format(name, MCD))
    
    """
    with ChargingBar(name, max = 100) as bar:
      for j in range(MCD):
        bar.next()
    """
    #print(data['data'][i]['name'] + " " + str(data['data'][i]['quote']['USD']['market_cap_dominance']))
    #print(data['data'][i]['quote']['USD']['market_cap_dominance'])
    i += 1

  print("-"*30)
  print("Top 25 Total Dominance: {:<.5}".format(total))
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  