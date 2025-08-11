def solve():
    """Index: 3556.
    Returns: the amount of money Kathleen has left.
    """
    # L1
    saved_june = 21 # saved $21 in June
    saved_july = 46 # saved $46 in July
    saved_august = 45 # saved $45 in August
    total_saved = saved_june + saved_july + saved_august

    # L2
    aunt_threshold = 125 # saves more than $125
    aunt_gift = 25 # give Kathleen $25
    # The solution states Kathleen's aunt did not give Kathleen any money because total_saved (112) is not greater than aunt_threshold (125).
    # Therefore, no money is added from the aunt.

    # L3
    spent_school_supplies = 12 # spent $12 on school supplies
    spent_new_clothes = 54 # spent $54 on new clothes
    total_spent = spent_school_supplies + spent_new_clothes

    # L4
    money_left = total_saved - total_spent

    # FA
    answer = money_left
    return answer