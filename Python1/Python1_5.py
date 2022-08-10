allBids = [int(x) for x in input("Enter All Bid : ").split()]
bidder = len(allBids) #get list len
if bidder <= 1:
    print("not enough bidder")
else:
    allBids.sort(reverse=False) # can be True [bidder-1 will be 0 digit]
    if allBids[bidder-1] == allBids[bidder-2]:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {allBids[bidder-1]} need to pay {allBids[bidder-2]}")