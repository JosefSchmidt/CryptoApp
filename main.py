import topCoins as topCoins
import myCoins as myCoins

def main():
  while(True):

    homeInput = input('\n1. See Top 20 coins\n' 
                        '2. My Coins\n'
                        'q. Quit Program')   
    if(homeInput == "q"):
      break 
    elif(homeInput == "1"):
      topCoins.main()

      while(True):
        top20Input = input('\n1. Search for Coin\n'
                             '2. Sort by name\n'
                             '3. Sort by daily change\n'
                             '4. Go back\n')

        if(top20Input == "1"):
          myCoins.searchForCoin()

        elif(top20Input == "2"):

          topCoins.TopCoin.top20.sort(key=lambda x: x.name)
          
          print('\nSORTED BY NAME')
          print('------------------------')
          for coin in topCoins.TopCoin.top20:
            print(coin)
          print()

        elif(top20Input == "3"):
          
          topCoins.TopCoin.top20.sort(key=lambda x: x.change, reverse=True)

          print('\nSORTED BY DAILY CHANGE %')
          print('------------------------')
          for coin in topCoins.TopCoin.top20:
            print(coin)
          print() 

        elif(top20Input == "4"):
          break

    elif(homeInput == "2"):
      
      while(True):
        print('\nMY COINS')
        print('---------------')

        if(len(myCoins.MyCoins.myListOfCoins) > 0 ):
          for coin in myCoins.MyCoins.myListOfCoins:
            print(coin)
        else:
          print('Currently no coins added')

        bookmarkInput = input('\n1. Update coins\n'
                                '2. Add coin\n'
                                '3. Delete coin\n'
                                '4. Go back\n')
        if(bookmarkInput == '1'):
          myCoins.updateCoins()                          

        elif(bookmarkInput == '2'):
          myCoins.addCoin()

        elif(bookmarkInput == '3'):
          myCoins.deleteCoin()
        
        elif(bookmarkInput == '4'):
          break

if __name__ == '__main__':
  main()