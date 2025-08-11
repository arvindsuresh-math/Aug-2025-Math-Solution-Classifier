def solve():
    """Index: 1146.
    Returns: the total amount of money Jane earned.
    """
    # L1
    tulip_bulbs = 20 # Jane planted 20 tulip bulbs
    pay_per_bulb = 0.50 # Jane's mother agreed to pay her $.50 for every flower bulb
    tulip_earnings = tulip_bulbs * pay_per_bulb

    # L2
    iris_bulbs = tulip_bulbs / 2

    # L3
    iris_earnings = iris_bulbs * pay_per_bulb

    # L4
    daffodil_bulbs = 30 # She also planted 30 daffodil bulbs
    daffodil_earnings = daffodil_bulbs * pay_per_bulb

    # L5
    crocus_bulbs = daffodil_bulbs * 3

    # L6
    crocus_earnings = crocus_bulbs * pay_per_bulb

    # L7
    total_earnings = tulip_earnings + iris_earnings + daffodil_earnings + crocus_earnings

    # FA
    answer = total_earnings
    return answer