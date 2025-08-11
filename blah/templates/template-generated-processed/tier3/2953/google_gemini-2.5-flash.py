def solve():
    """Index: 2953.
    Returns: the total number of pies eaten.
    """
    # L1
    sierra_pies = 12 # If Sierra ate 12 pies
    sierra_multiplier = 2 # twice as many pies as Bill
    bill_pies = sierra_pies / sierra_multiplier

    # L2
    adam_extra_pies = 3 # Adam eats three more pies than Bill
    adam_pies = bill_pies + adam_extra_pies

    # L3
    total_pies = bill_pies + adam_pies + sierra_pies

    # FA
    answer = total_pies
    return answer