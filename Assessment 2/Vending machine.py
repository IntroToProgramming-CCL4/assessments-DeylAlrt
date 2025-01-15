import time
import sys

# List/items of snacks and drinks.
snacks = {
    1: {"name": "Cheetos", "price": 6.50, "stock": 5},
    2: {"name": "Doritos", "price": 8.75, "stock": 3},
    3: {"name": "Maltesers", "price": 8.20, "stock": 4},
    4: {"name": "Snickers", "price": 6.15, "stock": 6},
    5: {"name": "Takis", "price": 6.80, "stock": 2},
}
drinks = {
    6: {"name": "Monster", "price": 8.00, "stock": 7},
    7: {"name": "Mountain Dew", "price": 7.00, "stock": 5},
    8: {"name": "Water", "price": 3.00, "stock": 4},
    9: {"name": "Vento", "price": 5.00, "stock": 2},
    10: {"name": "Orange Juice", "price": 4.00, "stock": 3},
}

cart = []
balance = 0.0

# Opening and granted animation.
def opening():
    message = "opening", ".", ".", ".\n"
    for i in message:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.6) 
opening()

def proceed():
    global balance
    while True:
        try:
            # Asks the user how much money to input to proceed.
            amount = float(input("\nInsert money to proceed: "))
            # inserts the user's input and shows the balance.
            if amount > 0:
                balance += amount
                display = "\nInserting",".",".","."
                for i in display:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.5) 
                print(f"\nYou have inserted 💲{amount:.2f}. Current balance: 💲{balance:.2f}")
                message2 = "Granted!!!"
                for char in message2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.09)
                break
            else:
                print("Please insert a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
proceed()

# Displays the list of items.
def display_item():
    print("\n\nWelcome to Dale's Vending Machine.")
    print("─" * 52)
    print("Here are the list of Snacks 🍫:")
    for number, item in snacks.items():
        print(f"{number}. {item['name']:<25} - 💲{item['price']:.2f}  -  Stocks: {item['stock']}")
    print("─" * 52)
    print("Here are the list of Drinks 🧃:")
    for number, item in drinks.items():
        print(f"{number}. {item['name']:<25} - 💲{item['price']:.2f}  -  Stocks: {item['stock']}")
    print("─" * 52)
display_item()

# Insert money function.
def insert_money():
    global balance
    while True:
        try:
            # Asks the user how much money to input.
            amount = float(input("\nInsert money (or type 0 to go back): "))
            # Exits out the insert money function.
            if amount == 0:
                break
            # inserts the user's input and shows the balance.
            elif amount > 0:
                balance += amount
                display = "\nInserting",".",".","."
                for i in display:
                    sys.stdout.write(i)
                    sys.stdout.flush()
                    time.sleep(0.5) 
                print(f"\nYou have inserted 💲{amount:.2f}. Current balance: 💲{balance:.2f}")
                break
            else:
                print("Please insert a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Selection of items function.
def select_items():
    global balance
    while True:
        try:
            display_item()
            # asks the user to input what item to purchase.
            user_input = int(input("\nPlease enter an item number to purchase (or 0 to go back): "))
            # exits out the selections of items.
            if user_input == 0:
                break
            # checks if the user chose a snack or a drink.
            if user_input in snacks:
                item = snacks[user_input]
            elif user_input in drinks:
                item = drinks[user_input]
            else:
                print("❌ Invalid item number ❌. Please try again.")
                continue
            # checks if there are still items in stock and then adds to the cart.
            if item['stock'] > 0:
                if balance >= item['price']:
                    cart.append(item)
                    item['stock'] -= 1
                    balance -= item['price']
                    print(f"\nAdded {item['name']} to cart. Remaining stock: {item['stock']}. Current balance: 💲{balance:.2f}")
                # executes when the user has low balance.
                else:
                    print(f"Insufficient balance. {item['name']} costs 💲{item['price']:.2f}, but your balance is 💲{balance:.2f}. Insert more money to purchase this item.")
            # Displays that a certain item has ran out of stock.
            else:
                print(f"Sorry, {item['name']} is out of stock 🥺👉👈 pick something else.")
        except ValueError:
            print("❌ Invalid input ❌. Please enter a number.")

# Shows what is in the cart.
def display_cart():
    # Shows that the cart is empty
    if not cart:
        print("\nYour cart is empty...")
    else:
    # Shows all the items that have been purchased.
        print("\nHere are the items in your cart:")
        total = 0
        for item in cart:
            print(f"{item['name']} - 💲{item['price']:.2f}")
            total += item['price']
        # shows how much all the items are.
        print(f"Total: 💲{total:.2f}")

# Options function for user to pick.
def main():
    while True:
        # Options to select on what the user would want to do.
        time.sleep(1.5)
        print(f"\nYour current balance is: 💵 {balance:.2f}")
        print("─" * 52)
        print("\nWhat would you like to do?")
        print("1. Insert more money")
        print("2. Select items")
        print("3. View cart")
        print("4. Exit")
        try:
            # If the user chooses one of the options then one of these will be called out depending on what the user chooses.
            choice = int(input("Enter your choice: "))
            # Calls out the insert money function.
            if choice == 1:
                insert_money()
            # Calls out the Select items function.
            elif choice == 2:
                select_items()
            # Calls out what is inside the cart function.
            elif choice == 3:
                display_cart()
            # Ends the purchasing and choosing options. This will then show how much money you have left
            elif choice == 4:
                print(f"\nThank you for using Dale's Vending Machine! 😊.")
                print("─" * 52)
                print("\nHere is your receipt:")
                print(f"Current balance: 💲{balance:.2f}")
                total = 0
                for item in cart:
                    print(f"{item['name']} - 💲{item['price']:.2f}")
                    total += item['price']
                # shows how much all the items are.
                print(f"Total: 💲{total:.2f}\n")
                print("─" * 52)
                if balance > 0:
                    display = ("Returning balance",".",".",".", f"\nYour returning balance is 💵 {balance:.2f}. Have a nice day! 😊")
                    for i in display:
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.5) 
                break
            else:
                print("❌ Invalid choice ❌. Please try again.")
        except ValueError:
            print("❌ Invalid input ❌. Please enter a number.")
main()

# Rating of experience function for user to rate how good or bad the vending machine is.
def experience():
    while True:
        try:
            user_input = int(input("\nKindly rate your experience ⭐ 1-5: "))
            # if the user's rate is less than or equal to 3 then this will be executed.
            if 1 <= user_input <= 3:
                print(f"\nOh wow thats pretty low 😥! Thank you for rating our Vending Machine. You rated us {user_input}⭐.")
                break
            # if the user's rate is more than or equal to 5 then this will be executed.
            elif 4 <= user_input <=5:
                print(f"\nHappy to hear that you like the experience 🤩! Thank you for rating our Vending Machine. You rated us {user_input}⭐.")
                break
            # this will execute if the user inputs more than 5 or less than 0.
            else:
                print("The rating is until 1-5 only! Try again.")
        # Executes if the user input is not an integer.
        except ValueError:
            print("Sorry, we do not accept this answer.")
experience()

def feedback():
    # Get user input for feedback
    user_feedback = input("\nPlease help us improve more by giving us feedbacks (Keep empty if none): ").strip().lower()
    
    # Try to read existing feedbacks from the file.
    try:
        with open("Feedbacks.txt", "r") as file:
            feedback_list = file.readlines()  # Read all lines from the file.
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list.
        feedback_list = []

    # Count how many times the user's feedback has appeared in the file.
    feedback_counts = sum(1 for line in feedback_list if line.strip().lower() == user_feedback)

    # Append the user's feedback to the file.
    with open("Feedbacks.txt", "a") as file:
        file.write(user_feedback + "\n")

    # Provide feedback to the user about their entry.
    print(f"Thank you for your feedback ❤️! Your feedback has been recorded {feedback_counts + 1} time(s).")
feedback()