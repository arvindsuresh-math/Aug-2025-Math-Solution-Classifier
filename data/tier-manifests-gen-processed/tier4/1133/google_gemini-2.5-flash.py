def solve():
    """Index: 1133.
    Returns: the amount of change Marcus will have after buying all the water he needs.
    """
    # L1
    num_balloons = 100 # 100 balloons
    ounces_per_balloon = 3 # Each balloon holds 3 ounces of water
    total_ounces_needed = num_balloons * ounces_per_balloon

    # L2
    ounces_per_bottle = 50 # 50 ounces of water
    num_bottles_needed = total_ounces_needed / ounces_per_bottle

    # L3
    cost_per_bottle = 2.5 # $2.5 a bottle
    total_cost = num_bottles_needed * cost_per_bottle

    # L4
    num_ten_dollar_bills = 2 # 2 $10 bills
    value_of_ten_dollar_bill = 10 # $10 bills
    money_had = num_ten_dollar_bills * value_of_ten_dollar_bill

    # L5
    change = money_had - total_cost

    # FA
    answer = change
    return answer