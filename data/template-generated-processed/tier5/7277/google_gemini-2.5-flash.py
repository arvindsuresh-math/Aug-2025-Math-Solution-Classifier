def solve():
    """Index: 7277.
    Returns: the total price spent on shoes.
    """
    # Define inputs from the question that are used to derive shoe_price_per_pair (X)
    num_pairs_shoes_bought = 6 # 6 pairs of shoes
    num_jerseys_bought = 4 # 4 jerseys
    jersey_price_fraction_of_shoe = 1/4 # 1/4 price of one pair of shoes
    total_cost_all_items = 560 # $560

    # Implicitly solving the equation from L1-L5:
    # L1: Let X be the shoe price. The jersey's price is 1/4*X.
    # L2: Jeff bought 6 pairs of shoes and 4 jerseys for 6*X + 4*(1/4X) = $560.
    # L3: Multiplying through the parentheses produces 6X + X = $560
    # L4: Combining like terms produces 7X = $560
    # L5: Dividing both sides by 7 produces X = $80
    shoe_price_per_pair = total_cost_all_items / (num_pairs_shoes_bought + num_jerseys_bought * jersey_price_fraction_of_shoe)

    # L6
    total_shoe_cost = shoe_price_per_pair * num_pairs_shoes_bought

    # FA
    answer = total_shoe_cost
    return answer