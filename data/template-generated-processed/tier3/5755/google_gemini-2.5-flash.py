def solve():
    """Index: 5755.
    Returns: the average age of John, Mary, and Tonya.
    """
    # L1
    tonya_age = 60 # If Tanya is 60
    john_divisor = 2 # half as old as Tonya
    john_age = tonya_age / john_divisor

    # L2
    mary_divisor = 2 # twice as old as Mary
    mary_age = john_age / mary_divisor

    # L3
    total_age = tonya_age + john_age + mary_age

    # L4
    number_of_people = 3 # WK
    average_age = total_age / number_of_people

    # FA
    answer = average_age
    return answer