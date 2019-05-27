import requests
from coin import Coin

class TopCoin:
    top20List = []

def displayTop20():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false'
    response = (requests.get(url)).json()

    for i in response:

        TopCoin.top20List.append(Coin(i['name'], i['current_price'], i['price_change_percentage_24h']))

    print('\nTOP 20 CRYPTOCOINS')
    print('------------------------')
    for coin in TopCoin.top20List:
        print(coin.__str__())
