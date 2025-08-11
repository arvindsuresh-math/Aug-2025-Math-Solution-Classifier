def solve():
    """Index: 4863.
    Returns: the amount Harry's final bid exceeded the third bidder's bid.
    """
    # L1
    starting_bid = 300 # The auction starts at $300
    harry_first_bid_amount = 200 # adding $200 to the starting value
    bid_after_harry_first = starting_bid + harry_first_bid_amount

    # L2
    second_bidder_multiplier = 2 # a second bidder doubles the bid
    bid_after_second_bidder = bid_after_harry_first * second_bidder_multiplier

    # L3
    third_bidder_multiplier = 3 # three times Harry's bid (interpreted by solution as 3 times the current bid after Harry's first bid)
    third_bidder_added_amount = bid_after_harry_first * third_bidder_multiplier

    # L4
    bid_after_third_bidder = third_bidder_added_amount + bid_after_second_bidder

    # L5
    harry_final_bid = 4000 # Harry bids $4,000
    harry_exceeds_third_bidder = harry_final_bid - bid_after_third_bidder

    # FA
    answer = harry_exceeds_third_bidder
    return answer