def solve():
    """Index: 5813.
    Returns: the number of machines needed to make the desired number of cell phones per minute.
    """
    # L1
    total_phones_made_by_machines = 10 # 10 cell phones
    number_of_machines = 2 # 2 machines
    phones_per_machine_per_minute = total_phones_made_by_machines / number_of_machines

    # L2
    desired_total_phones = 50 # 50 cell phones a minute
    machines_needed = desired_total_phones / phones_per_machine_per_minute

    # FA
    answer = machines_needed
    return answer