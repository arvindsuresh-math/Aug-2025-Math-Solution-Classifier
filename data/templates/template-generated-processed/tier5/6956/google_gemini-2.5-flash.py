def solve():
    """Index: 6956.
    Returns: the number of $10 bills given.
    """
    # Define initial parameters from the question and world knowledge
    total_cost = 80 # Viggo spent $80
    value_10_bill = 10 # WK
    value_20_bill = 20 # WK
    extra_20_bills = 1 # one more $20 bill than $10 bills

    # L1: Let x be the number of $10 bills.
    # L2: So, there are (x + 1) $20 bills.
    # L3: Adding the $10 and $20 bills should sum up to $80 so the equation is 10x + 20(x + 1) = 80.
    # L4: Then, distribute 20 to x + 1 so it becomes 10x + 20x + 20 = 80.
    constant_term_from_distribution = value_20_bill * extra_20_bills

    # L5: Combining the like terms on the left side gives 30x + 20 = 80.
    combined_x_coefficient = value_10_bill + value_20_bill

    # L6: Then transfer 20 to the right side of the equation, so it becomes 30x = 60.
    right_side_after_transfer = total_cost - constant_term_from_distribution

    # L7
    num_10_bills = right_side_after_transfer / combined_x_coefficient

    # FA
    answer = num_10_bills
    return answer