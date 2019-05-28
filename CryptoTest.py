import unittest
from myCoins import MyCoins
from topCoins import TopCoin


class CryptoTest(unittest.TestCase):

    myTestCoins = MyCoins()
    topCoins = TopCoin()

    def test_addCoin(self):

        self.assertEqual(len(CryptoTest.myTestCoins.myListOfCoins), 0)
        print('The length of the list is: ', len(CryptoTest.myTestCoins.myListOfCoins))

        CryptoTest.myTestCoins.addCoin('bitcoin')
        self.assertEqual(len(CryptoTest.myTestCoins.myListOfCoins), 1)
        print('The length of the list is: ', len(CryptoTest.myTestCoins.myListOfCoins))


    def test_deleteCoin(self):

        self.assertEqual(len(CryptoTest.myTestCoins.myListOfCoins), 1)
        print('The length of the list is: ', len(CryptoTest.myTestCoins.myListOfCoins))

        CryptoTest.myTestCoins.deleteCoin('bitcoin')
        self.assertEqual(len(CryptoTest.myTestCoins.myListOfCoins), 0)
        print('The length of the list is: ', len(CryptoTest.myTestCoins.myListOfCoins))

    def test_20Coins_added(self):

        self.assertEqual(len(CryptoTest.topCoins.top20List), 0)
        print('The length of the list is: ', len(CryptoTest.topCoins.top20List))

        CryptoTest.topCoins.displayTop20()
        self.assertEqual(len(CryptoTest.topCoins.top20List), 20)
        print('The length of the list is: ', len(CryptoTest.topCoins.top20List))


    def test_ifCoinExists(self):

        CryptoTest.myTestCoins.addCoin('bitcoin')

        # List comprehension
        tempCoin = [coin for coin in CryptoTest.myTestCoins.myListOfCoins if coin.name == 'bitcoin'][0]

        # tempCoin = None
        # for coin in CryptoTest.myTestCoins.myListOfCoins:
        #     if coin.name == 'bitcoin':
        #         tempCoin = coin

        self.assertIn(tempCoin, CryptoTest.myTestCoins.myListOfCoins)












