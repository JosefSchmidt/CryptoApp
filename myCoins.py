import requests
import json
from coin import Coin

class MyCoins:
    myListOfCoins = []

def main():  
    None

def searchForCoin():
    selectCoin = input('Coin name: ')
    
    url = 'https://api.coingecko.com/api/v3/coins/' + selectCoin

    response = (requests.get(url)).json()
    
    try:
        print('\nname: {}'.format(response['id']))
        print('Current Market Price: {}\n'.format(response['market_data']['current_price']['usd']))
        print('Description: \n{}\n\n'.format(response['description']['en']) )
    except:
        print('Could not find coin')
        

def addCoin():
    selectCoin = input('Coin name: ')

    url = 'https://api.coingecko.com/api/v3/coins/' + selectCoin
    
    response = (requests.get(url)).json()

    try:        
        MyCoins.myListOfCoins.append(Coin(selectCoin, response["market_data"]['current_price']['usd'], response["market_data"]['price_change_percentage_24h']))
        print(f'\nAdded coin: {selectCoin}')
    except (IndexError, KeyError):
        print('\nCould not find coin. Unexpected response after typed coin: ',
              response)


def deleteCoin():
    selectCoin = input('Coin name')

    for coin in MyCoins.myListOfCoins:
        if coin.name == selectCoin:
            MyCoins.myListOfCoins.remove(coin)
        else:
            continue

def updateCoins():
    
    url = 'https://api.coingecko.com/api/v3/coins/'

    for coin in MyCoins.myListOfCoins:
        url = url + coin.name
        response = (requests.get(url)).json()
        try:
            coin.price = response['market_data']['current_price']['usd']
        except (IndexError, KeyError):
            print('Could not find coin. Unexpected response after typed coin: ', response)
    
if __name__ == '__main__':
  main()