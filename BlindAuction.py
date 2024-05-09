import clear

import Art

end = False
auction = {}
max_bid = 0
max_bidder = ""

print(Art.logo)
print("Welcome to the secret action program:\n")

while not end:

    name = input("What's your name:")
    bid = int(input("What's your bid: $"))
    auction[name] = bid

    cont = input("Are there any other bidder's? Type 'yes' or 'no'").lower()
    if cont == "no":
        end = True
    elif cont == "yes":
        clear.clear()

for key in auction:
    if auction[key] > max_bid:
        max_bid = auction[key]
        max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
