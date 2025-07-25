def solve():
    """Index: 4419.
    Returns: the number of $10 bills Mark needs to use.
    """
    # L1
    num_soup_cans = 6 # 6 2$ cans of soup
    cost_per_soup_can = 2 # 2$ cans of soup
    cost_soup = num_soup_cans * cost_per_soup_can

    # L2
    num_bread_loaves = 2 # 2 $5 loaves of bread
    cost_per_bread_loaf = 5 # $5 loaves of bread
    cost_bread = num_bread_loaves * cost_per_bread_loaf

    # L3
    num_cereal_boxes = 2 # 2 3$ boxes of cereal
    cost_per_cereal_box = 3 # 3$ boxes of cereal
    cost_cereal = num_cereal_boxes * cost_per_cereal_box

    # L4
    num_milk_gallons = 2 # 2 $4 gallons of milk
    cost_per_milk_gallon = 4 # $4 gallons of milk
    cost_milk = num_milk_gallons * cost_per_milk_gallon

    # L5
    total_spent = cost_soup + cost_bread + cost_cereal + cost_milk

    # L6
    bill_denomination = 10 # $10 bills
    intermediate_bills_float = total_spent / bill_denomination
    num_bills_needed = (total_spent + bill_denomination - 1) // bill_denomination

    # FA
    answer = num_bills_needed
    return answer