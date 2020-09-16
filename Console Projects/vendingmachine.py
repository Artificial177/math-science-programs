import math

'''
This is my first real Python project, a console-based 'vending machine'.
'''

print ("Welcome to the Vending Machine!")
quarters = input("Enter the number of quarters you wish to insert: ")
credit_global = float(quarters)*0.25

# User enters quarters.

print ("You've entered $%.2f." % credit_global)

# System returns user value in dollar form.

if credit_global < 0.75:
   print ("Sorry, that isn't enough money to purchase anything in this vending machine!")
   quit()

category = {
   1:"Drinks",
   2:"Snacks",
   3:"Exit"
}

print()

def main_menu_global():
   print ("Select Category:")

   for item in category:
      print (item, ". ", category[item], sep='')


   choice = input("Select an option: ")

   return choice


category_choice = main_menu_global()

drink_menu = { # Drinks menu.
   "Water": 1,
   "Juice": 3,
   "Soda": 1.5
}

snack_menu = { # Snacks menu.
   "Chips": 1.25,
   "Peanuts": 0.75,
   "Cookie": 1
}



def print_selected_menu(input_menu):
   for item in input_menu:
      print(item + ": ($" + str(input_menu[item]) + ")")

      # Takes in the inputted menu (drinks or snacks), and prints out the item in format.

in_vending_global = True
purchase_global = 0
change_global = credit_global


# Basis of the program.
while in_vending_global == True:

   if category_choice.lower() == "1":

      in_drink_menu = True

      while in_drink_menu == True:
         print_selected_menu(drink_menu)
         drinkselection = input("Enter your drink selection (or x to exit): ")

         if drinkselection.lower() == "x" or credit_global == 0:
            in_drink_menu = False
            category_choice = main_menu_global()

            # Exits the drinks menu, reassigns the main menu function to a new value.

         elif drinkselection.lower() ==  "water" or "soda" or "juice": # If the user has entered a valid input.

            if drinkselection.lower() == "water": # Differentiates user input into three categories, then validates payment.
               if change_global < 1:
                  print("You don't have enough money to buy Water.")

               elif change_global >= 1:
                  purchase_global += 1
                  change_global -= 1
                  print("Vending: Water. You have $%.2f left." % (change_global))

            if drinkselection.lower() == "juice":
               if change_global < 3:
                  print("You don't have enough money to buy Juice.")

               elif change_global >= 3:
                  purchase_global += 3
                  change_global -= 3
                  print("Vending: Juice. You have $%.2f left." % (change_global))

            if drinkselection.lower() == "soda":
               if change_global < 1.5:
                  print("You don't have enough money to buy Soda.")

               elif change_global >= 1.5:
                  purchase_global += 1.5
                  change_global -= 1.5
                  print("Vending: Soda. You have $%.2f left." % (change_global))

         else:
            print("That is not a valid input. Please re-enter the name of the item which you wish to purchase.")




   elif category_choice.lower() == "2":

      in_snack_menu = True

      while in_snack_menu == True:
         print_selected_menu(snack_menu)
         drinkselection = input("Enter your drink selection (or x to exit): ")

         if drinkselection.lower() == "x" or credit_global == 0:
            in_snack_menu = False
            category_choice = main_menu_global()

            # Exits the drinks menu, reassigns the main menu function to a new value.

         elif drinkselection.lower() ==  "chips" or "peanuts" or "cookie": # If the user has entered a valid input.

            if drinkselection.lower() == "chips": # Differentiates user input into three categories, then validates payment.
               if change_global < 1.25:
                  print("You don't have enough money to buy Chips.")

               elif change_global >= 1.25:
                  purchase_global += 1.25
                  change_global -= 1.25
                  print("Vending: Chips. You have $%.2f left." % (change_global))

            if drinkselection.lower() == "peanuts":
               if change_global < 0.75:
                  print("You don't have enough money to buy Peanuts.")

               elif change_global >= 0.75:
                  purchase_global += 0.75
                  change_global -= 0.75
                  print("Vending: Peanuts. You have $%.2f left." % (change_global))

            if drinkselection.lower() == "cookie":
               if change_global < 1:
                  print("You don't have enough money to buy Cookie.")

               elif change_global >= 1:
                  purchase_global += 1
                  change_global -= 1
                  print("Vending: Cookie. You have $%.2f left." % (change_global))

         else:
            print("That is not a valid input. Please re-enter the name of the item which you wish to purchase.")




   elif category_choice.lower() == "3" or credit_global == 0:
      print("Paid Amount: $%.2f, Total Purchase: $%.2f, Change: $%.2f" % (credit_global, purchase_global, change_global))
      in_vending_global = False

   else:
      print("That is not a valid input. Please re-enter the number of the option you wish to select.")
      category_choice = main_menu_global()














