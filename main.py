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

      # Going in to a while loop so program doesn't stop
      while True:

        # Get user input and display template string from StringTemplates
        top20_Input = input(StringTemplates.top20_input_string)

        # If user input is '1' call 'searchForCoins()'
        if top20_Input == "1":
          myCoins.searchForCoin()

        # Else if user input is '2' sort top20List by name.
        elif top20_Input == "2":

          # Sorting the list from here because top20List is static
          topCoins.TopCoin.top20List.sort(key=lambda x: x.name)

          # Prints the StringTemplates string 'sortedByName'
          print(StringTemplates.sortedByName)

          # Prints all the coins from the static top20List
          for coin in topCoins.TopCoin.top20List:
            print(coin)
          print()

        # If user input is '3' sort top20List by change
        elif top20_Input == "3":

          # Sorting the my20List - notice that the list is reversed so the highest value comes first
          topCoins.TopCoin.top20List.sort(key=lambda x: x.change, reverse=True)
          # Prints the StringTemplates string 'sortedByDailyChange'
          print(StringTemplates.sortedByDailyChange)

          # Prints all the coins from the static top20List
          for coin in topCoins.TopCoin.top20List:
            print(coin)
          print() 

        # If user input is '4' break the while loop and return to home_input
        elif top20_Input == "4":
          break

    # If user input is '2' navigate to user Bookmark section
    elif home_Input == "2":

      while True:
        # Print the StringTemplates string 'myCoins'
        print(StringTemplates.myCoins)

        # If the length of myListOfCoins is bigger than 0 print the coins
        if len(myCoins.MyCoins.myListOfCoins) > 0:
          for coin in myCoins.MyCoins.myListOfCoins:
            print(coin)
        else:
          # If the length of myListOfCoins is 0 or less print the 'Currently no coins added' message
          print('Currently no coins added')

        # Print the StringTemplates string 'bookmark_input_string'
        bookmark_input = input(StringTemplates.bookmark_input_string)

        # If user input is '1' call updateCoins()
        if bookmark_input == '1':
          # Updates the market value for the saved coins and their daily change in %
          myCoins.updateCoins()                          

        # If user input is '2' call addCoin()
        elif bookmark_input == '2':
          # Allows user to add a coin
          myCoins.addCoin()

        # If user input is '3' call deleteCoin()
        elif bookmark_input == '3':
          # Allows user to delete a coin
          myCoins.deleteCoin()

        # If user input is '4' break the loop
        elif bookmark_input == '4':
          break

if __name__ == '__main__':
  main()