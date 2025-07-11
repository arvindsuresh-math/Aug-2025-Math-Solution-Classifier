def solve():
    """Index: 1242.
    Returns: the number of pounds Vinny lost in the fifth month.
    """
    # L1
    first_month_loss = 20 # lost 20 pounds in the first month
    second_month_loss = first_month_loss / 2

    # L2
    third_month_loss = second_month_loss / 2

    # L3
    fourth_month_loss = third_month_loss / 2

    # L4
    total_first_four_months_loss = first_month_loss + second_month_loss + third_month_loss + fourth_month_loss

    # L5
    initial_weight = 300 # Vinny weighed 300 pounds
    final_weight = 250.5 # Vinny weighed 250.5 pounds at the end
    total_loss = initial_weight - final_weight

    # L6
    fifth_month_loss = total_loss - total_first_four_months_loss

    # FA
    answer = fifth_month_loss
    return answer