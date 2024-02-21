from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name:")
bid = input("What is your bid?: $")
other_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
bids_dictionary = {}
def repetition():
   name = input("What is your name:")
   bid = input("What is your bid?: $")
   bids_dictionary[name] = bid



other_bidders = "yes"
while other_bidders == "yes":
  clear()
  repetition()
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'")
  clear()
highest_bid = max(bids_dictionary, key=bids_dictionary.get)
print(f"The winner is {highest_bid} with an amount of : {bids_dictionary[highest_bid]} $")
