def solve():
    """Index: 386.
    Returns: the total amount Daniela spends on shoes and a dress after discounts.
    """
    # L1
    shoe_price = 50 # $50 a pair
    num_shoes = 2 # 2 pairs of shoes
    total_shoe_price = shoe_price * num_shoes

    # L2
    shoes_discount_percent = 40 # 40 percent off on shoes
    full_percent = 100 # WK
    shoes_pay_percent = full_percent - shoes_discount_percent

    # L3
    shoes_pay_decimal = 0.60 # 60 percent as decimal
    discounted_shoes_cost = total_shoe_price * shoes_pay_decimal

    # L4
    dress_discount_percent = 20 # 20 percent off dresses
    dress_pay_percent = full_percent - dress_discount_percent

    # L5
    dress_price = 100 # dress originally priced at $100
    dress_pay_decimal = 0.80 # 80 percent as decimal
    discounted_dress_cost = dress_price * dress_pay_decimal

    # L6
    total_spent = discounted_shoes_cost + discounted_dress_cost

    # FA
    answer = total_spent
    return answer