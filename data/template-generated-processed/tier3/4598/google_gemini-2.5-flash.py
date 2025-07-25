def solve():
    """Index: 4598.
    Returns: the total amount spent on buying t-shirts.
    """
    # L1
    total_employees = 40 # total of 40 employees
    num_shirt_categories = 4 # 2 sectors, men and women (2*2=4 categories)
    shirts_per_category = total_employees / num_shirt_categories

    # L2
    white_men_shirt_price = 20 # $20 for white men's t-shirts
    cost_white_men_shirts = white_men_shirt_price * shirts_per_category

    # L3
    price_difference = 5 # $5 cheaper
    cost_white_women_shirts = (white_men_shirt_price - price_difference) * shirts_per_category

    # L4
    black_men_shirt_price = 18 # $18 for black men's t-shirts
    cost_black_men_shirts = black_men_shirt_price * shirts_per_category

    # L5
    cost_black_women_shirts = (black_men_shirt_price - price_difference) * shirts_per_category

    # L6
    total_cost = cost_white_men_shirts + cost_white_women_shirts + cost_black_men_shirts + cost_black_women_shirts

    # FA
    answer = total_cost
    return answer