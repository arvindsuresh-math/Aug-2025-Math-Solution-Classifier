from fractions import Fraction

def solve():
    """Index: 5076.
    Returns: the total amount Bethany received for the items after the auction.
    """
    # L1
    tv_initial_price = 500 # cost was $500
    tv_increase_fraction = Fraction(2, 5) # increased by 2/5 times its initial price
    tv_price_increase = tv_increase_fraction * tv_initial_price

    # L2
    tv_final_price = tv_initial_price + tv_price_increase

    # L3
    phone_initial_price = 400 # which was $400
    phone_increase_percentage = Fraction(40, 100) # increased by 40% from its original price
    phone_price_increase = phone_increase_percentage * phone_initial_price

    # L4
    phone_final_price = phone_initial_price + phone_price_increase

    # L5
    total_received_amount = tv_final_price + phone_final_price

    # FA
    answer = total_received_amount
    return answer