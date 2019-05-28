import requests
from coin import Coin
from stringTemplates import StringTemplates

class TopCoin:

    top20List = []

    def displayTop20(self):

        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=20&page=1&sparkline=false'
        response = (requests.get(url)).json()

        for i in response:
            TopCoin.top20List.append(Coin(i['name'], i['current_price'], i['price_change_percentage_24h']))

        StringTemplates.top20Title()
        for coin in TopCoin.top20List:
            print(coin.__str__())

    # searchForCoin() allows the user to search for a coin an view a price, daily percent change and a description
    def searchForCoin(self, coin):

        # Uses try-catch for error handling.
        # If response is an error or if internet connection is lost raise exception
        try:
            # API url with the typed coin connected
            url = 'https://api.coingecko.com/api/v3/coins/' + coin

            response = (requests.get(url)).json()

            print('\n\rName: {}'.format(response['id']))
            print('Current Market Price: {}\n'.format(response['market_data']['current_price']['usd']))
            print('Description: \n{}\n\n'.format(response['description']['en']))

        except (requests.exceptions.RequestException,
                ConnectionResetError) as err:
                print(err, " -- Could not find coin")

        except IndexError as indexError:
            print('IndexError: ',indexError)

        except KeyError as keyError:
            print('KeyError. Could not find', keyError)
