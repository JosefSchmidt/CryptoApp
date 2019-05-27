import topCoins as topCoins
import myCoins as myCoins
from stringTemplates import StringTemplates

def main():
  while True:
    # Get input from user to navigate
    home_Input = input(StringTemplates.home_input_string)

    # If answer is 'q' the program will stop
    if(home_Input.lower() == "q"):
      break

    # If answer is '1' the program will call 'displayTop20()' from topCoins and display top 20 coins
    elif(home_Input == "1"):

      # Calling displayTop20()
      topCoins.displayTop20()

      while True:

        # Get
        top20_Input = input(StringTemplates.top20_input_string)

        if top20_Input == "1":
          myCoins.searchForCoin()

        elif top20_Input == "2":

          topCoins.TopCoin.top20List.sort(key=lambda x: x.name)

          print(StringTemplates.sortedByName)

          for coin in topCoins.TopCoin.top20List:
            print(coin)
          print()

        elif top20_Input == "3":
          
          topCoins.TopCoin.top20List.sort(key=lambda x: x.change, reverse=True)
          print(StringTemplates.sortedByDailyChange)

          for coin in topCoins.TopCoin.top20List:
            print(coin)
          print() 

        elif top20_Input == "4":
          break

    elif home_Input == "2":
      while True:
        print(StringTemplates.myCoins)
        if len(myCoins.MyCoins.myListOfCoins) > 0:
          for coin in myCoins.MyCoins.myListOfCoins:
            print(coin)
        else:
          print('Currently no coins added')

        bookmark_input = input(StringTemplates.bookmark_input_string)

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