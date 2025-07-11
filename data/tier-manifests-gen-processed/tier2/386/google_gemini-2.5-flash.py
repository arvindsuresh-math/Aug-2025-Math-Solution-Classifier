def solve():
    """Index: 386.
    Returns: the total money Daniela spends.
    """
    # L1
    shoe_price_per_pair = 50 # $50 a pair
    num_shoe_pairs = 2 # 2 pairs of shoes
    original_shoes_cost = shoe_price_per_pair * num_shoe_pairs

    # L2
    total_percent = 100 # WK
    shoe_discount_percent = 40 # 40 percent off on shoes
    shoe_paid_percent = total_percent - shoe_discount_percent

    # L3
    shoe_paid_decimal_factor = 0.60 # WK
    final_shoes_cost = original_shoes_cost * shoe_paid_decimal_factor

    # L4
    dress_discount_percent = 20 # 20 percent off dresses
    dress_paid_percent = total_percent - dress_discount_percent

    # L5
    original_dress_price = 100 # dress originally priced at $100
    dress_paid_decimal_factor = 0.80 # WK
    final_dress_cost = original_dress_price * dress_paid_decimal_factor

    # L6
    total_spent = final_shoes_cost + final_dress_cost

    # FA
    answer = total_spent
    return answer