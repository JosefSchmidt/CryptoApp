import requests
from coin import Coin

class MyCoins:

    # Array of saved coins
    myListOfCoins = []


# searchForCoin() allows the user to search for a coin an view a price, daily percent change and a description
def searchForCoin():

    # Asks for user to type in a coin to be search for
    selectCoin = input('Coin name: ')

    # API url with the typed coin connected
    url = 'https://api.coingecko.com/api/v3/coins/' + selectCoin

    # Uses try-catch for error handling.
    # If response is an error or if internet connection is lost raise exception
    try:
        response = (requests.get(url)).json()
        print('\n\rName: {}'.format(response['id']))
        print('Current Market Price: {}\n'.format(response['market_data']['current_price']['usd']))
        print('Description: \n{}\n\n'.format(response['description']['en']))

    except (requests.exceptions.RequestException,
            ConnectionResetError) as err:
            print(err, " -- Could not find coin")
        
# addCoin() allows the user to add a coin to myListOfCoins
def addCoin():

    # Asks for user to type the coins name to be added to myListOfCoins
    selectCoin = input('Coin name: ')

    # API url with the typed coin connected
    url = 'https://api.coingecko.com/api/v3/coins/' + selectCoin

    try:
        response = (requests.get(url)).json()
        MyCoins.4.append(Coin(selectCoin, response["market_data"]['current_price']['usd'], response["market_data"]['price_change_percentage_24h']))
        print('\nAdded coin: {}'.format(selectCoin))

    except (requests.exceptions.RequestException, ConnectionResetError) as error:
        print('\nCould not find coin. Unexpected response after typed coin: ', error)

    except IndexError as indexError:
        print(indexError)

    except KeyError as keyError:
        print(keyError)


# deleteCoin() allows the user to delete a coin from myListOfCoins
def deleteCoin():

    # Asks the user to type the coins name to be deleted from myListOfCoins
    selectCoin = input('Coin name')


    # Searches after typed coin and if matches removes it from myListOfCoins
    for coin in MyCoins.myListOfCoins:
        if coin.name == selectCoin:
            MyCoins.myListOfCoins.remove(coin)
        else:
            continue

# updateCoins() allows the user to update the market value and daily market change in percent to the coins added to myListOfCoins
def updateCoins():

    # API to get coins
    url = 'https://api.coingecko.com/api/v3/coins/'

    for coin in MyCoins.myListOfCoins:
        url = url + coin.name
        response = (requests.get(url)).json()
        try:
            coin.price = response['market_data']['current_price']['usd']

        except (requests.exceptions.RequestException, ConnectionResetError) as error:
            print('\nCould not find coin. Unexpected response after typed coin: ', error)

        except IndexError as indexError:
            print(indexError)

        except KeyError as keyError:
            print(keyError)
