def solve():
    """Index: 1132.
    Returns: the total number of employees in the factory now.
    """
    # L1
    initial_employees = 852 # employed 852 people
    percentage_increase_numerator = 25 # 25% more workers
    percentage_denominator = 100 # 25% more workers
    new_workers_added = initial_employees * percentage_increase_numerator / percentage_denominator

    # L2
    total_employees = initial_employees + new_workers_added

    # FA
    answer = total_employees
    return answer