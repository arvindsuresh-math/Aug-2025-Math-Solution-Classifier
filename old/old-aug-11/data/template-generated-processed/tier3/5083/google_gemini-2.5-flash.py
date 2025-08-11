def solve():
    """Index: 5083.
    Returns: the number of times each person bid on the desk.
    """
    # L1
    final_price = 65 # to $65
    initial_price = 15 # from $15
    total_price_increase = final_price - initial_price

    # L2
    price_increase_per_bid = 5 # raises the price of an item he is auctioning by $5 every time
    total_bids = total_price_increase / price_increase_per_bid

    # L3
    number_of_bidders = 2 # Two people enter a bidding war
    bids_per_person = total_bids / number_of_bidders

    # FA
    answer = bids_per_person
    return answer