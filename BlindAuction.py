import art
print(art.logo)

def find_max_bid(bids):
    winner = ""
    max_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > max_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is: {winner} with {max_bid} $")

dictionary = {}
new_bid = True

while new_bid:
    name = input("What is you name?: ")
    dictionary[name] = int(input("What is your bid?: $"))

    if input("Are there any other bidders? Type 'yes or 'no'.\n").lower() == "no":
        new_bid = False
        find_max_bid(dictionary)
    elif input("Are there any other bidders? Type 'yes or 'no'.\n").lower() == "yes":
        print("\n" * 100)



