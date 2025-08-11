def solve():
    """Index: 1242.
    Returns: the number of pounds Vinny lost throughout the fifth month.
    """
    # L1
    first_month_loss = 20 # lost 20 pounds in the first month
    half_factor = 2 # WK
    second_month_loss = first_month_loss / half_factor

    # L2
    third_month_loss = second_month_loss / half_factor

    # L3
    fourth_month_loss = third_month_loss / half_factor

    # L4
    total_loss_first_four_months = first_month_loss + second_month_loss + third_month_loss + fourth_month_loss

    # L5
    initial_weight = 300 # Vinny weighed 300 pounds
    final_weight = 250.5 # weighed 250.5 pounds at the end of his diet
    total_loss_entire_diet = initial_weight - final_weight

    # L6
    fifth_month_loss = total_loss_entire_diet - total_loss_first_four_months

    # FA
    answer = fifth_month_loss
    return answer