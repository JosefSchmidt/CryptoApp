import topCoins as topCoins
import myCoins as myCoins

def main():
  while True:

    home_Input = input\
  (
  """
  1. See Top 20 Coins
  2. My Coins
  q. Quit Program
  """
  )

    if(home_Input.lower() == "q"):
      break 
    elif(home_Input == "1"):
      topCoins.main()

      while True:

        top20_Input = input\
  (
  """
  1. Search for Coin
  2. Sort by name
  3. Sort by daily change
  4. Go back
  """
  )

        if top20_Input == "1":
          myCoins.searchForCoin()

        elif top20_Input == "2":

          topCoins.TopCoin.top20.sort(key=lambda x: x.name)
          
          print('\nSORTED BY NAME')
          print('------------------------')
          for coin in topCoins.TopCoin.top20:
            print(coin)
          print()

        elif top20_Input == "3":
          
          topCoins.TopCoin.top20.sort(key=lambda x: x.change, reverse=True)

          print('\nSORTED BY DAILY CHANGE %')
          print('------------------------')
          for coin in topCoins.TopCoin.top20:
            print(coin)
          print() 

        elif top20_Input == "4":
          break

    elif home_Input == "2":
      
      while True:
        print('\nMY COINS')
        print('---------------')

        if len(myCoins.MyCoins.myListOfCoins) > 0:
          for coin in myCoins.MyCoins.myListOfCoins:
            print(coin)
        else:
          print('Currently no coins added')

        bookmark_input = input('\n1. Update coins\n'
                                '2. Add coin\n'
                                '3. Delete coin\n'
                                '4. Go back\n')
        if bookmark_input == '1':
          myCoins.updateCoins()                          

        elif bookmark_input == '2':
          myCoins.addCoin()

        elif bookmark_input == '3':
          myCoins.deleteCoin()
        
        elif bookmark_input == '4':
          break

if __name__ == '__main__':
  main()