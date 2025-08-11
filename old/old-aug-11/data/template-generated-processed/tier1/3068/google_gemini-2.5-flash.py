def solve():
    """Index: 3068.
    Returns: the number of units sold to Customer B.
    """
    # L1
    total_units = 20 # 20 units of phones
    defective_units = 5 # 5 defective units
    non_defective_units = total_units - defective_units

    # L2
    customer_a_units = 3 # customer A who bought 3 units
    customer_c_units = 7 # customer C who bought 7 units
    units_sold_ac = customer_a_units + customer_c_units

    # L3
    units_sold_b = non_defective_units - units_sold_ac

    # FA
    answer = units_sold_b
    return answer