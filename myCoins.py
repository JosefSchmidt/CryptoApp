import requests
from coin import Coin

class MyCoins:

    # Array of saved coins
    myListOfCoins = []


    # addCoin() allows the user to add a coin to myListOfCoins
    def addCoin(self, coin):

        try:
            # API url with the typed coin connected
            url = 'https://api.coingecko.com/api/v3/coins/' + coin

            response = (requests.get(url)).json()
            MyCoins.myListOfCoins.append(Coin(coin, response["market_data"]['current_price']['usd'], response["market_data"]['price_change_percentage_24h']))
            print('\nAdded coin: {}'.format(coin))

        except (requests.exceptions.RequestException, ConnectionResetError) as error:
            print('\nCould not find coin. Unexpected response after typed coin: ', error)

        except IndexError as indexError:
            print('IndexError: ',indexError)

        except KeyError as keyError:
            print('KeyError. Could not find',keyError)

        except ValueError as valueError:
            print('ValueError: :',valueError)

        except TypeError as typeError:
            print('TypeError: ', typeError)


    # deleteCoin() allows the user to delete a coin from myListOfCoins
    def deleteCoin(self, typedCoin):

        # Searches after typed coin and if matches removes it from myListOfCoins
        for coin in MyCoins.myListOfCoins:
            if coin.name == typedCoin:
                MyCoins.myListOfCoins.remove(coin)
            else:
                continue

    # updateCoins() allows the user to update the market value and daily market change in percent to the coins added to myListOfCoins
    def updateCoins(self):

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
