def max_bid ():
    max = 0
    for num in bid:
        if num > max:
            max = num








more_bids = True
while more_bids:
    name = input("What is your name?\n")
    bid = [200, 5000, 250, 3000, 284, 3900, 400]
    choose = int(input("choose one value to bid"))
    ask = input("Type 'yes' if there is another bidder, type 'no' if there isn't:\n")
    max_bid()

    

    if ask == "no":
      more_bids = False
    
print(f"The highest bidder is {name}, item sold for ${max}")

