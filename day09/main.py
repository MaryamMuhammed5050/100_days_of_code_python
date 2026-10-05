def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {}
    new_bidder["bid"] = bidder_amount
    new_bidder["name"] = bidder_name
    auction_info.append(new_bidder)