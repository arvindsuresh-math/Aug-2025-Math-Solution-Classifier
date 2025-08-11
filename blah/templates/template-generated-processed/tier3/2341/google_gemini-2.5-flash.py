def solve():
    """Index: 2341.
    Returns: the total number of objects Bill tossed into the river.
    """
    # L1
    ted_sticks = 10 # Ted tosses 10 sticks
    bill_more_sticks = 6 # Bill throws 6 more sticks into the river than Ted does
    bill_sticks = ted_sticks + bill_more_sticks

    # L2
    ted_rocks = 10 # 10 rocks
    ted_rocks_multiplier = 2 # Ted tosses twice as many rocks into the river as Bill
    bill_rocks = ted_rocks / ted_rocks_multiplier

    # L3
    total_bill_objects = bill_sticks + bill_rocks

    # FA
    answer = total_bill_objects
    return answer