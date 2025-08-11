def solve():
    """Index: 5192.
    Returns: the total number of points Martha gets.
    """
    # L1
    beef_price_per_pound = 11 # 3 pounds of beef for $11 each
    beef_pounds = 3 # 3 pounds of beef
    total_beef_cost = beef_price_per_pound * beef_pounds

    # L2
    fruits_veg_price_per_pound = 4 # 8 pounds of fruits and vegetables for $4/pound
    fruits_veg_pounds = 8 # 8 pounds of fruits and vegetables
    total_fruits_veg_cost = fruits_veg_price_per_pound * fruits_veg_pounds

    # L3
    spice_price_per_jar = 6 # 3 jars of spices for $6 each
    spice_jars = 3 # 3 jars of spices
    total_spice_cost = spice_price_per_jar * spice_jars

    # L4
    other_groceries_cost = 37 # other groceries totaling $37
    total_spending = total_beef_cost + total_fruits_veg_cost + total_spice_cost + other_groceries_cost

    # L5
    points_per_block = 50 # 50 points per $10 spent
    spending_block = 10 # per $10 spent
    points_per_dollar = points_per_block / spending_block

    # L6
    points_before_bonus = total_spending * points_per_dollar

    # L7
    bonus_points = 250 # a 250 point bonus
    bonus_threshold = 100 # if she spends more than $100
    total_points = points_before_bonus + bonus_points

    # FA
    answer = total_points
    return answer