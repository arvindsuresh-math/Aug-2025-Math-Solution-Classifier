def solve():
    """Index: 6398.
    Returns: the total money Lily has spent on hydrangeas.
    """
    # L1
    current_year = 2021 # By 2021
    start_year = 1989 # Since 1989
    num_years = current_year - start_year

    # L2
    plant_cost = 20.00 # Each plant costs $20.00
    total_spent = plant_cost * num_years

    # FA
    answer = total_spent
    return answer