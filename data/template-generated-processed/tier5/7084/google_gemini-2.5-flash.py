def solve():
    """Index: 7084.
    Returns: the number of boxes Sally sold on Saturday.
    """
    # L2
    # The problem states "50% more on Sunday than she sold on Saturday".
    # This means Sunday sales are 1.5 times Saturday sales (S + 0.5*S).
    # The total sales are given as 150.
    # So, the equation is S + 1.5S = 150.
    sunday_increase_factor = 0.5 # 50% more
    sunday_sales_multiplier = 1 + sunday_increase_factor
    total_boxes_sold = 150 # total of 150 boxes on the two days

    # L3
    # Combine the coefficients for S: S + 1.5S simplifies to 2.5S.
    combined_s_coefficient = 1 + sunday_sales_multiplier

    # L4
    # Solve for S: 2.5S = 150 => S = 150 / 2.5
    saturday_sales = total_boxes_sold / combined_s_coefficient

    # FA
    answer = saturday_sales
    return answer