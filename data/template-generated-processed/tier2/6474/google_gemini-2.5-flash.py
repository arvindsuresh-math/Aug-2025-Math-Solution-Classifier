def solve():
    """Index: 6474.
    Returns: how much more money one company made from the other.
    """
    # L1
    company_a_bottles_sold = 300 # Company A was able to sell 300
    company_a_bottle_price = 4 # Company A sells a big bottle for $4
    company_a_earnings = company_a_bottles_sold * company_a_bottle_price

    # L2
    company_b_bottles_sold = 350 # company B 350 big bottles
    company_b_bottle_price = 3.5 # Company B sells a big bottle for $3.5
    company_b_earnings = company_b_bottles_sold * company_b_bottle_price

    # L3
    earnings_difference = company_b_earnings - company_a_earnings

    # FA
    answer = earnings_difference
    return answer